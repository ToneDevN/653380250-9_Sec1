# Lecture Week5 Dictionary and Set

## Dictionary

มีลักษณะเป็น Hash Table เก็บข้อมูลเป็นคู่ Key, Value มี BigO เป็น **O(1)** เร็วในการค้นหา

### ตัวอย่าง Syntax

```python
my_dict = {"key" : "value"} # Key ไม่สามารถซ้ำกันได้
```

### Dictionary Method

#### Creating

- สร้าง **Empty Dictionary** `my_dict = dict()` หรือ `my_dict = {}`
- Dictionary ที่มีค่าเริ่มต้น `student = {'name' : 'Nawamin' , 'age' : 20, 'major' : 'Information Technology', 'gpa' : 3.5`

#### Accessing Value

สามารถเข้าถึงข้อมูล Dictionary ด้วย **Key** ที่มีอยู่ใน Dictionary

```python
my_dict['key']

# Or

my_dict.get('key')
```

### Adding and Modifying Element

เพิ่มข้อมูลใน Dictionary หรือแก้ไขข้อมูลใน Dictionary สามารถทำได้โดยใช้ **Key**

- Remove Element
- Interating Thought
- Other Useful Method

## Set
