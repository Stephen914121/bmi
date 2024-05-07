# if練習-BMI計算程式
# 寫一個BMI 計算程式，請看此網站：http://depart.femh.org.tw/dietary/3OPD/BMI.htm
# 讓使用者輸入身高體重，計算出並印出使用者的BMI，然後依照以上網站的表格印出是過輕、正常、過重、輕度肥胖、中度肥胖、還是重度肥胖
# BMI值計算公式:    BMI = 體重(公斤) / 身高2(公尺2)

height = input('請輸入身高:')
weight = input('請輸入體重:')
height = float(height) / 100
weight = float(weight)
bmi = weight / (height * height)

if bmi < 18.5:
    print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('正常範圍')
elif bmi >= 24 and bmi < 27: 
    print('過重')
elif bmi >= 27 and bmi < 30:
    print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('中度肥胖')
else:
	print('嚴重肥胖')