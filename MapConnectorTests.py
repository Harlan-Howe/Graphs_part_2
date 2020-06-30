import unittest
import cv2
from MapConnectorFile import MapConnector

class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertual(True, False)

    def setUp(self) -> None:
        self.connector = MapConnector()


    def test_1_display_path(self):
        edge_nums = [47,51,33,32,19,11]
        example_path = []
        for num in edge_nums:
            example_path.append(self.connector.edges[num])
        self.connector.first_city_id = 49
        self.connector.second_city_id = 89
        print("You should see a pink line connecting Helena, MT to San Antonio, TX.")
        self.connector.display_path(example_path,line_color=(128,128,255))
        cv2.waitKey()
        cv2.destroyAllWindows()

    @unittest.skip("Skipping test 2. Get test 1 working first.")
    def test_2_print_no_path(self):
        self.assertEqual("No path found.", self.connector.describe_path(None), "If path is none, we should get a message.")


    @unittest.skip("Skipping test 3. Get test 2 working first.")
    def test_3_east_west_path_description(self):
        edge_nums = [90,54,48,2]
        path = []
        for num in edge_nums:
            path.append((self.connector.edges[num]))
        self.connector.first_city_id=96
        self.connector.second_city_id= 95

        print(self.connector.describe_path(path))
        self.assertEqual("Path found:\n• Madison, WI\n• Minneapolis, MN\n• Bismarck, ND\n• Helena, MT\n• Seattle, WA\ntotal_distance = 103318.0	total_time = 3053590.0",
                         self.connector.describe_path(path), "East->West path did not match. You might have the correct cities, but different spacing/punctuation. Be sure to check the comparison.")
        # self.connector.display_path(path, line_color=(128, 128, 255))
        # cv2.waitKey()
        # cv2.destroyAllWindows()


    @unittest.skip("Skipping test 4. Get test 3 working first.")
    def test_4_west_east_path_description(self):
        edge_nums = [4,73,50,52,56,58,89,133,138,179,180]
        path = []
        for num in edge_nums:
            path.append((self.connector.edges[num]))
        self.connector.first_city_id=72
        self.connector.second_city_id= 65

        print(self.connector.describe_path(path))
        self.assertEqual("Path found:\n• Portland, OR\n• Boise, ID\n• Salt Lake City, UT\n• Cheyenne, WY\n• Lincoln, NE\n• Omaha, NE\n• Des Moines, IA\n• Chicago, IL\n• Toledo, OH\n• Cleveland, OH\n• Buffalo, NY\n• Syracuse, NY\ntotal_distance = 156894.0	total_time = 4640760.0",
                         self.connector.describe_path(path),
                         "West->East path did not match. You might have the correct cities, but different spacing/punctuation. Be sure to check the comparison.")
        # self.connector.display_path(path, line_color=(128, 128, 255))
        # cv2.waitKey()
        # cv2.destroyAllWindows()


    @unittest.skip("Skipping test 5. Get test 4 working first.")
    def test_5_zig_zag_path_description(self):

        edge_nums = [203,123,99,15,17,24]


        path = []
        for num in edge_nums:
            path.append((self.connector.edges[num]))
        self.connector.first_city_id = 58
        self.connector.second_city_id = 89

        print(self.connector.describe_path(path))
        self.assertEqual("Path found:\n• Albuquerque, NM\n• Oklahoma City, OK\n• Little Rock, AR\n• Dallas, TX\n• Fort Worth, TX\n• El Paso, TX\n• Tucson, AZ\ntotal_distance = 112256.0	total_time = 3462014.0",
                            self.connector.describe_path(path),
                            "ZigZag path did not match. You might have the correct cities, but different spacing/punctuation. Be sure to check the comparison.")
        # self.connector.display_path(path, line_color=(128, 128, 255))
        # cv2.waitKey()
        # cv2.destroyAllWindows()

    #NOTE: Tests 6-9 are optimized for DISTANCE, not TIME.


    @unittest.skip("Skipping test 6. Get test 5 working first.")
    def test_6_find_very_short_path(self):
        edge_nums = [54,55]
        expected_path = []
        for num in edge_nums:
            expected_path.append((self.connector.edges[num]))
        self.connector.first_city_id = 53 #Bismark
        self.connector.second_city_id = 79 #Pierre

        result = self.connector.perform_search()
        self.assertEqual(expected_path,result,"Extra Short path did not match expected.")


    @unittest.skip("Skipping test 7. Get test 6 working first.")
    def test_7_find_short_path(self):
        edge_nums = [131,143,142]
        expected_path = []
        for num in edge_nums:
            expected_path.append((self.connector.edges[num]))
        self.connector.first_city_id = 28 #Chicago
        self.connector.second_city_id = 81 #Memphis

        result = self.connector.perform_search()
        self.assertEqual(expected_path,result,"Short path did not match expected.")


    @unittest.skip("Skipping test 8. Get test 7 working first.")
    def test_8_find_medium_path(self):
        edge_nums = [3,73,35,36,31]
        expected_path = []
        for num in edge_nums:
            expected_path.append((self.connector.edges[num]))
        self.connector.first_city_id = 95 #Seattle
        self.connector.second_city_id = 4 #Tuscon

        result = self.connector.perform_search()
        self.assertEqual(expected_path,result,"Medium path did not match expected.")


    @unittest.skip("Skipping test 9. Get test 8 working first.")
    def test_9_find_long_path(self):
        edge_nums = [121,118,151,156,161,175,174,189,186,188,193]
        expected_path = []
        for num in edge_nums:
            expected_path.append((self.connector.edges[num]))
        self.connector.first_city_id = 21 #Miami
        self.connector.second_city_id = 93 #Montpellier

        result = self.connector.perform_search()
        self.assertEqual(expected_path,result,"Long path did not match expected.")