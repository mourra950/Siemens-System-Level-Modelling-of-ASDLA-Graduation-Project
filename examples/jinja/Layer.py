class Layer:
    def __init__(self, channels, filters, height, width, units, stride, padding, name, kernel_size):
        self.channels = channels
        self.filters = filters
        self.height = height
        self.width = width
        self.units = units
        self.stride = stride
        self.padding = padding
        self.name = name
        self.kernel_size = kernel_size
