from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import cross_validate
import pickle

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
restecg_elemnts = driver.find_elements_by_class_name("patient-restecg")

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
    row.append(int(restecg_elemnts[i].text))
    row.append(int(thalach_elemnts[i].text))
    row.append(int(exang_elemnts[i].text))
    row.append(float(oldpeak_elemnts[i].text))
    row.append(int(slope_elemnts[i].text))
    row.append(int(ca_elemnts[i].text))
    row.append(int(thal_elemnts[i].text))
    row.append(int(target_elemnts[i].text))

    table.append(row)

table_headers = ["age", "sex", "cp", "trestbps", "chol", 
                "fbs", "restecg", "thalach", "exang", "oldpeak", 
                "slope", "ca", "thal", "target"]

df = pd.DataFrame(table, columns=table_headers)
y = df["target"] #teraz to słownik target to klasyfikacja
df = df.drop(["target"], axis=1) #usuwanie tego nie chcemy w modelu
X = df



#trenowanie
classifier = KNN(n_neighbors=3) #trzy wartosci - grupy


# #walidacja - nie najlepszy sposób, ale sprawdza się przy małym zbiorze danych
# result = cross_validate(classifier, X, y, cv=3) #cv ile razy chcemy walidować, standard to 10 razy
# #accuracy jest praktycznie bezużyteczną metodą/wskaźnikiem w ML; ale najłatwiejsdza w zrozumeiniu
# # w rzecyzwistosci przejmujemy się precisios recole... ?
# print(result["test_score"])



classifier.fit(X, y)

#zapisac model po wytrenowania
with open("knn_heart_disease.pkl", 'wb') as file:
    pickle.dump(classifier, file)

