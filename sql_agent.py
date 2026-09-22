import sqlite3


# =====================================================
# CREATE DATABASE
# =====================================================

connection = sqlite3.connect("students.db")
cursor = connection.cursor()


# =====================================================
# CREATE TABLE
# =====================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    marks INTEGER
)
""")


# =====================================================
# INSERT SAMPLE DATA
# =====================================================

cursor.execute("DELETE FROM students")

students = [
    (1, "Rahul", "CSE", 95),
    (2, "Priya", "CSE", 88),
    (3, "Arjun", "ECE", 91),
    (4, "Sneha", "IT", 84),
    (5, "Kiran", "CSE", 78)
]

cursor.executemany(
    "INSERT INTO students VALUES (?, ?, ?, ?)",
    students
)

connection.commit()


# =====================================================
# DATABASE TOOL
# =====================================================

def execute_sql(query):

    try:
        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        return f"Database Error: {e}"


# =====================================================
# USER QUESTION
# =====================================================

question = input(
    "\nEnter your question about the students database: "
)


# =====================================================
# REACT - REASON
# =====================================================

print("\n========================================")
print("REACT AGENT")
print("========================================")

print("\nTHOUGHT:")
print("I need to understand the user's question and find the required information.")


# =====================================================
# REACT - ACTION
# =====================================================

question_lower = question.lower()

if "highest" in question_lower or "maximum" in question_lower:
    sql_query = """
SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 1;
"""

elif "lowest" in question_lower or "minimum" in question_lower:
    sql_query = """
SELECT name, marks
FROM students
ORDER BY marks ASC
LIMIT 1;
"""

elif "average" in question_lower:
    sql_query = """
SELECT AVG(marks)
FROM students;
"""

elif "all students" in question_lower or "show students" in question_lower:
    sql_query = """
SELECT * FROM students;
"""

elif "cse" in question_lower:
    sql_query = """
SELECT * FROM students
WHERE department = 'CSE';
"""

else:
    sql_query = """
SELECT * FROM students;
"""


print("\nACTION:")
print("execute_sql")

print("\nSQL QUERY:")
print(sql_query)


# =====================================================
# TOOL EXECUTION
# =====================================================

result = execute_sql(sql_query)


# =====================================================
# REACT - OBSERVATION
# =====================================================

print("\nOBSERVATION:")
print(result)


# =====================================================
# FINAL ANSWER
# =====================================================

if isinstance(result, str):

    final_answer = result

elif "highest" in question_lower or "maximum" in question_lower:

    if result:
        name = result[0][0]
        marks = result[0][1]

        final_answer = (
            f"{name} has the highest marks with {marks} marks."
        )
    else:
        final_answer = "No student data found."

elif "lowest" in question_lower or "minimum" in question_lower:

    if result:
        name = result[0][0]
        marks = result[0][1]

        final_answer = (
            f"{name} has the lowest marks with {marks} marks."
        )
    else:
        final_answer = "No student data found."

elif "average" in question_lower:

    if result:
        average = result[0][0]

        final_answer = (
            f"The average marks of the students is {average:.2f}."
        )
    else:
        final_answer = "No student data found."

else:

    final_answer = f"The database returned: {result}"


print("\n========================================")
print("FINAL ANSWER")
print("========================================")

print(final_answer)


# =====================================================
# CLOSE DATABASE
# =====================================================

connection.close()

print("\n========================================")
print("SQL AGENT EXPERIMENT COMPLETED")
print("========================================")
