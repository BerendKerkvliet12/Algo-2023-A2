import typing
import unittest
import numpy as np

from divconq import IntelDevice


class TestIntelDevice(unittest.TestCase):

    def test_fill_coordinate_to_loc_edge_cases_empty(self):
        no_loc = [] 
        ob = IntelDevice(1, 1, no_loc, [], 8)
        ob.fill_coordinate_to_loc()
        self.assertTrue(len(ob.coordinate_to_location) == 0)
    
    def test_fill_coordinate_to_loc_edge_cases_single_loc(self):
        single_loc = ["1010100 1101101 1110001 1101100 1101101 1110110"]  # Leiden
        ob = IntelDevice(1, 1, single_loc, [], 8)
        ob.fill_coordinate_to_loc()
        self.assertTrue(ob.coordinate_to_location[(0, 0)] == "Leiden")

    def test_fill_coordinate_to_loc_edge_cases_grid_overflow(self):
        enc_locations = [
            #set 1
            "1011010 1110111 1111100 1111100 1101101 1111010 1101100 1101001 1110101",  # Rotterdam
            "1001100 1101101 1110100 1101110 1111100",  # Delft
            "1010100 1101101 1110001 1101100 1101101 1110110",  # Leiden
            "1001010 1101101 1111010 1110100 1110001 1110010 1110110",  # Berlijn
            "1011000 1110111 1111010 1111100 1110111",  # Porto
            "1010011 1110001 1101101 1111110",  # Kiev
            #set 2
            "1011010 1110111 1111100 1111100 1101101 1111010 1101100 1101001 1110101",  # Rotterdam
            "1001100 1101101 1110100 1101110 1111100",  # Delft
            "1010100 1101101 1110001 1101100 1101101 1110110",  # Leiden
            "1001010 1101101 1111010 1110100 1110001 1110010 1110110",  # Berlijn
            "1011000 1110111 1111010 1111100 1110111",  # Porto
            "1010011 1110001 1101101 1111110",  # Kiev
            #set 3 in order to overflow the grid
            "1011010 1110111 1111100 1111100 1101101 1111010 1101100 1101001 1110101",  # Rotterdam
            "1001100 1101101 1110100 1101110 1111100",  # Delft
            "1010100 1101101 1110001 1101100 1101101 1110110",  # Leiden
            "1001010 1101101 1111010 1110100 1110001 1110010 1110110",  # Berlijn
            "1011000 1110111 1111010 1111100 1110111",  # Porto
            "1010011 1110001 1101101 1111110",  # Kiev
            #set 4
            "1011010 1110111 1111100 1111100 1101101 1111010 1101100 1101001 1110101",  # Rotterdam
            "1001100 1101101 1110100 1101110 1111100",  # Delft
            "1010100 1101101 1110001 1101100 1101101 1110110",  # Leiden
            "1001010 1101101 1111010 1110100 1110001 1110010 1110110",  # Berlijn
            "1011000 1110111 1111010 1111100 1110111",  # Porto
            "1010011 1110001 1101101 1111110",  # Kiev
        ] 

        ob = IntelDevice(3, 2, enc_locations, [], 8)
        ob.fill_coordinate_to_loc()

        solution = {
            (0, 0): "Rotterdam",
            (0, 1): "Delft",
            (0, 2): "Leiden",
            (1, 0): "Berlijn",
            (1, 1): "Porto",
            (1, 2): "Kiev",
        }

        for key, value in solution.items():
            self.assertTrue(ob.coordinate_to_location[key] == value)
        self.assertTrue(len(ob.coordinate_to_location) == len(solution))



# We couldn't find a way to make separate unit test codes so we tried to adjust the other tests to find the errors in our code. However, most of the unittests were too comparable to the actual unittest so we didn't include them.








#################################################################################

    
    # def test_encode_message(self):
    #         # without caesar shift
    #         ob = IntelDevice(3,5,[],[],0)
    #         answers =[
    #             "1000011 1101100 1100001 1110011 1110011 1101001 1100110 1101001 1100101 1100100 100000 1101001 1101110 1100110 1101111 1110010 1101101 1100001 1110100 1101001 1101111 1101110",
    #             "1001100 1100101 1101001 1100100 1100101 1101110 100000 1010101 1101110 1101001 1110110 1100101 1110010 1110011 1101001 1110100 1111001",
    #             "1000001 1101100 1100111 1101111 1110010 1101001 1110100 1101000 1101101 1110011 100000 1100001 1101110 1100100 100000 1000100 1100001 1110100 1100001 100000 1010011 1110100 1110010 1110101 1100011 1110100 1110101 1110010 1100101 1110011"
    #         ] 
    #         queries = ["Classified information", "Leiden University", "Algorithms and Data Structures"]
            
    #         for query, answer in zip(queries, answers):
    #             self.assertEqual(ob.encode_message(query),answer)
    
    #         # with caesar shift 8
    #         ob = IntelDevice(3,5,[],[],8)
    #         answers =[
    #             "1001011 1110100 1101001 1111011 1111011 1110001 1101110 1110001 1101101 1101100 101000 1110001 1110110 1101110 1110111 1111010 1110101 1101001 1111100 1110001 1110111 1110110",
    #             "1010100 1101101 1110001 1101100 1101101 1110110 101000 1011101 1110110 1110001 1111110 1101101 1111010 1111011 1110001 1111100 10000001",
    #             "1001001 1110100 1101111 1110111 1111010 1110001 1111100 1110000 1110101 1111011 101000 1101001 1110110 1101100 101000 1001100 1101001 1111100 1101001 101000 1011011 1111100 1111010 1111101 1101011 1111100 1111101 1111010 1101101 1111011"
    #         ] 
    #         queries = ["Classified information", "Leiden University", "Algorithms and Data Structures"]
            
    #         for query, answer in zip(queries, answers):
    #             self.assertEqual(ob.encode_message(query),answer)
    
    
    # def test_encode_message_2(self):
    #         # without caesar shift
    #         ob = IntelDevice(3,5,[],[],0)
    #         answers =[
    #             "1000011 1101100 1100001 1110011 1110011 1101001 1100110 1101001 1100101 1100100 100000 1101001 1101110 1100110 1101111 1110010 1101101 1100001 1110100 1101001 1101111 1101110",
    #             "1001100 1100101 1101001 1100100 1100101 1101110 100000 1010101 1101110 1101001 1110110 1100101 1110010 1110011 1101001 1110100 1111001",
    #             "1000001 1101100 1100111 1101111 1110010 1101001 1110100 1101000 1101101 1110011 100000 1100001 1101110 1100100 100000 1000100 1100001 1110100 1100001 100000 1010011 1110100 1110010 1110101 1100011 1110100 1110101 1110010 1100101 1110011"
    #         ] 
    #         queries = ["Classified information", "Leiden University", "Algorithms and Data Structures"]
            
    #         for query, answer in zip(queries, answers):
    #             self.assertEqual(ob.encode_message(query),answer)
    
    #         # with caesar shift 8
    #         ob = IntelDevice(4,5,[],[],9)
    #         answers =[
    #             "100102131211 1110100 1101001 1111011 1111011 1110001 1101110 1110001 1101101 1101100 101000 1110001 1110110 1101110 1110111 1111010 1110101 1101001 1111100 1110001 1110111 1110110",
    #             "1010100 1101101 1110001 1101100 1101101 1110110 101000 1011101 1110110 1110001 1111110 1101101 1111010 1111011 1110001 1111100 10000001",
    #             "1001001 1110100 1101111 1110111 1111010 1110001 1111100 1110000 1110101 1111011 101000 1101001 1110110 1101100 101000 1001100 1101001 1111100 1101001 101000 1011011 1111100 1111010 1111101 1101011 1111100 1111101 1111010 1101101 1111011"
    #         ] 
    #         queries = ["Classified1 information", "Leiden University", "Algorithms and Data Structures"]
            
    #         for query, answer in zip(queries, answers):
    #             self.assertEqual(ob.encode_message(query),answer)
    