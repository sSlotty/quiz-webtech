## quiz-webtech 💻
### install
การติดตั้ง จำเป็นที่จะต้องสร้าง virtualenv ก่อน
#### clone project
```
git clone https://github.com/sSlotty/quiz-webtech
```
#### install lib
```
pip install -r requirements.txt
```
#### start project
```
python app.py
```
### Feature
  - get food by name and calories
  - get bmr
  - create food
  - edit food
  - delete food
### Path 
  #### GET
  ```
  localhost:5000/foods [ get food by param optional name / calories ]
  ```
  #### POST
  ```
  localhost:5000/foods [ create food ]
  ```
  #### PUT
  ```
  localhost:5000/foods [ edit food ]
  ```
  #### DELETE
  ```
  localhost:5000/foods/delete/{name} [ DELETE food ]
  ```
  #### GET BMR
  ```
  localhost:5000/bmr [ GET BMR param : name , age , weight , height, gender ]
  ```
  
### Author 👱🏻‍♂️
```
Thanathip Chanasri
Computer Science Faculy of Science Srinakharinwirot University
```
