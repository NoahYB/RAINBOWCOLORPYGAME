class rainbow:
    #250,250,0
    def __init__(self,red,green,blue):
        self.r = red
        self.g = green
        self.b = blue
    def green_func(self):
        if self.r == 250 and self.g < 250 and self.b == 0:
            self.g += 2
            return self.g
        elif self.r == 0 and self.g > 0 and self.b == 250:
            self.g -= 2
            return self.g
        else:
            return self.g
    def red_func(self):
        if self.r > 0 and self.g == 250 and self.b == 0:
            self.r -= 2
            return self.r
        elif self.r < 250 and self.g == 0 and self.b == 250:
            self.r += 2
            return self.r
        else:
            return self.r
    def blue_func(self):
        if self.r == 0 and self.g == 250 and self.b < 250:
            self.b += 2
            return self.b
        elif self.r == 250 and self.g == 0 and self.b > 0:
            self.b -= 2
            return self.b
        else:
            return self.b
