# API Dev Trial Task



## Setup

To setup this API,  first we will need to setup the environment variables. Create a `.env` file in config directory of the project and store the following content in it. 

```
export DATABASE="" # the database name
export DATABASE_HOST="" # the database host url
export DATABASE_USER="" # the user of the database server
export DATABASE_PASSWORD="" #the password for the database server user
```

To execute this API we will be needing Docker. If you don't have Docker already, please follow the instructions [here](https://docs.docker.com/get-docker/) to install it. Once you have Docker ready, head up to the root directory of the project and run the following commands.

```bash
sudo docker build --tag api-dev-trial-task.
```

```bash
sudo docker run -it --network="host" -p 5008:5008 -t api-dev-trial-task
```

After running the above commands, the API will be live on port `5008`



## API Requests

This section of the documentation shows some sample requests and their responses.

#### Health

To see whether the API is live and running we should the send the following request.

```http
GET <api-url>/api/health
```

If the API is live and running we will see the following response.

```json
{
    "success": true,
    "errors": null,
    "data": {
        "status": "healthy"
    }
}
```



#### Get All quizzes

To get all available quizzes, send the following request.

```http
GET <api-url>/api/getQuiz
```

Response:

```json
{
    "success": true,
    "errors": null,
    "data": {
        "quiz": [
            {
                "id": "e962aaff-772b-4964-bb6d-44b572e1d23g",
                "title": "This is Quiz 3 of Computer Science.",
                "description": "This Quiz will comprise of general SAS concepts.",
                "questions": [
                    {
                        "questionStatement": "This is question 2.",
                        "id": "a8eb9ad4-3b68-4b7e-a000-26f0af8c0a8f",
                        "mandatory": true,
                        "quizId": "e962aaff-772b-4964-bb6d-44b572e1d23g",
                        "options": [
                            {
                                "id": "6cfa6e51-7200-4738-ba62-6c32444a720b",
                                "option": "A",
                                "questionId": "a8eb9ad4-3b68-4b7e-a000-26f0af8c0a8f",
                                "correct": false
                            },
                            {
                                "id": "6cfa6e51-7200-4738-ba62-6c32444a720c",
                                "option": "B",
                                "questionId": "a8eb9ad4-3b68-4b7e-a000-26f0af8c0a8f",
                                "correct": true
                            },
                            {
                                "id": "6cfa6e51-7200-4738-ba62-6c32444a720d",
                                "option": "C",
                                "questionId": "a8eb9ad4-3b68-4b7e-a000-26f0af8c0a8f",
                                "correct": false
                            }
                        ]
                    }
                ]
            },
            {
                "id": "fc5d039b-97ae-4138-9481-85c567a0109f",
                "title": "This is Quiz 5!!!",
                "description": "The topic of this quiz is DLD",
                "questions": [
                    {
                        "questionStatement": "What does TDM mean ?!",
                        "id": "22be920e-ba58-400b-9e97-2d39635e9b0d",
                        "mandatory": true,
                        "quizId": "fc5d039b-97ae-4138-9481-85c567a0109f",
                        "options": [
                            {
                                "id": "6c09699e-ba94-4e7d-bfca-4c92df585216",
                                "option": "Time Death Match",
                                "questionId": "22be920e-ba58-400b-9e97-2d39635e9b0d",
                                "correct": false
                            },
                            {
                                "id": "e05deae4-cd58-4f64-a3d9-7379fc78ced2",
                                "option": "Time Division Mulitplexing",
                                "questionId": "22be920e-ba58-400b-9e97-2d39635e9b0d",
                                "correct": true
                            }
                        ]
                    },
                    {
                        "questionStatement": "What is Python??",
                        "id": "6a43b10e-7d7a-4e52-bf06-476ac103de18",
                        "mandatory": true,
                        "quizId": "fc5d039b-97ae-4138-9481-85c567a0109f",
                        "options": [
                            {
                                "id": "87d278cb-683d-46f6-b347-0fa22ee538e2",
                                "option": "A Programming Language!!",
                                "questionId": "6a43b10e-7d7a-4e52-bf06-476ac103de18",
                                "correct": true
                            },
                            {
                                "id": "f531891a-fd34-44ff-abb8-b07d7abac4ab",
                                "option": "A snake!!",
                                "questionId": "6a43b10e-7d7a-4e52-bf06-476ac103de18",
                                "correct": false
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```



#### Get a Specific Quiz

To get a specific quiz, send the following request with the `id `of the quiz as a query parameter.

```http
GET <api-url>/api/getQuiz?id<quiz-id>
```

Response:

```js
{
    "success": true,
    "errors": null,
    "data": {
        "quiz": [
            {
                "id": "fc5d039b-97ae-4138-9481-85c567a0109f",
                "title": "This is Quiz 5!!!",
                "description": "The topic of this quiz is DLD",
                "questions": [
                    {
                        "questionStatement": "What does TDM mean ?!",
                        "id": "22be920e-ba58-400b-9e97-2d39635e9b0d",
                        "mandatory": true,
                        "quizId": "fc5d039b-97ae-4138-9481-85c567a0109f",
                        "options": [
                            {
                                "id": "6c09699e-ba94-4e7d-bfca-4c92df585216",
                                "option": "Time Death Match",
                                "questionId": "22be920e-ba58-400b-9e97-2d39635e9b0d",
                                "correct": false
                            },
                            {
                                "id": "e05deae4-cd58-4f64-a3d9-7379fc78ced2",
                                "option": "Time Division Mulitplexing",
                                "questionId": "22be920e-ba58-400b-9e97-2d39635e9b0d",
                                "correct": true
                            }
                        ]
                    },
                    {
                        "questionStatement": "What is Python??",
                        "id": "6a43b10e-7d7a-4e52-bf06-476ac103de18",
                        "mandatory": true,
                        "quizId": "fc5d039b-97ae-4138-9481-85c567a0109f",
                        "options": [
                            {
                                "id": "87d278cb-683d-46f6-b347-0fa22ee538e2",
                                "option": "A Programming Language!!",
                                "questionId": "6a43b10e-7d7a-4e52-bf06-476ac103de18",
                                "correct": true
                            },
                            {
                                "id": "f531891a-fd34-44ff-abb8-b07d7abac4ab",
                                "option": "A snake!!",
                                "questionId": "6a43b10e-7d7a-4e52-bf06-476ac103de18",
                                "correct": false
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```





#### Update Quiz

To update something in an existing quiz, send the following request.

```http
PATCH <api-url>/api/updateQuiz
```

Request Body:

```json
{
    "id": "fc5d039b-97ae-4138-9481-85c567a0109f",
    "title": "This is Quiz 6!!!",
    "description": "The topic of this quiz is CP",
    "questions":[
        {
            "id": "22be920e-ba58-400b-9e97-2d39635e9b0d",
            "questionStatement": "What does TDM mean ?!",
            "mandatory": true,
            "options": [
                {
                    "id": "6c09699e-ba94-4e7d-bfca-4c92df585216",
                    "option": "Time Death Match",
                    "correct": false
                },
                {
                    "id": "e05deae4-cd58-4f64-a3d9-7379fc78ced2",
                    "option": "Time Division Mulitplexing",
                    "correct": true
                }
            ]
        },
        {
            "id": "6a43b10e-7d7a-4e52-bf06-476ac103de18",
            "questionStatement": "What is Python??",
            "mandatory": true,
            "options": [
                {
                    "id": "87d278cb-683d-46f6-b347-0fa22ee538e2",
                    "option": "A Programming Language!!",
                    "correct": true
                },
                {
                    "id": "f531891a-fd34-44ff-abb8-b07d7abac4ab",
                    "option": "A snake!!",
                    "correct": false
                }
            ]
        }
    ]
}
```



Response:

```json
{
    "success": true,
    "errors": null,
    "data": {
        "quiz": {
            "id": "fc5d039b-97ae-4138-9481-85c567a0109f",
            "title": "This is Quiz 6!!!",
            "description": "The topic of this quiz is CP",
            "questions": [
                {
                    "id": "22be920e-ba58-400b-9e97-2d39635e9b0d",
                    "mandatory": true,
                    "questionStatement": "What does TDM mean ?!",
                    "quizId": "fc5d039b-97ae-4138-9481-85c567a0109f",
                    "options": [
                        {
                            "id": "6c09699e-ba94-4e7d-bfca-4c92df585216",
                            "option": "Time Death Match",
                            "correct": false,
                            "questionId": "22be920e-ba58-400b-9e97-2d39635e9b0d"
                        },
                        {
                            "id": "e05deae4-cd58-4f64-a3d9-7379fc78ced2",
                            "option": "Time Division Mulitplexing",
                            "correct": true,
                            "questionId": "22be920e-ba58-400b-9e97-2d39635e9b0d"
                        }
                    ]
                },
                {
                    "id": "6a43b10e-7d7a-4e52-bf06-476ac103de18",
                    "mandatory": true,
                    "questionStatement": "What is Python??",
                    "quizId": "fc5d039b-97ae-4138-9481-85c567a0109f",
                    "options": [
                        {
                            "id": "87d278cb-683d-46f6-b347-0fa22ee538e2",
                            "option": "A Programming Language!!",
                            "correct": true,
                            "questionId": "6a43b10e-7d7a-4e52-bf06-476ac103de18"
                        },
                        {
                            "id": "f531891a-fd34-44ff-abb8-b07d7abac4ab",
                            "option": "A snake!!",
                            "correct": false,
                            "questionId": "6a43b10e-7d7a-4e52-bf06-476ac103de18"
                        }
                    ]
                }
            ]
        }
    }
}
```



#### Submit Quiz

To submit a quiz, send the following request.

```http
POST <api-url>/api/submitQuiz
```

Request Body:

```json
{
    "answers": [
        {
            "questionId": "22be920e-ba58-400b-9e97-2d39635e9b0d",
            "questionStatement": "What does TDM mean ?!",
            "optionId": "6c09699e-ba94-4e7d-bfca-4c92df585216",
            "option": "Time Death Match"
        },
        {
            "questionId": "6a43b10e-7d7a-4e52-bf06-476ac103de18",
            "questionStatement": "What is Python??",
            "optionId": "87d278cb-683d-46f6-b347-0fa22ee538e2",
            "option": "A Programming Language!!"
        }
    ]
}
```



Response:

```json
{
    "success": true,
    "errors": null,
    "data": {
        "quiz": {
            "answers": [
                {
                    "questionId": "22be920e-ba58-400b-9e97-2d39635e9b0d",
                    "questionStatement": "What does TDM mean ?!",
                    "optionId": "e05deae4-cd58-4f64-a3d9-7379fc78ced2",
                    "option": "Time Division Mulitplexing"
                },
                {
                    "questionId": "6a43b10e-7d7a-4e52-bf06-476ac103de18",
                    "questionStatement": "What is Python??",
                    "optionId": "87d278cb-683d-46f6-b347-0fa22ee538e2",
                    "option": "A Programming Language!!"
                }
            ],
            "score": "1/2"
        }
    }
}
```



#### Delete Quiz

To delete a quiz, send the following request.

```http
DELETE <api-url>/api/deleteQuiz?<quiz-id>
```

Response:

```json
{
    "success": true,
    "errors": null,
    "data": {
        "quiz": [
            {
                "id": "fc5d039b-97ae-4138-9481-85c567a0109f",
                "title": "This is Quiz 6!!!",
                "description": "The topic of this quiz is CP"
            }
        ]
    }
}
```

