# Computer Programming problem application form

## 3. Problem Title
```
เขียนชื่อโจทย์ของท่านพร้อมระบุความยากใน format: "[1]-กระดานหมากรุก" 
```

## 4. Problem Description
```
ให้ input (ตัวเลขจำนวณเต็มบวก) มา 1 ตัวเลข แล้วให้ print ออกมาเป็นกระดานหมากรุก เหมือนใน test case
restricted keyword: import bin {} [] dict tuple set try except finally replace find
rstrip lstrip strip
```

## 5. Input Specification
```
บรรทัดที่ 1: ตัวเลขจำนวนเต็มบวก 1 เลข
```

## 6. Output Specification
```
บรรทัดที่ 1 ถึง n: ขนาดของกระดานหมากรุก
```

## 7. Test Case
```
--- Case 1 ---
input: 
2

output: 
O X
X O


--- Case 2 ---
input: 
3

output: 
O X O
X O X
O X O
```

--- Case 3 ---
input: 
5

output: 
O X O X O
X O X O X
O X O X O
X O X O X
O X O X O
```

--- Case 4 ---
input: 
8

output: 
O X O X O X O X
X O X O X O X O
O X O X O X O X
X O X O X O X O
O X O X O X O X
X O X O X O X O
O X O X O X O X
X O X O X O X O
```

## 8. Problem Solution
```
""" กระดานหมากรุก """
# รับค่า
size = int(input())

# แสดงผล
for row in range(1, size+1):
    for col in range(1, size+1):
        if col == size:
            if (row+col) % 2 == 0:
                print("O")
            else:
                print("X")
        else:
            if (row+col) % 2 == 0:
                print("O", end=" ")
            else:
                print("X", end=" ")
```
>**การแนบคำตอบโค้ด ให้แนบไฟล์ .py ที่เขียนเพื่อแก้ปัญหาของโจทย์พร้อมกับ markdown ไฟล์นี้ลงใน repository ของผู้สมัคร**

## 9. Problem Reflection
**ระบุตามความเป็นจริง** 
———————

1. คุณได้ใช้ AI ในการช่วยคิดโจทย์ หรือช่วยแก้ปัญหาของโค้ดท่ายหรือไม่ หากใช้ กรุณาระบุว่าใช้ AI ทำอะไรบ้าง?

```
ไม่ได้ใช้
```

2. ได้อิงโจทย์จากแหล่งอะไรก็ตามแต่หรือไม่ หากใช่ ขอให้คุณยืนยันว่าตัวเองเข้าใจโจทย์ และเป็นคนเขียน problem Description และส่วนอื่นๆ ของโจทย์ทั้งหมด รวมถึงเขียนโค้ดคำตอบด้วยตัวเอง

```
อิงโจทย์จาก compro ที่เรียนนั้นครับ แต่ที่เหลือเขียนเองครับ
```

3. ได้ตรวจสอบโค้ดด้วย test case อะไรบ้าง รวมถึง edge case ด้วย

```
test case
ตรวจด้วย 1-10 จะ run ออกมาเป็น กระดานขนาด n*n

edge case
ตรวจด้วย (-1)-(-5) จะ run ออกมาเป็น ว่างเปล่า(ไม่มีคำตอบ)
```

4. ยีนยันว่าโค้ดของผู้สมัครผ่านการทดสอบเรียบร้อยแล้ว สามารถทำงานตามความต้องการของโจทย์ได้ครบทุกข้อกำหนด และผ่านการทดสอบ edge case
และตรวจทานส่วนอื่นๆ เป็นที่เรียบร้อย

```
ใช่
```

## 10. Application Submission

การส่งใบสมัคร **ให้อัปโหลดไฟล์นี้และไฟล์ .py ที่เป็นคำตอบลงใน repository ของผู้สมัครลงบน github แล้วตั้งค่าการมองเห็นเป็นรูปแบบสาธารณะ(public) พร้อมทั้งส่งลิงค์ **repository** ลงในเว็บไซต์รับสมัคร**

หากไม่อัปโหลดจะถือว่าข้อมูลการสมัครตำแหน่ง Architect เป็นโมฆะ