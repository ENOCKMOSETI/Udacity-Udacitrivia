# Backend - Full Stack Trivia API Reference 

## Getting Started

    - Base URL: App runs locally at http://127.0.0.1:5000 which is set as a proxy in the frontend configuration 
    - Authentication: This version does not require authentication or API keys

## Endpoints

### GET '/categories'
- Returns an object with a success value and list of categories

- Sample curl http://127.0.0.1:5000/categories
```
    {
        "categories": [
            "Science",
            "Art",
            "Geography",
            "History",
            "Entertainment",
            "Sports"
        ],
        "success": true
    }
```

### GET '/questions'
- Returns an object with a success value, current_category, total number of questions, a list of questions sorted by id and a list of categories.
  Results are paginated in groups of 10. Include an optional page number as a request argument.
  Returns the first page if no argument is passed

- Sample curl http://127.0.0.1:5000/questions
```
    {
    "categories": [
        "Science",
        "Art",
        "Geography",
        "History",
        "Entertainment",
        "Sports"
    ],
    "current_category": null,
    "questions": [
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        }
    ],
    "success": true,
    "total_questions": 24
    }
```
### DELETE '/questions/{id}'
- Removes question with the given id. Returns an object with a success value and the deleted question id

- Sample curl -X DELETE http://127.0.0.1:5000/questions/9
```
    {
        "deleted": 9,
        "success": true
    }
```

### POST '/questions'
- Adds a question to the list of questions. Returns an object with a success value and the created question object.

- Sample curl -X POST -H "Content-Type: application/json" -d '{"question": "hello", "answer": "hello", "difficulty": 1, "category": 2}' http://127.0.0.1:5000/questions
```
    {
        "created": {
            "answer": "hello",
            "category": 2,
            "difficulty": 1,
            "id": 31,
            "question": "hello"
        },
        "success": true
    }
```

### POST '/questions/search'
- Returns an object with a success value, total questions and a list of questions that include the search term

- Sample: curl -X POST -H "Content-Type: application/json" -d '{"searchTerm": "Which"}' http://127.0.0.1:5000/questions/search
```
    {
    "questions": [
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Jackson Pollock",
            "category": 2,
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        },
        {
            "answer": "Scarab",
            "category": 4,
            "difficulty": 4,
            "id": 23,
            "question": "Which dung beetle was worshipped by the ancient Egyptians?"
        }
    ],
    "success": true,
    "total_questions": 7
    }
```
### GET '/categories/{id}/questions'
- Returns an object with a list of questions in the provided category id

- Sample curl https:127.0.0.1:5000/categories/1/questions
```
    {
        "current_category": 1,
        "questions": [
            {
                "answer": "The Liver",
                "category": 1,
                "difficulty": 4,
                "id": 20,
                "question": "What is the heaviest organ in the human body?"
            },
            {
                "answer": "Alexander Fleming",
                "category": 1,
                "difficulty": 3,
                "id": 21,
                "question": "Who discovered penicillin?"
            },
            {
                "answer": "Blood",
                "category": 1,
                "difficulty": 4,
                "id": 22,
                "question": "Hematology is a branch of medicine involving the study of what?"
            },
            {
                "answer": "Guido van Rossum",
                "category": 1,
                "difficulty": 5,
                "id": 24,
                "question": "Who created the Python programming language?"
            },
            {
                "answer": "James Gosling",
                "category": 1,
                "difficulty": 5,
                "id": 25,
                "question": "Who created the Java programming language?"
            }
        ],
        "success": true,
        "total_questions": 5
    }
```
### POST '/quizzes'
- Returns an object with a success value a random question in the specified category provided as a json body

- Sample curl -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"id": 2, "type": "Geography"}}' http://127.0.0.1:5000/questions
```
    {
        "question": {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        "success": true
    }
```

### Testing

To run the tests, run
```
drop database trivia_test

create database trivia_test

psql trivia_test < trivia.psql

python test_flaskr.py
```
