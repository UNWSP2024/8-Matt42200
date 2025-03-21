START


    // Create an empty dictionary to store courses
    CREATE an empty dictionary `courses`


    // Ask the user how many courses they want to input
    PROMPT user for the number of courses to input: `num_courses`


    // Loop through the number of courses the user wants to enter
    FOR i FROM 1 TO num_courses
        // Prompt user for the course ID and course name
        PROMPT user for course ID: `course_id`
        PROMPT user for course name: `course_name`
        
        // Store course ID and name in the dictionary
        courses[course_id] = course_name
    END FOR


    // Ask the user for the subject to search for
    PROMPT user for the subject: `subject`


    // Output header for the search result
    PRINT "Courses with subject " + subject + ":"


    // Initialize a flag to check if courses are found
    SET found = FALSE


    // Loop through the dictionary to find courses with the given subject
    FOR each course_id, course_name in courses
        IF course_id starts with subject
            // Print the matching course ID and name
            PRINT course_id + ": " + course_name
            SET found = TRUE
        END IF
    END FOR


    // If no courses were found, print a message
    IF found is FALSE
        PRINT "No courses found with that subject."
    END IF


END