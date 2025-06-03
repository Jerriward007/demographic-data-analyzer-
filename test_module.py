import unittest
import demographic_data_analyzer


class DemographicAnalyzerTestCase(unittest.TestCase):
    def test_results(self):
        result = demographic_data_analyzer.calculate_demographic_data()

        self.assertAlmostEqual(result['average_age_men'], 39.4, places=1)
        self.assertAlmostEqual(result['percentage_bachelors'], 16.4, places=1)
        self.assertAlmostEqual(result['higher_education_rich'], 46.5, places=1)
        self.assertAlmostEqual(result['lower_education_rich'], 17.4, places=1)
        self.assertEqual(result['min_work_hours'], 1)
        self.assertAlmostEqual(result['rich_percentage'], 10.0, places=1)
        self.assertEqual(result['highest_earning_country'], 'Iran')
        self.assertAlmostEqual(result['highest_earning_country_percentage'], 41.9, places=1)
        self.assertEqual(result['top_IN_occupation'], 'Prof-specialty')


if __name__ == "__main__":
    unittest.main()
