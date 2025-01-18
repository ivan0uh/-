import unittest
import runner_and_tournament


class Tournament(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = runner_and_tournament.Runner("Усэйн", 10)
        self.Andrew = runner_and_tournament.Runner('Андрей', 9)
        self.Nick = runner_and_tournament.Runner("Ник", 3)
    @classmethod
    def tearDownClass(cls):
        for key, value in Tournament.all_results.items():
            print(f'{key} : {value}')

    def test_usain_and_nick(self):
        tour = runner_and_tournament.Tournament(90,self.Usain,self.Nick)
        results = tour.start()
        Tournament.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')

    def test_andrew_and_nick(self):
        tour = runner_and_tournament.Tournament(90,self.Andrew,self.Nick)
        results = tour.start()
        Tournament.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')

    def test_usain_andrew_and_nick(self):
        tour = runner_and_tournament.Tournament(90,self.Usain,self.Nick,self.Andrew)
        results = tour.start()
        Tournament.all_results.update(results)
        last_runner = max(results.keys())
        self.assertTrue(results[last_runner] == 'Ник')

if __name__ == '__main__':
    unittest.main()
