# -*- coding: utf-8 -*-
"""Копия блокнота "Fork of ds-praktikum-3-modul-2-amaliyot"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N7ipaRxdf-rDDf3Q7NG9mO8MJlvTMDPc
"""

# IMPORTANT: RUN THIS CELL IN ORDER TO IMPORT YOUR KAGGLE DATA SOURCES,
# THEN FEEL FREE TO DELETE THIS CELL.
# NOTE: THIS NOTEBOOK ENVIRONMENT DIFFERS FROM KAGGLE'S PYTHON
# ENVIRONMENT SO THERE MAY BE MISSING LIBRARIES USED BY YOUR
# NOTEBOOK.
import kagglehub
dansbecker_melbourne_housing_snapshot_path = kagglehub.dataset_download('dansbecker/melbourne-housing-snapshot')

print('Data source import complete.')

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

"""## Avvalgi amaliyotda `GitHub`ga yuklangan `melb_data.csv` faylni `df` ga chaqirib oling"""

#Javobingizni shu yerga yozing
df=pd.read_csv("https://github.com/Xasan17/lessons_python/blob/main/melb_data.csv?raw=true")
df.head()

# Mening javobim
df = pd.read_csv("https://github.com/anvarnarz/praktikum_datasets/blob/main/melb_data.csv?raw=true")
df.head()

"""Yuqoridagi Dataframe Melburn shahri uchun sotuvdagi uylar haqida m'lumotlarni jamlagan.

Quyida jadvalning ba'zi sutunlari tarjimasi berilgan (qolganini o'zingiz Google yordamida tarjima qilishingiz mumkin):
- `Room` - xonalar soni
- `Type` - uyning turi (h - villa/kottej/hovli; u - kvartira; t - shahardagi hovli)
- `Price` - narx
- `Bathroom` - tualet-vanna
- `Landsize` - yerning maydoni (hovli uchun)
- `BuildingArea` - Bino qurilgan yerning maydoni
- `YearBuilt` - qurilgan yili
- `Lattitude` va `Longitude` - GPS kordinatalar
- `Regionname` - Region

# 🔺 DIQQAT!
#### **Agar alohida aytilmagan bo'lsa, `df`ga kiritilgan o'zgartirishlarni saqlamang (`inplace=False`)**

## 1-VAZIFA. `df` dagi barcha ustunlardagi`NaN` qiymatlar sonini chiqaring
"""

#Javobingizni shu yerga yozing
df.isnull().sum()

"""## 2-VAZIFA. `df` barcha `NaN` qiymatlarni 0 bilan almashtiring"""

#Javobingizni shu yerga yozing
df.fillna(0)

"""## 3-VAZIFA. Quyidagi 2 ustun uchun o'rta qiymatlarni hisoblang:
- BuildingArea
- YearBuilt (**butun son qaytishi kerak**)
"""

#Javobingizni shu yerga yozing
print(df['BuildingArea'].mean())
print(int(df['YearBuilt'].mean()))

"""**To'g'ri javob:**"""

print(df['BuildingArea'].mean())
print(int(df['YearBuilt'].mean()))

"""## 4-VAZIFA: `BuildingArea` va `YearBuilt` ustunlaridagi `NaN` qiymatlarni shu sutun uchun o'rta qiymatlar bilan almashtiring
**DIQQAT!** `YearBuilt` ustuni qiymatlari butun son bo'lishi kerak
"""

#Javobingizni shu yerga yozing
df.fillna({'BuildingArea': df['BuildingArea'].mean(), 'YearBuilt': int(df['YearBuilt'].mean())})

"""**To'g'ri javob:**"""

df.fillna({'BuildingArea':df['BuildingArea'].mean(), 'YearBuilt':int(df['YearBuilt'].mean())})

"""## 5-VAZIFA. `.groupby()`
Ustun uchun o'rta qiymat har doim ham aniq bo'lavermaydi. Keling avval `YearBuilt` ustuni uchun aniqroq qiymat topishga harakat qilamiz.

Buning uchun `Regionname` ustuni qiymatlaridan foydalanishimiz mumkin, ya'ni bir Regiondagi binolar tahminan bir hil yillarda qurilgan deb tahmin qilsak bo'ladi.

### 5.1 `.groupby()` yordamida `df` qiymatlarini `Regionname` ustuni bo'yicha guruhlang va `YaerBuilt` ustuni uchun o'rta qiymatni hisoblang.
"""

#Javobingizni shu yerga yozing
df.groupby('Regionname').YearBuilt.mean().astype(int)

"""**To'g'ri javob:**"""

df.groupby(['Regionname']).YearBuilt.mean().astype(int)

"""### 5.2. `df` `YearBuilt` ustunidagi `NaN` qiymatlarni yuqoridagi qiymatlar bilan almashtiring.
`df[df.Regionname='Eastern Metropolitan']=...`

Har bir `Regionname` uchun qiymatlarni bittalab kiritmaslik uchun for siklidan foydalanishingiz mumkin.
"""

#Javobingizni shu yerga yozing
group=df.groupby(['Regionname']).YearBuilt.mean().astype(int)
for idx in group.index:
  df[df.Regionname==idx]=df[df.Regionname==idx].fillna({'YearBuilt':group[idx]})
df[df.Regionname==idx]

"""**To'g'ri javob**"""

groups = df.groupby(['Regionname']).YearBuilt.mean() # Bu Series obyekti
for idx in groups.index:
   df[df.Regionname==idx] = df[df.Regionname==idx].fillna({'YearBuilt':groups[idx]})

"""### `YearBuilt` uchun yana ham aniqroq o'rta qiymat hisoblashning qanday yo'lini taklif qilgan bo'lar edingiz?

## 6-VAZIFA. `BuildingArea` ustunidagi `NaN` qiymatlarni to'ldiramiz
`BuildingArea` bino qurilgan yerning maydonini bildiradi. Bu qiymatlarni tahmin qilish uchun qaysi ustun qiymatlaridan foydalanish to'g'ri deb hisoblaysiz?
"""

df.head()

"""### 6.1 `df`ni xonalar soni bo'yicha o'rta qiymat olib ko'ring"""

#Javobingizni shu yerga yozing
df.groupby('Rooms').BuildingArea.mean()
df[df.Rooms==10]

"""### 6.2 Xonalar va uy turi bo'yicha o'rta qiymatni olib ko'ring."""

#Javobingizni shu yerga yozing
df.groupby(['Rooms', 'Type'])['BuildingArea'].mean()

"""### 6.3 Ahamiyat bering, 10 xonalik uylar uchun o'rta qiymat chiqmayapti. Bu nimadan dalolat beradi? Jami 10 xonalik uylar nechta? Ular bilan qanday yo'l tutishni maslahat berasiz?"""

#Javobingizni shu yerga yozing
df.loc[df.Rooms==10, 'BuildingArea']=df[df.Rooms==8].BuildingArea.max()
df.loc[df.Rooms==10]

"""### 6.4 `BuildingArea` ustunidagi mavjud `NaN` qiymatlarni o'zingiz to'g'ri deb bilgan usul bilan to'ldiring."""

group_means = df.groupby(['Rooms', 'Type'])['BuildingArea'].mean()
rooms_means = df.groupby('Rooms')['BuildingArea'].mean()

# Заполняем пропущенные значения
df['BuildingArea'] = df.apply(
    lambda row: group_means[row['Rooms'], row['Type']] if pd.isna(row['BuildingArea']) else row['BuildingArea'],
    axis=1
)
df['BuildingArea'] = df.apply(
    lambda row: rooms_means[row['Rooms']] if pd.isna(row['BuildingArea']) else row['BuildingArea'],
    axis=1
)

"""### 7-VAZIFA. Yuqoridagi vazifalardan so'ng, bizda faqatgina `CouncilArea` ustunida `NaN` qiymatlar qolishi kerak xolos.
**Bu ustundagi `NaN` qiymatlarni avvalgi qatordagi qiymatlar bilan to'ldirib keting. Natijani saqlab qoling**
"""

df['CouncilArea']=df['CouncilArea'].fillna(method='ffill')

"""## YAKUNIY JADVAL
Ahamiyat bering, yakuniy jadvalda `NaN` qiymatlar bo'lmasligi kerak.
"""

df.isnull().sum()