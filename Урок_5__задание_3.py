#coding=windows-1251
summa=int(input("����������� ����� ���������� "))
mike=int(input("� ������ �������� - "))
ivan=int(input("� ����� �������� - "))

if(mike>=summa)and(ivan>=summa):
 print("2")
elif(mike>=summa)and(ivan<summa):
  print("Mike")
elif(mike<summa)and(ivan>=summa):
  print("Ivan")
elif(mike<summa)and(ivan<summa)and((mike+ivan)>=summa):
  print("1")
elif(mike<summa)and(ivan<summa)and((mike+ivan)<summa):
  print("0")

  
