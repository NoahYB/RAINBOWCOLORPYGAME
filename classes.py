class rainbow:
    #250,250,0
    def __init__(self,red,green,blue):
        self.r = red
        self.g = green
        self.b = blue
    def green_func(self):
        if self.r == 240 and self.g < 240 and self.b == 0:
            self.g += 2
            if self.g >240:
                self.g = 240
            return self.g
        elif self.r == 0 and self.g > 0 and self.b == 240:
            self.g -= 2
            return self.g
        else:
            return self.g
    def red_func(self):
        if self.r > 0 and self.g == 240 and self.b == 0:
            self.r -= 2
            return self.r
        elif self.r < 240 and self.g == 0 and self.b == 240:
            self.r += 2.5
            if self.r >240:
                self.r = 240
            return self.r
        else:
            return self.r
    def blue_func(self):
        if self.r == 0 and self.g == 240 and self.b < 240:
            self.b += 2
            if self.b >240:
                self.b = 240
            return self.b
        elif self.r == 240 and self.g == 0 and self.b > 0:
            self.b -= 2
            return self.b
        else:
            return self.b
    def green_func_change(self):
        if self.r == 240 and self.g < 240 and self.b == 0:
            self.g += 10
            if self.g >240:
                self.g = 240
            return self.g
        elif self.r == 0 and self.g > 0 and self.b == 240:
            self.g -= 10
            return self.g
        else:
            return self.g
    def red_func_change(self):
        if self.r > 0 and self.g == 240 and self.b == 0:
            self.r -= 10
            return self.r
        elif self.r < 240 and self.g == 0 and self.b == 240:
            self.r += 10
            if self.r >240:
                self.r = 240
            return self.r
        else:
            return self.r
    def blue_func_change(self):
        if self.r == 0 and self.g == 240 and self.b < 240:
            self.b += 10
            if self.b > 240:
                self.b = 240
            return self.b
            
        elif self.r == 240 and self.g == 0 and self.b > 0:
            self.b -= 10
            return self.b
        else:
            return self.b

