acLuminanceTable = {'0/0': (4, '1010'), '0/1': (2, '00'), '0/2': (2, '01'), '0/3': (3, '100'), '0/4': (4, '1011'), '0/5': (5, '11010'), '0/6': (7, '1111000'), '0/7': (8, '11111000'), '0/8': (10, '1111110110'), '0/9': (16, '1111111110000010'), '0/A': (16, '1111111110000011'), '1/1': (4, '1100'), '1/2': (5, '11011'), '1/3': (7, '1111001'), '1/4': (9, '111110110'), '1/5': (11, '11111110110'), '1/6': (16, '1111111110000100'), '1/7': (16, '1111111110000101'), '1/8': (16, '1111111110000110'), '1/9': (16, '1111111110000111'), '1/A': (16, '1111111110001000'), '2/1': (5, '11100'), '2/2': (8, '11111001'), '2/3': (10, '1111110111'), '2/4': (12, '111111110100'), '2/5': (16, '1111111110001001'), '2/6': (16, '1111111110001010'), '2/7': (16, '1111111110001011'), '2/8': (16, '1111111110001100'), '2/9': (16, '1111111110001101'), '2/A': (16, '1111111110001110'), '3/1': (6, '111010'), '3/2': (9, '111110111'), '3/3': (12, '111111110101'), '3/4': (16, '1111111110001111'), '3/5': (16, '1111111110010000'), '3/6': (16, '1111111110010001'), '3/7': (16, '1111111110010010'), '3/8': (16, '1111111110010011'), '3/9': (16, '1111111110010100'), '3/A': (16, '1111111110010101'), '4/1': (6, '111011'), '4/2': (10, '1111111000'), '4/3': (16, '1111111110010110'), '4/4': (16, '1111111110010111'), '4/5': (16, '1111111110011000'), '4/6': (16, '1111111110011001'), '4/7': (16, '1111111110011010'), '4/8': (16, '1111111110011011'), '4/9': (16, '1111111110011100'), '4/A': (16, '1111111110011101'), '5/1': (7, '1111010'), '5/2': (11, '11111110111'), '5/3': (16, '1111111110011110'), '5/4': (16, '1111111110011111'), '5/5': (16, '1111111110100000'), '5/6': (16, '1111111110100001'), '5/7': (16, '1111111110100010'), '5/8': (16, '1111111110100011'), '5/9': (16, '1111111110100100'), '5/A': (16, '1111111110100101'), '6/1': (7, '1111011'), '6/2': (12, '111111110110'), '6/3': (16, '1111111110100110'), '6/4': (16, '1111111110100111'), '6/5': (16, '1111111110101000'), '6/6': (16, '1111111110101001'), '6/7': (16, '1111111110101010'), '6/8': (16, '1111111110101011'), '6/9': (16, '1111111110101100'), '6/A': (16, '1111111110101101'), '7/1': (8, '11111010'), '7/2': (12, '111111110111'), '7/3': (16, '1111111110101110'), '7/4': (16, '1111111110101111'), '7/5': (16, '1111111110110000'), '7/6': (16, '1111111110110001'), '7/7': (16, '1111111110110010'), '7/8': (16, '1111111110110011'), '7/9': (16, '1111111110110100'), '7/A': (16, '1111111110110101'), '8/1': (9, '111111000'), '8/2': (15, '111111111000000'), '8/3': (16, '1111111110110110'), '8/4': (16, '1111111110110111'), '8/5': (16, '1111111110111000'), '8/6': (16, '1111111110111001'), '8/7': (16, '1111111110111010'), '8/8': (16, '1111111110111011'), '8/9': (16, '1111111110111100'), '8/A': (16, '1111111110111101'), '9/1': (9, '111111001'), '9/2': (16, '1111111110111110'), '9/3': (16, '1111111110111111'), '9/4': (16, '1111111111000000'), '9/5': (16, '1111111111000001'), '9/6': (16, '1111111111000010'), '9/7': (16, '1111111111000011'), '9/8': (16, '1111111111000100'), '9/9': (16, '1111111111000101'), '9/A': (16, '1111111111000110'), 'A/1': (9, '111111010'), 'A/2': (16, '1111111111000111'), 'A/3': (16, '1111111111001000'), 'A/4': (16, '1111111111001001'), 'A/5': (16, '1111111111001010'), 'A/6': (16, '1111111111001011'), 'A/7': (16, '1111111111001100'), 'A/8': (16, '1111111111001101'), 'A/9': (16, '1111111111001110'), 'A/A': (16, '1111111111001111'), 'B/1': (10, '1111111001'), 'B/2': (16, '1111111111010000'), 'B/3': (16, '1111111111010001'), 'B/4': (16, '1111111111010010'), 'B/5': (16, '1111111111010011'), 'B/6': (16, '1111111111010100'), 'B/7': (16, '1111111111010101'), 'B/8': (16, '1111111111010110'), 'B/9': (16, '1111111111010111'), 'B/A': (16, '1111111111011000'), 'C/1': (10, '1111111010'), 'C/2': (16, '1111111111011001'), 'C/3': (16, '1111111111011010'), 'C/4': (16, '1111111111011011'), 'C/5': (16, '1111111111011100'), 'C/6': (16, '1111111111011101'), 'C/7': (16, '1111111111011110'), 'C/8': (16, '1111111111011111'), 'C/9': (16, '1111111111100000'), 'C/A': (16, '1111111111100001'), 'D/1': (11, '11111111000'), 'D/2': (16, '1111111111100010'), 'D/3': (16, '1111111111100011'), 'D/4': (16, '1111111111100100'), 'D/5': (16, '1111111111100101'), 'D/6': (16, '1111111111100110'), 'D/7': (16, '1111111111100111'), 'D/8': (16, '1111111111101000'), 'D/9': (16, '1111111111101001'), 'D/A': (16, '1111111111101010'), 'E/1': (16, '1111111111101011'), 'E/2': (16, '1111111111101100'), 'E/3': (16, '1111111111101101'), 'E/4': (16, '1111111111101110'), 'E/5': (16, '1111111111101111'), 'E/6': (16, '1111111111110000'), 'E/7': (16, '1111111111110001'), 'E/8': (16, '1111111111110010'), 'E/9': (16, '1111111111110011'), 'E/A': (16, '1111111111110100'), 'F/0': (11, '11111111001'), 'F/1': (16, '1111111111110101'), 'F/2': (16, '1111111111110110'), 'F/3': (16, '1111111111110111'), 'F/4': (16, '1111111111111000'), 'F/5': (16, '1111111111111001'), 'F/6': (16, '1111111111111010'), 'F/7': (16, '1111111111111011'), 'F/8': (16, '1111111111111100'), 'F/9': (16, '1111111111111101'), 'F/A': (16, '1111111111111110')}
acChrominanceTable = {'0/0': (2, '00'), '0/1': (2, '01'), '0/2': (3, '100'), '0/3': (4, '1010'), '0/4': (5, '11000'), '0/5': (5, '11001'), '0/6': (6, '111000'), '0/7': (7, '1111000'), '0/8': (9, '111110100'), '0/9': (10, '1111110110'), '0/A': (12, '111111110100'), '1/1': (4, '1011'), '1/2': (6, '111001'), '1/3': (8, '11110110'), '1/4': (9, '111110101'), '1/5': (11, '11111110110'), '1/6': (12, '111111110101'), '1/7': (16, '1111111110001000'), '1/8': (16, '1111111110001001'), '1/9': (16, '1111111110001010'), '1/A': (16, '1111111110001011'), '2/1': (5, '11010'), '2/2': (8, '11110111'), '2/3': (10, '1111110111'), '2/4': (12, '111111110110'), '2/5': (15, '111111111000010'), '2/6': (16, '1111111110001100'), '2/7': (16, '1111111110001101'), '2/8': (16, '1111111110001110'), '2/9': (16, '1111111110001111'), '2/A': (16, '1111111110010000'), '3/1': (5, '11011'), '3/2': (8, '11111000'), '3/3': (10, '1111111000'), '3/4': (12, '111111110111'), '3/5': (16, '1111111110010001'), '3/6': (16, '1111111110010010'), '3/7': (16, '1111111110010011'), '3/8': (16, '1111111110010100'), '3/9': (16, '1111111110010101'), '3/A': (16, '1111111110010110'), '4/1': (6, '111010'), '4/2': (9, '111110110'), '4/3': (16, '1111111110010111'), '4/4': (16, '1111111110011000'), '4/5': (16, '1111111110011001'), '4/6': (16, '1111111110011010'), '4/7': (16, '1111111110011011'), '4/8': (16, '1111111110011100'), '4/9': (16, '1111111110011101'), '4/A': (16, '1111111110011110'), '5/1': (6, '111011'), '5/2': (10, '1111111001'), '5/3': (16, '1111111110011111'), '5/4': (16, '1111111110100000'), '5/5': (16, '1111111110100001'), '5/6': (16, '1111111110100010'), '5/7': (16, '1111111110100011'), '5/8': (16, '1111111110100100'), '5/9': (16, '1111111110100101'), '5/A': (16, '1111111110100110'), '6/1': (7, '1111001'), '6/2': (11, '11111110111'), '6/3': (16, '1111111110100111'), '6/4': (16, '1111111110101000'), '6/5': (16, '1111111110101001'), '6/6': (16, '1111111110101010'), '6/7': (16, '1111111110101011'), '6/8': (16, '1111111110101100'), '6/9': (16, '1111111110101101'), '6/A': (16, '1111111110101110'), '7/1': (7, '1111010'), '7/2': (11, '11111111000'), '7/3': (16, '1111111110101111'), '7/4': (16, '1111111110110000'), '7/5': (16, '1111111110110001'), '7/6': (16, '1111111110110010'), '7/7': (16, '1111111110110011'), '7/8': (16, '1111111110110100'), '7/9': (16, '1111111110110101'), '7/A': (16, '1111111110110110'), '8/1': (8, '11111001'), '8/2': (16, '1111111110110111'), '8/3': (16, '1111111110111000'), '8/4': (16, '1111111110111001'), '8/5': (16, '1111111110111010'), '8/6': (16, '1111111110111011'), '8/7': (16, '1111111110111100'), '8/8': (16, '1111111110111101'), '8/9': (16, '1111111110111110'), '8/A': (16, '1111111110111111'), '9/1': (9, '111110111'), '9/2': (16, '1111111111000000'), '9/3': (16, '1111111111000001'), '9/4': (16, '1111111111000010'), '9/5': (16, '1111111111000011'), '9/6': (16, '1111111111000100'), '9/7': (16, '1111111111000101'), '9/8': (16, '1111111111000110'), '9/9': (16, '1111111111000111'), '9/A': (16, '1111111111001000'), 'A/1': (9, '111111000'), 'A/2': (16, '1111111111001001'), 'A/3': (16, '1111111111001010'), 'A/4': (16, '1111111111001011'), 'A/5': (16, '1111111111001100'), 'A/6': (16, '1111111111001101'), 'A/7': (16, '1111111111001110'), 'A/8': (16, '1111111111001111'), 'A/9': (16, '1111111111010000'), 'A/A': (16, '1111111111010001'), 'B/1': (9, '111111001'), 'B/2': (16, '1111111111010010'), 'B/3': (16, '1111111111010011'), 'B/4': (16, '1111111111010100'), 'B/5': (16, '1111111111010101'), 'B/6': (16, '1111111111010110'), 'B/7': (16, '1111111111010111'), 'B/8': (16, '1111111111011000'), 'B/9': (16, '1111111111011001'), 'B/A': (16, '1111111111011010'), 'C/1': (9, '111111010'), 'C/2': (16, '1111111111011011'), 'C/3': (16, '1111111111011100'), 'C/4': (16, '1111111111011101'), 'C/5': (16, '1111111111011110'), 'C/6': (16, '1111111111011111'), 'C/7': (16, '1111111111100000'), 'C/8': (16, '1111111111100001'), 'C/9': (16, '1111111111100010'), 'C/A': (16, '1111111111100011'), 'D/1': (11, '11111111001'), 'D/2': (16, '1111111111100100'), 'D/3': (16, '1111111111100101'), 'D/4': (16, '1111111111100110'), 'D/5': (16, '1111111111100111'), 'D/6': (16, '1111111111101000'), 'D/7': (16, '1111111111101001'), 'D/8': (16, '1111111111101010'), 'D/9': (16, '1111111111101011'), 'D/A': (16, '1111111111101100'), 'E/1': (14, '11111111100000'), 'E/2': (16, '1111111111101101'), 'E/3': (16, '1111111111101110'), 'E/4': (16, '1111111111101111'), 'E/5': (16, '1111111111110000'), 'E/6': (16, '1111111111110001'), 'E/7': (16, '1111111111110010'), 'E/8': (16, '1111111111110011'), 'E/9': (16, '1111111111110100'), 'E/A': (16, '1111111111110101'), 'F/0': (10, '1111111010'), 'F/1': (15, '111111111000011'), 'F/2': (16, '1111111111110110'), 'F/3': (16, '1111111111110111'), 'F/4': (16, '1111111111111000'), 'F/5': (16, '1111111111111001'), 'F/6': (16, '1111111111111010'), 'F/7': (16, '1111111111111011'), 'F/8': (16, '1111111111111100'), 'F/9': (16, '1111111111111101'), 'F/A': (16, '1111111111111110')}
