"""
You are building a simple neural network for a startup that predicts apartment rental prices based on square footage. Your model uses a single linear layer with two parameters: weight (w) and bias (b), making predictions as: `price = w * sqft + b`

You have been given a small dataset of 50 apartments with their square footage and monthly rent. Your task is to:

1. Implement three different optimizers from scratch: Vanilla SGD, SGD with Momentum, and Adam
2. Train your model using each optimizer for 100 epochs with batch size of 10
3. Compare their performance by tracking and visualizing:
    - Loss curves over epochs
    - Final parameter values
    - Convergence speed (how many epochs to reach loss < 5000)
4. Implement a learning rate schedule for Adam (warmup for 10 epochs, then cosine decay) and compare it against constant learning rate Adam

Your initial parameters should be w = 0.0 and b = 0.0.

Use the following hyperparameters:

- SGD learning rate: 0.001
- SGD with Momentum learning rate: 0.001, momentum = 0.9
- Adam learning rate: 0.01, beta1 = 0.9, beta2 = 0.999

**Dataset:**
The true relationship is `price = 2.5 * sqft + 500` with some random noise added.

**Expected Outputs:**

1. Print final loss and parameters for each optimizer
2. Create a comparison plot showing all loss curves on the same graph
3. Answer: Which optimizer converged fastest? Which reached the lowest final loss?
"""

import random
import numpy as np


# Generate synthetic dataset
def generate_dataset(num_samples=50):
    sqft = np.random.uniform(300, 5000, num_samples)
    price = 2.5 * sqft + (500 + np.random.normal(0, 50, num_samples))
    return sqft, price


def vanilla_sgd(w, b, grad_w, grad_b, lr):
    w = w - lr * grad_w
    b = b - lr * grad_b
    return w, b


def sgd_with_momentum(w, b, grad_w, grad_b, lr, momentum, v_w=0.0, v_b=0.0):
    v_w = v_w * momentum + (1 - momentum) * grad_w
    v_b = v_b * momentum + (1 - momentum) * grad_b
    w = w - lr * v_w
    b = b - lr * v_b
    return w, b, v_w, v_b


def adam_optimizer(
    w,
    b,
    grad_w,
    grad_b,
    lr,
    beta1,
    beta2,
    t,
    m_a_w=0.0,
    m_a_b=0.0,
    v_a_w=0.0,
    v_a_b=0.0,
):
    m_a_w = beta1 * m_a_w + (1 - beta1) * grad_w
    m_a_b = beta1 * m_a_b + (1 - beta1) * grad_b
    v_a_w = beta2 * v_a_w + (1 - beta2) * (grad_w**2)
    v_a_b = beta2 * v_a_b + (1 - beta2) * (grad_b**2)

    m_a_w_hat = m_a_w / (1 - beta1**t)
    m_a_b_hat = m_a_b / (1 - beta1**t)
    v_a_w_hat = v_a_w / (1 - beta2**t)
    v_a_b_hat = v_a_b / (1 - beta2**t)

    w = w - lr * m_a_w_hat / (np.sqrt(v_a_w_hat) + 1e-8)
    b = b - lr * m_a_b_hat / (np.sqrt(v_a_b_hat) + 1e-8)
    return w, b, m_a_w, m_a_b, v_a_w, v_a_b


def calculate_loss(sqft, price, optimizer):
    start_w = 0.0
    start_b = 0.0
    v_w, v_b = 0.0, 0.0
    v_a_w, v_a_b = 0.0, 0.0
    m_a_w, m_a_b = 0.0, 0.0
    t = 0
    losses = []
    # Normalization
    sqft = (sqft - np.mean(sqft)) / np.std(sqft)
    price = (price - np.mean(price)) / np.std(price)

    for epoch in range(100):
        indices = np.random.permutation(len(sqft))
        for batch in range(0, len(sqft), 10):
            x_batch = sqft[indices[batch : batch + 10]]
            y_batch = price[indices[batch : batch + 10]]

            # forward pass
            y_pred = start_w * x_batch + start_b

            # calculate loss
            loss = np.mean((y_pred - y_batch) ** 2)
            losses.append(loss)
            # calculate gradients
            grad_w = np.mean(2 * (y_pred - y_batch) * x_batch)
            grad_b = np.mean(2 * (y_pred - y_batch))

            # update parameters
            if optimizer == "vanilla_sgd":
                start_w, start_b = vanilla_sgd(
                    start_w, start_b, grad_w, grad_b, lr=0.001
                )
            elif optimizer == "sgd_momentum":
                start_w, start_b, v_w, v_b = sgd_with_momentum(
                    start_w,
                    start_b,
                    grad_w,
                    grad_b,
                    lr=0.001,
                    momentum=0.9,
                    v_w=v_w,
                    v_b=v_b,
                )
            elif optimizer == "adam_constant":
                start_w, start_b, m_a_w, m_a_b, v_a_w, v_a_b = adam_optimizer(
                    start_w,
                    start_b,
                    grad_w,
                    grad_b,
                    lr=0.01,
                    beta1=0.9,
                    beta2=0.999,
                    t=t + 1,
                    m_a_w=m_a_w,
                    m_a_b=m_a_b,
                    v_a_w=v_a_w,
                    v_a_b=v_a_b,
                )
            else:
                total_steps = 100 * (len(sqft) // 10)  # 100 epochs × batches
                warmup_steps = 10 * (len(sqft) // 10)
                # Adam with learning rate schedule
                if t < warmup_steps:
                    lr = 0.01 * (t) / warmup_steps  # warmup - 10 epochs
                else:
                    progress = (t - warmup_steps) / (total_steps - warmup_steps)
                    lr = 0.01 * 0.5 * (1 + np.cos(np.pi * progress))  # cosine decay

                start_w, start_b, m_a_w, m_a_b, v_a_w, v_a_b = adam_optimizer(
                    start_w,
                    start_b,
                    grad_w,
                    grad_b,
                    lr=lr,
                    beta1=0.9,
                    beta2=0.999,
                    t=epoch + 1,
                    m_a_w=m_a_w,
                    m_a_b=m_a_b,
                    v_a_w=v_a_w,
                    v_a_b=v_a_b,
                )
    return losses


if __name__ == "__main__":
    sqft, price = generate_dataset()
    print("Dataset generated with 50 samples.")

    optimizers = ["vanilla_sgd", "sgd_momentum", "adam_constant", "adam_schedule"]
    results = {}
    for opt in optimizers:
        print(f"Training with {opt}...")
        losses = calculate_loss(sqft, price, opt)
        results[opt] = losses
        final_loss = losses[-1]
        print(f"Final loss for {opt}: {final_loss:.2f}")
