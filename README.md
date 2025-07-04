# Итоговый проект курса @Финальная работа, специализация: Data Engineer"


## Описание проектной деятельности
Data Engineer СберАвтоподписка Pipeline.

## Краткое описание задачи

* Настройте и запустите локальную БД, подходящую для хранения
и исполнения запросов к данным в предоставленном датасете.
* Создайте объекты в БД для хранения данных исходного файла.
* Обработайте и поместите в БД данные из предоставленного
основного датасета.
* Настройте пайплайн сбора, обработки и записи в БД новых .json-
файлов.

## Материалы и ссылки
https://drive.google.com/file/d/1R-Lk45ZeXPf6v13_MfV-8qYp_1wv0N2S/view

https://drive.google.com/drive/folders/1rA4o6KHH-M2KMvBLHp5DZ5gioF2q7hZw

https://drive.google.com/drive/folders/10LlyVJeMvVKQJaHRWkeo2t3sqklPRLJd


## Требования к программному обеспечению и железу

* Установлен Python
* Установлен Git

## Запуск

1. Открываем любой CLI(PowerShell, Git Bash, CMD)
2. Переходим в каталог пользователя(в bash это команда cd ~) или в другой удобный для Вас катало операционной системы.
2. Вводим команду: 
```
git clone https://github.com/savinsyu/Data_Engineer_Sber_Auto.git
```
3. Переходим в папку Data_Engineer_Sber_Auto 
4. Распаковываем [scripts.zip](scripts.zip)
4. Запускаем файл [scripts.py](scripts.py), pipeline запуститься и будет работать всё время перезапуская job каждые 5 секунд.