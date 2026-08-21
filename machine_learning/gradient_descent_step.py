def gradient_step(parameters, gradients, learning_rate):
    return  [parameter - learning_rate* gradient for parameter, gradient in zip(parameters, gradients)]