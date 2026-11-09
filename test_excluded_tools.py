import pytest


# The pizza never needs a tool that the customer excluded.
@pytest.mark.parametrize("excluded", [[], ["Knife"], ["Scissors"], ["Knife", "Scissors"]])
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded


@pytest.mark.xfail(
    reason="Defect 1: excluding all three tools returns 500 instead of a 400 error",
    strict=True,
)
def test_all_tools_excluded_is_rejected(api, auth):
    body = {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 400
    assert res.json() == {"error": "no pizza can satisfy the request"}
