# GET Request

This app creates a simple GET request that returns the number of successful tasks completed by each assignee.

http://127.0.0.1:8000/todo/task_executions/ generates the following response

```
[
    {
        "assignee_id": 1,
        "task_count": 3
    },
    {
        "assignee_id": 2,
        "task_count": 5
    }
]
```