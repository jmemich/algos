#include <math.h>
#include <iostream>
#include <eigen/Dense>

using namespace Eigen;

struct GradParams
{
    float b0;
    Eigen::VectorXf betas;
};

// TODO vectorize
GradParams gradient(const Eigen::VectorXf & x,
                    const float & y,
                    const Eigen::VectorXf & betas,
                    const float & b0)
{
    GradParams gparams;
    float y_hat = b0+betas.dot(x);
    gparams.b0 = -2*(y-y_hat); // dB0/dB0 = 1
    gparams.betas = -2*(y-y_hat)*x; // dBiXi/dBi = Xi
    return gparams;
}

float loss(const Eigen::MatrixXf & X,
           const Eigen::VectorXf & y,
           const Eigen::VectorXf & betas,
           const float b0)
{
    float err = 0;
    float y_hat;
    for (int i=0; i<X.rows(); i++) {
        y_hat = b0 + betas.dot(X.row(i));
        err += std::pow(y[i]-y_hat, 2);
    }
    return err/X.rows();
}

void linreg(const Eigen::MatrixXf & X,
            const Eigen::VectorXf & y) {
    // TODO set seed
    float b0 = 1.0; // TODO make random
    Eigen::VectorXf betas = Eigen::VectorXf::Ones(3); // TODO make random

    float err;
    int steps = 10000;
    float alpha = 0.01;
    for (int step=0; step<steps; step++) { 
        for (int i=0; i<X.rows(); i++) {
            GradParams gparams = gradient(X.row(i), y[i], betas, b0);
            b0 -= alpha*gparams.b0;
            betas -= alpha*gparams.betas;
        }
        err = loss(X,y,betas,b0);
        // std::cout << "step: " << step+1 << "|err: " << err << std::endl;;
    }
    std::cout << "b0: " << b0 << std::endl;
    std::cout << "betas: " << betas.transpose() << std::endl;
}

int main() {
    Eigen::MatrixXf X(10,3);
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

    Eigen::VectorXf y(10);
    y << 1,2,3,4,5,6,7,8,9,10;

    linreg(X,y);
}
