from admin_panel import add_student,get_student,update_student,delete_student,add_task,add_classRecordings
def admin():
    print('Your in admin panel')
    print('Choose your operation')
    print('1.Add student')
    print('2.Get student')
    print('3.Update student')
    print('4.Delete student')
    print('5.Add task')
    print('6.Add class recordings')
    op=int(input('Choose operaton to get start: '))
    print('='*40)

    if op == 1:
        print('You can add student')
        add_student()
    if op == 2:
        print('You can get student')
        get_student()
    if op == 3:
        print('You can update student')  
        update_student()     
    if op == 4:
        print('You can delete student')
        delete_student()
    if op ==5:
        print('You can add task')
        add_task()
    if op == 6:
        print('You can add class  recordings') 
        add_classRecordings()  
