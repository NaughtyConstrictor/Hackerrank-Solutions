class Complex(object):
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imag = imaginary
    
    def mod(self):
        return type(self)((self.real*self.real + self.imag*self.imag)**0.5)
    
    def imag_symmetry(self):
        return type(self)(self.real, -self.imag)
    
    def __add__(self, no):
        return type(self)(self.real + no.real, self.imag + no.imag)
    
    def __sub__(self, no):
        return type(self)(self.real - no.real, self.imag - no.imag)

    def __mul__(self, no):
        return type(self)(
                        self.real*no.real - self.imag*no.imag, 
                        self.real*no.imag + self.imag*no.real
                        )

    def __truediv__(self, no):
        module = no.mod().real
        module *= module
        temp = self * no.imag_symmetry()
        return type(self)(temp.real / module, temp.imag / module)
    
    def __str__(self):
        return f"{self.real:.2f}{self.imag:+.2f}i"
        # if self.imag == 0:
        #     result = "%.2f+0.00i" % (self.real)
        # elif self.real == 0:
        #     if self.imag >= 0:
        #         result = "0.00+%.2fi" % (self.imag)
        #     else:
        #         result = "0.00-%.2fi" % (abs(self.imag))
        # elif self.imag > 0:
        #     result = "%.2f+%.2fi" % (self.real, self.imag)
        # else:
        #     result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        # return result

