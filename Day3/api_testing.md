# T15 – API Testing

## Tools Used
- PowerShell Invoke-RestMethod
- FastAPI Swagger UI

## Testing Performed

1. GET `/students` – Retrieved all student records.
2. GET `/students/1` – Retrieved an individual student.
3. POST `/students` – Added a new student named Priya.
4. GET `/students` – Verified that Priya was successfully added.

## Test Results

| Method | Endpoint | Result |
|---|---|---|
| GET | /students | Passed |
| GET | /students/1 | Passed |
| POST | /students | Passed |
| GET | /students (verification) | Passed |

## Key Learnings
- REST API testing using HTTP methods.
- Sending JSON request bodies.
- Setting Content-Type headers.
- Understanding HTTP status codes.
- Testing APIs using PowerShell and Swagger UI.

## Status
API testing practice completed successfully.