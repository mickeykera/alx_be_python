from class_static_methods_demo import Calculator

print("Testing Calculator class...")

# Test static method
sum_result = Calculator.add(10, 5)
print(f"The sum is: {sum_result}")

# Test class method
product_result = Calculator.multiply(10, 5)
print(f"The product is: {product_result}")

print("All tests completed!")
