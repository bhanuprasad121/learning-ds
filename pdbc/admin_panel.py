from db_connection import mysql_connection
conn=mysql_connection()
curobj=conn.cursor()
def add_task():
    task_id=int(input('Enter task id: '))
    task_name=input('Enter task name: ')
    task_loc=input('Enter link of task: ')
    task_issuedate=input('Enter issue of date of task(YYYY-MM-DD): ')
    query='insert into tasks(task_id,task_name,task_loc,task_issuedate)values(%s,%s,%s,%s)'
    curobj.execute(query,(task_id,task_name,task_loc,task_issuedate))
    conn.commit()
    print(f'Task added sucessfully')
    print('='*40)
def add_classRecordings():
    reco_id=int(input('Enter recording id: '))
    reco_title=input('Enter recording title: ')
    reco_link=input('Enter link of the recording: ')
    reco_issuedate=input('Enter date of recording uploaded(YYYY-MM-DD): ')
    query='insert into recordings(reco_id,reco_title,reco_link,reco_issuedate)values(%s,%s,%s,%s)'
    curobj.execute(query,(reco_id,reco_title,reco_link,reco_issuedate))
    conn.commit()
    print('Class recording is uploaded sucessfully')
    print('='*40)
def delete_student():
    print('Delete student ')
    s_id=int(input('Enter the student admission number to delete the student details: '))
    query='delete from students where stu_admno=%s '
    curobj.execute(query,(s_id,))
    conn.commit()
    print(f'Delete the student details {s_id}')
    print('='*40)
    
def update_student():
    print('Now you can update the students')
    s_id=int(input('Enter student admission number to update his details: '))
    s_year=int(input('Update the year of the student: '))
    s_age=int(input('Update the age of the student: '))
    query='Update students set stu_year=%s,stu_age=%s where stu_admno=%s'
    curobj.execute(query,(s_year,s_age,s_id))
    conn.commit()
    print(f'Updated the student details{s_id}')
    print('='*40)

def get_student():
    print('Now you can get the students detail ')
    print('1.Do you want to get all the details of the students ')
    print('2.Do you want to get few details of the students ')
    op=int(input('Enter the given options: '))
    if op == 1:
        query='select*from students'
        curobj.execute(query)
        allstudata=curobj.fetchall()
        print(allstudata)
    if op==2:
        criteria=input('select *from students where stu_name like %a: ')
        criteria2=int(input('select stu_admno from students:' ))
        query='select * from students where stu_name=%s and stu_admno=%s'
        curobj.execute(query,(criteria,criteria2))
        few=curobj.fetchall()
        print(few)
        print('='*40)

def add_student():
    s_admno=int(input('Enter student admission number: '))
    s_name=input('Enter student name: ')
    s_age=int(input('Enter age: '))
    s_year=int(input('Enter student year: '))
    s_dept=input('Enter department of student: ')
     # query ('insert into students(stu_admno,stu_name,stu_age,stu_year,stu_dept)values(%s,%s,%s,%s,%s)',(s_admno,s_name,s_age,s_year,s_dept))
    curobj.execute('Insert into students(stu_admno,stu_name,stu_age,stu_year,stu_dept)values(%s,%s,%s,%s,%s)',(s_admno,s_name,s_age,s_year,s_dept))
    conn.commit()
    print('added to db')
    print('='*40)