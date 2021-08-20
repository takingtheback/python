'''
3 학생의 이름, 번호, 국어, 영어, 수학 점수를 입력받아서, 각 학생의 총점, 평균을 계산하여 결과를 출력

이름 번호 국어 영어 수학 총점 평균
aaa    1 65  98  89  234  78.9

'''
print(' 첫번째 학생의 이름, 번호, 국어, 영어, 수학 점수를 순서대로 입력해주세요.')
a = []
name = input('이름 : ')
a.append(name)
no = input('번호 : ')
a.append(no)
kr = int(input('국어 : '))
a.append(kr)
en = int(input('영어 : '))
a.append(en)
ma = int(input('수학 : '))
a.append(ma)

print(' 두번째 학생의 이름, 번호, 국어, 영어, 수학 점수를 순서대로 입력해주세요.')
b = []
name = input('이름 : ')
b.append(name)
no = input('번호 : ')
b.append(no)
kr = int(input('국어 : '))
b.append(kr)
en = int(input('영어 : '))
b.append(en)
ma = int(input('수학 : '))
b.append(ma)

print(' 첫번째 학생의 이름, 번호, 국어, 영어, 수학 점수를 순서대로 입력해주세요.')
c = []
name = input('이름 : ')
c.append(name)
no = input('번호 : ')
c.append(no)
kr = int(input('국어 : '))
c.append(kr)
en = int(input('영어 : '))
c.append(en)
ma = int(input('수학 : '))
c.append(ma)

totalA = int(a[2] + a[3] + a[4])
averageA = round(int(totalA)/3, 1)
totalB = int(b[2] + b[3] + b[4])
averageB = round(int(totalB)/3, 1)
totalC = int(c[2] + c[3] + c[4])
averageC = round(int(totalC)/3, 1)

print('이름   번호  국어  영어  수학  총점   평균')
print(a[0], '   ', a[1],'  ', a[2], ' ', a[3], ' ', a[4], ' ', totalA, ' ', averageA)
print(b[0], '   ', b[1],'  ', b[2], ' ', b[3], ' ', b[4], ' ', totalB, ' ', averageB)
print(c[0], '   ', c[1],'  ', c[2], ' ', c[3], ' ', c[4], ' ', totalC, ' ', averageC)