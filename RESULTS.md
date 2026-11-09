# API lab results

## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: A Fine Hawaii
- Step 0.12, results of the three runs without a session: fail, fail, pass (flaky)
- Step 0.16, blocks of "how many of the three tools are excluded": 0 tools, 1 tool, 2 tools, 3 tools

## Defect report
- Title: Defect 1: excluding all three tools returns 500 instead of 400
- Request: POST /api/pizza with {"excludedTools":["Knife","Pizza cutter","Scissors"]} and Authorization: token <valid user token>
- Expected result: 400 Bad Request with a JSON error message such as {"error":"no pizza can satisfy the request"}
- Actual result: 500 Internal Server Error with an empty body
- Severity: High

## Part A
- Step A4, status codes when the other user reads, changes and deletes: read 404, change 400, delete 400

## Part B
1. API tests can find real integration failures such as wrong server responses, auth problems, and broken cross-service behavior that unit tests with stubs cannot see. Unit tests with stubs are still useful because they are faster and isolate logic from the full environment.
2. Every test creates its own user to avoid collisions, data races and shared state on a multi-user system. The same idea applies to the shared shop or hotel in Project 2: each test must create its own data and never reuse someone else's account or record.
3. The tests send every request through one session so the load balancer keeps routing the user to the same backend server and the login cookie is preserved. The optional Step 0.12 test without a session was flaky because the login request sometimes hit a different server that had not seen the new user yet.
4. The defect appears when all three tools are excluded. A 500 with an empty body is worse than a 400 with a message because the client cannot tell what went wrong and the application may crash or fail silently. The xfail test stays in the suite to keep the defect visible while the code is still broken, and strict=True makes the run fail as soon as the defect is fixed.
5. Base choice coverage for the model in Step A1 needs 1 + 2 + 3 + 1 + 2 = 9 tests. Full combinations coverage would need 3 x 4 x 2 x 3 = 72 tests.
6. In Step A4, the other user got read 404, change 400, and delete 400. That is plausible because the API treats access to someone else's rating as not found or as a forbidden operation. It is a defect only if the product owner expects a consistent, documented unauthorized status for all three operations; otherwise the actual behavior is just a valid security response.
7. The command curl -H "@madeup.txt" https://quickpizza.grafana.com/api/ratings returns 401 with {"error":"authentication failed"}. This is not a data defect in the database, but it is a reminder that a stranger should never be able to use a made-up token to read or alter real data. On a real system, a leaked token would allow reading or modifying the victim's account unless the system rejects it.
8. An API test checks the exact response contract and backend behaviour more directly than a UI test, while a browser test can confirm what a human user actually sees and interacts with on the page.
