from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from webdriver_manager.chrome import ChromeDriverManager


ops = Options()
ops.add_argument("--headless") # żeby interfejsu nie otwierało
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=ops)

driver.get('https://b2gdevs.github.io/MLIntro/heart-disease.html')
# driver.get('https://www.exploit-db.com/exploits/50608')

# liczba elemntów jest taka sama, bo ROW
age_elemnts = driver.find_elements_by_class_name("patient-age")
sex_elemnts = driver.find_elements_by_class_name("patient-sex")
cp_elemnts = driver.find_elements_by_class_name("patient-cp")
trestbps_elemnts = driver.find_elements_by_class_name("patient-trestbps")
chol_elemnts = driver.find_elements_by_class_name("patient-chol")
fbs_elemnts = driver.find_elements_by_class_name("patient-fbs")
thalach_elemnts = driver.find_elements_by_class_name("patient-thalach")
exang_elemnts = driver.find_elements_by_class_name("patient-exang")
oldpeak_elemnts = driver.find_elements_by_class_name("patient-oldpeak")
slope_elemnts = driver.find_elements_by_class_name("patient-slope")
ca_elemnts = driver.find_elements_by_class_name("patient-ca")
thal_elemnts = driver.find_elements_by_class_name("patient-thal")
target_elemnts = driver.find_elements_by_class_name("patient-target")

table = []

for i in range(len(age_elemnts)-1): #ostatni wiersz zawiera undefined data - czyszczenie
    row = []

    row.append(int(age_elemnts[i].text))
    row.append(int(sex_elemnts[i].text))
    row.append(int(cp_elemnts[i].text))
    row.append(int(trestbps_elemnts[i].text))
    row.append(int(chol_elemnts[i].text))
    row.append(int(fbs_elemnts[i].text))
    row.append(int(thalach_elemnts[i].text))
    row.append(int(exang_elemnts[i].text))
    row.append(float(oldpeak_elemnts[i].text))
    row.append(int(slope_elemnts[i].text))
    row.append(int(ca_elemnts[i].text))
    row.append(int(thal_elemnts[i].text))
    row.append(int(target_elemnts[i].text))

    table.append(row)

print(table)