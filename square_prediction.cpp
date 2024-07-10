#include <iostream>
#include <math.h>
#include <vector>
#include <cstdlib>  // For rand() and srand()
#include <ctime>    // For time()


using namespace std;

double predict(double x, double a, double b, double c) {
    return a * x * x + b * x + c;
}

double mean_squared_error(vector<double> X, vector<double> y, double a, double b, double c) {
    double errors = 0;
    for (size_t i = 0; i < X.size(); i++)
        errors += pow((predict(X[i], a, b, c) - y[i]), 2);

    return errors / X.size();
}

vector<double> gradient_descent(vector<double> X, vector<double> y, double lr=0.00000001, int iter=1000000) {
    std::srand(std::time(0));
    std::vector<double> params(3);

    for(size_t i = 0; i < 3; ++i) 
        params[i] = rand() % 10;

    size_t i = 0;
    size_t n = X.size();

    cout << "iteration      loss           a             b            c" << endl;
    cout << "----------------------------------------------------------------------------" << endl;

    while (i < iter) {
        double da = 0;
        double db = 0;
        double dc = 0;

        for (size_t i = 0; i < X.size(); i++) {
            double x = X[i];
            double y_true = y[i];
            double y_pred = predict(x, params[0], params[1], params[2]);
            double error = y_pred - y_true;
            da += 2 * error * (x * x);
            db += 2 * error * x;
            dc += 2 * error;
        }

        params[0] -= lr * (da / n);
        params[1] -= lr * (db / n);
        params[2] -= lr * (dc / n);

        if (i % 100000 == 0)
            cout << i << "       " << mean_squared_error(X, y, params[0], params[1], params[2]) << "       " << params[0] << "       " << params[1] << "       " << params[2] << endl;
        i++;
    }

    return params;
}

int main () {
    vector<double> X_train;
    for (int i = 1; i <= 100; ++i) {
        X_train.push_back(i);
    }

    vector<double> y_train;
    for (int x : X_train) {
        y_train.push_back(x * x);
    }
    
    auto params = gradient_descent(X_train, y_train);
    cout << "prediction: " << predict(210, params[0], params[1], params[2]) << " actual: "<< 210 * 210 << endl;
}