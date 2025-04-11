point_dict = {}

point_dict.update(dict.fromkeys("AEIOULNSTR", 1))
point_dict.update(dict.fromkeys("DG", 2))
point_dict.update(dict.fromkeys("BCMP", 3))
point_dict.update(dict.fromkeys("FHVWY", 4))
point_dict.update(dict.fromkeys("K", 5))
point_dict.update(dict.fromkeys("JX", 8))
point_dict.update(dict.fromkeys("QZ", 10))

point_dict.update(dict.fromkeys("АВЕИНОРСТ", 1))
point_dict.update(dict.fromkeys("ДКЛМПУ", 2))
point_dict.update(dict.fromkeys("БГЁЬЯ", 3))
point_dict.update(dict.fromkeys("ЙЫ", 4))
point_dict.update(dict.fromkeys("ЖЗХЦЧ", 5))
point_dict.update(dict.fromkeys("ШЭЮ", 8))
point_dict.update(dict.fromkeys("ФЩЪ", 10))

print(sum([point_dict.get(letter, 0) for letter in input().upper()]))