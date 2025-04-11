Anton=int(input())
Boris=int(input())
Viktor=int(input())# put your python code here
if Anton>Boris:
    if Anton>Viktor:
        print("Антон старше всех")
    if Anton==Viktor:
        print("Антон и Виктор старше всех")

if Boris>Viktor:
    if Boris>Anton:
        print("Борис старше всех")
    if Boris==Anton:
        print("Антон и Борис старше всех")
        
if Viktor>Anton:
    if Viktor>Boris:
        print("Виктор старше всех")
    if Viktor==Boris:
        print("Борис и Виктор старше всех")
