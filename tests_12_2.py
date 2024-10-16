import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.runner_1 = Runner('Усэйн', speed= 10)
        self.runner_2 = Runner('Андрей', speed= 9)
        self.runner_3 = Runner('Ник', speed= 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(cls.all_results[i])

    def test_tour_1(self):
        test_tour = Tournament(90, self.runner_1, self.runner_3)
        results = test_tour.start()
        self.all_results['tour_1'] = {x: results[x].name for x in results}

    def test_tour_2(self):
        test_tour = Tournament(90, self.runner_2, self.runner_3)
        results = test_tour.start()
        self.all_results['tour_2'] = {x: results[x].name for x in results}

    def test_tour_3(self):
        test_tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = test_tour.start()
        self.all_results['tour_3'] = {x: results[x].name for x in results}

if __name__ == '__main__':
    unittest.main()