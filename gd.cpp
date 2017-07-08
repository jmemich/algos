#include <iostream>
#include <cmath>


float f(float x)
{
    return (x * x) + (2 * x) - 11;
}


float g(float x)
{
    return (2 * x) + 2;
}


template <typename Value, typename P1,
          typename P2, typename F,
          typename G>
Value gradient_descent(Value x, P1 s, P2 eps, F f, G g)
{
    auto val= f(x), delta= val;
    do {
        x-= s * g(x);
        auto new_val= f(x);
        delta= std::abs(new_val - val);
        val= new_val;
    } while (delta > eps);
    return x;
}


int main ()
{
    float x = 38.92;
    float step = 0.1;
    float eps = 0.001;
    float val = gradient_descent ( x, step, eps, f, g );
    std::cout << "value is... " << val << std::endl;
    
    return 0;
}
