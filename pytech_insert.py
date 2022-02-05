from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.gg85n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# Jimmy Document
jimmy = {
    "student_id": "1007",
    "first_name": "Jimmy",
    "last_name": "Crackcorn",
    "enrollments": [
        {
            "term": "Spring 2022",
            "gpa": "3.75",
            "start_date": "Jan 3, 2022",
            "end_date": "Mar 6, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/database Security",
                    "instructor": "Professor Lappe",
                    "grade": "A+"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Cyber Investigations/Forensics",
                    "instructor": "Professor Fine",
                    "grade": "A-"
                }
            ]
        }
    ]

}

# Jennie document 
jennie = {
    "student_id": "1008",
    "first_name": "Jennie",
    "last_name": "Reynolds",
    "enrollments": [
        {
            "term": "Spring 2022",
            "gpa": "3.25",
            "start_date": "Jan 3, 2022",
            "end_date": "Mar 6, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/database Security",
                    "instructor": "Professor Lappe",
                    "grade": "B+"
                },
                {
                    "course_id": "CYBR420",
                    "description": "Cyber Investigations/Forensics",
                    "instructor": "Professor Fine",
                    "grade": "A-"
                }
            ]
        }
    ]
}
# Jack data document
jack = {
    "student_id": "1009",
    "first_name": "Jack",
    "last_name": "Tripper",
    "enrollments": [
        {
            "term": "Spring 2022",
            "gpa": "4.0",
            "start_date": "Jan 3, 2022",
            "end_date": "Mar 6, 2022",
            "courses": [
                {
                    "course_id": "DAT410",
                    "description": "Advanced Dating Techniques",
                    "instructor": "Professor Beagle",
                    "grade": "A+"
                },
                {
                    "course_id": "KIT420",
                    "description": "Advanced Chef Stuff",
                    "instructor": "Professor Angelino ",
                    "grade": "A+"
                }
            ]
        }
    ]
}
# get the students collection
students = db.students
# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
jimmy_student_id = students.insert_one(jimmy).inserted_id
print("  Inserted student record Jimmy Crackcorn into the students collection with document_id " + str(jimmy_student_id))

jennie_student_id = students.insert_one(jennie).inserted_id
print("  Inserted student record Jennie Reynolds into the students collection with document_id " + str(jennie_student_id))

jack_student_id = students.insert_one(jack).inserted_id
print("  Inserted student record Jack Tripper into the students collection with document_id " + str(jack_student_id))

input("\n\n  End of program, press any key to exit... ")