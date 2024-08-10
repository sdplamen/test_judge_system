import unittest

# Define the task function (the problem statement)
def task_run(input_data):
    # Put the code from problem solution and return the result

    # For example:
    products = {}
    for line in input_data.split('\n'):
        if line == 'statistics':
            break
        product, quantity = line.split(': ')
        quantity = int(quantity)
        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

    output = 'Products in stock:\n'
    for product, quantity in products.items():
        output += f'- {product}: {quantity}\n'
    output += f'Total Products: {len(products)}\n'
    output += f'Total Quantity: {sum(products.values())}'
    return output


# User-provided solution (to be tested)
def user_solution_run(input_data):
    # Put the code from user solution and return the result

    # For example:
    products = {}
    for line in input_data.split('\n'):
        if line == 'statistics':
            break
        product, quantity = line.split(': ')
        quantity = int(quantity)
        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

    output = 'Products in stock:\n'
    for product, quantity in products.items():
        output += f'- {product}: {quantity}\n'
    output += f'Total Products: {len(products)}\n'
    output += f'Total Quantity: {sum(products.values())}'
    return output


# Define the test case for the task
class TestTask(unittest.TestCase):
    correct_tests = 0
    total_tests = 0

    # Put the test functions here
    # For Example:

    def run_test(self, func, input_data, expected_output):
        TestTask.total_tests += 1
        if func(input_data) == expected_output:
            TestTask.correct_tests += 1

    def test_task(self):
        input_data = 'bread: 4\ncheese: 2\nham: 1\nbread: 1\nstatistics'
        expected_output = '''Products in stock:
        - bread: 5
        - cheese: 2
        - ham: 1
        Total Products: 3
        Total Quantity: 8'''


    # Run the test for task_run function
        self.run_test(task_run, input_data, expected_output)
    # Run the test for user_solution_run function
        self.run_test(user_solution_run, input_data, expected_output)

# Main judge function to run the tests
def judge():
    # Load the test cases from TestTask class
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestTask)
    # Run the test suite
    runner = unittest.TextTestRunner(resultclass=unittest.TextTestResult, verbosity=2)
    result = runner.run(suite)
    # Retrieve the correct and total tests count
    total_tests = TestTask.total_tests
    correct_tests = TestTask.correct_tests
    # Calculate and print the success rate
    success_rate = (correct_tests / total_tests) * 100 if total_tests > 0 else 0
    print(f'Success Rate: {success_rate:.2f}% ({correct_tests}/{total_tests}) tests passed')


if __name__ == "__main__":
    judge()
