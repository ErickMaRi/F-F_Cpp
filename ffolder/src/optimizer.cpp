// src/optimizer.cpp

#include "optimizer.hpp"

#include <cmath>
#include <stdexcept>

// Implementación del constructor de AdamOptimizer
AdamOptimizer::AdamOptimizer(float learning_rate, float beta1, float beta2, float epsilon)
    : lr(learning_rate), beta1(beta1), beta2(beta2), eps(epsilon),
      t_weights(0), t_biases(0),
      m_weights(), v_weights(),
      m_biases(), v_biases() {}

// Implementación de updateWeights
void AdamOptimizer::updateWeights(Eigen::MatrixXf& weights,
                                  const Eigen::MatrixXf& gradients) {
    if (m_weights.size() == 0) {
        m_weights = Eigen::MatrixXf::Zero(weights.rows(), weights.cols());
        v_weights = Eigen::MatrixXf::Zero(weights.rows(), weights.cols());
    }

    ++t_weights;
    m_weights = beta1 * m_weights + (1.0f - beta1) * gradients;
    v_weights = beta2 * v_weights + (1.0f - beta2) * gradients.array().square().matrix();
    Eigen::MatrixXf m_hat = m_weights.array() / (1.0f - std::pow(beta1, t_weights));
    Eigen::MatrixXf v_hat = v_weights.array() / (1.0f - std::pow(beta2, t_weights));

    weights.array() -= lr * m_hat.array() / (v_hat.array().sqrt() + eps);
}

// Implementación de updateBiases
void AdamOptimizer::updateBiases(Eigen::VectorXf& biases,
                                 const Eigen::VectorXf& gradients) {
    if (m_biases.size() == 0) {
        m_biases = Eigen::VectorXf::Zero(biases.size());
        v_biases = Eigen::VectorXf::Zero(biases.size());
    }

    ++t_biases;
    m_biases = beta1 * m_biases + (1.0f - beta1) * gradients;
    v_biases = beta2 * v_biases + (1.0f - beta2) * gradients.array().square().matrix();
    Eigen::VectorXf m_hat = m_biases.array() / (1.0f - std::pow(beta1, t_biases));
    Eigen::VectorXf v_hat = v_biases.array() / (1.0f - std::pow(beta2, t_biases));

    biases.array() -= lr * m_hat.array() / (v_hat.array().sqrt() + eps);
}