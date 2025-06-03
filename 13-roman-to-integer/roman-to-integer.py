class Solution:
    def romanToInt(self, s):
        ret_val = 0

        sym_to_val_map = {}
        sym_to_val_map['I'] = 1
        sym_to_val_map['V'] = 5
        sym_to_val_map['X'] = 10
        sym_to_val_map['L'] = 50
        sym_to_val_map['C'] = 100
        sym_to_val_map['D'] = 500
        sym_to_val_map['M'] = 1000

        i = 0
        while (i < len(s)):
            c = s[i]
            c2 = s[i:i+2]

            if (c2 == 'IV'):
                ret_val += 4
                i += 2
            elif (c2 == 'IX'):
                ret_val += 9
                i += 2
            elif (c2 == 'XL'):
                ret_val += 40
                i += 2
            elif (c2 == 'XC'):
                ret_val += 90
                i += 2
            elif (c2 == 'CD'):
                ret_val += 400
                i += 2
            elif (c2 == 'CM'):
                ret_val += 900
                i += 2
            else:
                ret_val += sym_to_val_map[c]
                i += 1
            
        return ret_val