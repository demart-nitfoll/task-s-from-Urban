import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_walker = Runner('tester')
        for i in range(10):
            test_walker.walk()
        self.assertEqual(test_walker.distance, 50)
    def test_run(self):
        test_runner = Runner('tester')
        for i in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)
    def test_challenge(self):
        test_runner = Runner('run_tester')
        test_walker = Runner('walk_tester')
        for i in range(10):
            test_walker.walk()
            test_runner.run()
        self.assertNotEqual(test_runner, test_walker)

if __name__ == '__main__':
    unittest.main()

