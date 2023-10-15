""" A package delivery service charges a flat fee of $10 for shipping and an additional 5% of the
package's value as an insurance fee. Write a function to calculate the total cost (C) to ship a
package based on its value (P). """

def calculate_shipping_cost(package_value):
  """Calculates the total cost to ship a package based on its value.

  Args:
    package_value: The value of the package.

  Returns:
    The total cost to ship the package.
  """

  insurance_fee = package_value * 0.05
  total_cost = insurance_fee + 10
  return total_cost

# Example usage:

package_value = 100
total_cost = calculate_shipping_cost(package_value)

print(f"The total cost to ship the package is ${total_cost:.2f}.")
