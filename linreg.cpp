#include <math.h>
#include <iostream>
#include <eigen/Dense>

using namespace Eigen;

VectorXf linreg(const MatrixXf & X,
                const VectorXf & y,
                const float & alpha,
                const int & steps) {
    float b0 = 0.0;
    VectorXf betas = VectorXf::Random(3);  // TODO seed
    float err, y_hat;
    for (int step=0; step<steps; step++) { 
        err = 0;
        for (int i=0; i<X.rows(); i++) {
            y_hat = b0+betas.dot(X.row(i));
            b0 -= alpha*-2*(y[i]-y_hat); // dB0/dB0 = 1
            betas -= alpha*-2*(y[i]-y_hat)*X.row(i); // dBiXi/dBi = Xi
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
    VectorXf result = VectorXf(1+betas.rows());
    result(0) = b0;
    for (int i=0; i<betas.rows(); i++) {
        result(i+1) = betas(i);
    }
    return result;
}

int main() {
    MatrixXf X(10,3);
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

    VectorXf y(10);
    y << 1,2,3,4,5,6,7,8,9,10;

    float alpha = 0.01;
    int steps = 10000;
    VectorXf params = linreg(X,y,alpha,steps);
    std::cout << "parameters: " << params.transpose() << std::endl;
    return 0;
}
