def course_lookup():
    courses = {}  # Dictionary to store course ID as key and course name as value


    num_courses = int(input("How many courses would you like to enter? "))
    
    for _ in range(num_courses):
        course_id = input("Enter course ID (e.g., COS 2005): ").strip()
        course_name = input("Enter course name: ").strip()


        courses[course_id] = course_name


    subject = input("Enter the subject to search for (e.g., COS): ").strip()


    print(f"\nCourses with subject {subject}:")


    found = False
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")
            found = True
    
    if not found:
        print("No courses found with that subject.")


course_lookup()