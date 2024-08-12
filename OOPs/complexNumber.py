class ComplexNumber:
    
    # dunder / magic method 
    def __init__(self, real = 0.0, imaginary = 0.0):
        self.real = real
        self.imaginary = imaginary
        
        
    def conjugate(self):
        # imaginary = self.imaginary * -1
        # print(f"({self.real } + { imaginary}i)")
        
        return ComplexNumber(self.real, -1 * self.imaginary)
     
     
    # dunder / magic method    
    def __str__(self):
        
        if(self.real == 0):
            return f"{self.imaginary}i"
        
        
        elif(self.imaginary < 0):
            imaginary = abs(self.imaginary)
            return f"({self.real} - {imaginary}i)"
        
        else:
            return f"({self.real} + {self.imaginary}i)"
        
    
    
    def __add__(self, other):
        resultReal = 0
        resultImaginary = 0
        
        resultReal = self.real + other.real
        resultImaginary = self.imaginary + other.imaginary
        
        ans = ComplexNumber(resultReal, resultImaginary)
        
        return ans
    
    
    def __sub__(self, other):
        resultReal = 0
        resultImaginary = 0
        
        resultReal = self.real - other.real
        resultImaginary = self.imaginary - other.imaginary
        
        ans = ComplexNumber(resultReal, resultImaginary)
        
        return ans
    
    
    
    def __mul__(self, other):
        resultReal = 0
        resultImaginary = 0
        
        resultReal = (self.real * other.real) - (self.imaginary * other.imaginary)
        
        resultImaginary = (self.real * other.imaginary) + (other.real * self.imaginary)
        
        ans = ComplexNumber(resultReal, resultImaginary)
        
        return ans
    
    
    def __truediv__(self, other):
        resultReal = 0
        resultImaginary = 0
        
        denominator = other.real ** 2 + other.imaginary ** 2
        
        ans = self * ComplexNumber(other.real / denominator, (-1 * other.imaginary) / denominator)
        
        return ans
    
    
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
    
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
        
        
        
cn = ComplexNumber(3,3)
print(cn.conjugate())
# print(cn)

cn1 = ComplexNumber(5,-5)
print(cn1)

# cn2 = ComplexNumber(0, 5)
# print(cn2)

# print(cn+cn1)
# print(cn-cn1)
# print(cn*cn1)
# print(cn/cn1)
# print(cn == cn1)
print(cn != cn1)



