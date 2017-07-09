#include <math.h>
#include <iostream>
#include <eigen/Dense>

using namespace Eigen;

VectorXd linreg(const MatrixXd & X,
                const VectorXd & y,
                const float & alpha,
                const int & steps,
                const int solver=0) {
    std::cout << "solver : " << ((solver==0) ? "SGD" : "AdaGrad") << std::endl;
    float b0=0.0;
    VectorXd betas = VectorXd::Random(X.cols());  // TODO seed
    float err, y_hat;
    // AdaGrad
    float eps=1e-8; // numerical stability
    float adjalpha;
    float gradb0;
    float Ggradb0=0;
    VectorXd gradbetas;
    VectorXd Ggradbetas = VectorXd::Zero(X.cols());
    for (int step=0; step<steps; step++) {
        err = 0;
        for (int i=0; i<X.rows(); i++) {
            y_hat = b0+betas.dot(X.row(i));
            gradb0 = -2*(y[i]-y_hat); // dB0/dB0 = 1
            gradbetas = -2*(y[i]-y_hat)*X.row(i); // dBiXi/dBi = Xi
            if (solver == 0) { 
                // vanilla SGD
                b0 -= alpha*gradb0;
                betas -= alpha*gradbetas;
            } else if (solver == 1) {
                // AdaGrad
                Ggradb0 += pow(gradb0,2);
                adjalpha = alpha/sqrt(Ggradb0+eps);
                b0 -= adjalpha*gradb0;
                for (int j=0; j<betas.rows(); j++) {  // TODO vectorize
                    Ggradbetas[j] += pow(gradbetas[j],2);
                    adjalpha = alpha/sqrt(Ggradbetas[j]+eps);
                    betas[j] -= adjalpha*gradbetas[j];
                }
            }
            err += std::pow(y[i]-y_hat,2);
        }
        err /= X.rows();
        if (err < 1e-10) {  // early stopping
            std::cout << "stopping early on step " << step+1
                      << " with error " << err
                      << std::endl;
            break;
        }
    }
    VectorXd result = VectorXd(1+betas.rows());
    result(0) = b0;
    for (int i=0; i<betas.rows(); i++) {
        result(i+1) = betas(i);
    }
    return result;
}

int main() {
    MatrixXd X(10,3);
    X << 1.1,1,10,
         2.1,1,1,
         3.1,1,9,
         4.1,1,2,
         5.1,1,8,
         6.1,2,3,
         7.1,2,7,
         8.1,2,4,
         9.1,2,6,
         10.1,2,5;

    VectorXd y(10);
    y << 1,2,3,4,5,6,7,8,9,10;

    float alpha = 0.9;
    int steps = 1000;
    VectorXd params = linreg(X,y,alpha,steps,1);
    std::cout << "parameters: " << params.transpose() << std::endl;
    return 0;
}
