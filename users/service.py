from utils.dbUtil import database

def create_user_student(email, username, fullName, phone, role, approveRole, lineNotify, create_date, school, province, file):
    query = "INSERT INTO users(email, username, fullName, phone, role, approveRole, lineNotify, create_date) VALUES('{}','{}','{}','{}','{}',{},{},'{}'); INSERT INTO studentInfo(userId, school, province, file) VALUES(LAST_INSERT_ID(),'{}','{}','{}')".format(
        email, username, fullName, phone, role, approveRole, lineNotify, create_date, school, province, file
    )
    return database.execute(query)

def create_user_teacher(email, username, fullName, phone, role, approveRole, lineNotify, create_date, faculty, majors, description):
    query = "INSERT INTO users(email, username, fullName, phone, role, approveRole, lineNotify, create_date) VALUES('{}','{}','{}','{}','{}',{},{},'{}'); INSERT INTO teacherInfo(userId, faculty, majors, description) VALUES(LAST_INSERT_ID(),'{}','{}','{}')".format(
        email, username, fullName, phone, role, approveRole, lineNotify, create_date, faculty, majors, description
    )
    return database.execute(query)

def update_user_student(email, username, fullName, phone, role, approveRole, lineNotify, school, province, file, id):
    query = f"UPDATE users LEFT JOIN studentInfo ON users.id = studentInfo.userId SET email='{email}', username='{username}', fullName='{fullName}', phone='{phone}', role='{role}', approveRole={approveRole}, lineNotify={lineNotify}, school='{school}', province='{province}', file='{file}' WHERE users.id = {id}"
    return database.execute(query)

def update_user_teacher(email, username, fullName, phone, role, approveRole, lineNotify,  faculty, majors, description, id):
    query = f"UPDATE users LEFT JOIN studentInfo ON users.id = studentInfo.userId SET email='{email}', username='{username}', fullName='{fullName}', phone='{phone}', role='{role}', approveRole={approveRole}, lineNotify={lineNotify}, faculty='{faculty}', majors='{majors}', description='{description}' WHERE users.id = {id}"
    return database.execute(query)

def del_user_student(id):
    query = f"DELETE studentInfo, users FROM studentInfo INNER JOIN users ON users.id = studentInfo.userId WHERE studentInfo.userId = {id}"
    return database.execute(query)

def del_user_teacher(id):
    query = f"DELETE teacherInfo, users FROM teacherInfo INNER JOIN users ON users.id = teacherInfo.userId WHERE teacherInfo.userId = {id}"
    return database.execute(query)



def find_user_byEmail(email:str):
    query = "SELECT * FROM users WHERE email=:email"
    return database.fetch_one(query, values={"email":email})


def create_admin(email, username, role, password):
    query = "INSERT INTO users(email, username, role) VALUES('{}','{}','{}'); INSERT INTO admin(userId, password) VALUES(LAST_INSERT_ID(),'{}')".format(
        email, username, role, password
    )
    return database.execute(query)

def find_exist_admin_email(email:str):
    query = "SELECT * FROM users LEFT JOIN admin ON users.id = admin.userId WHERE email=:email"
    return database.fetch_one(query, values={"email": email})

def get_all_users():
    query = "SELECT * FROM users"
    return database.fetch_all(query)