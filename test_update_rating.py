import pytest


# Boundary values for a rating update keep valid values while refusing invalid ones.
@pytest.mark.parametrize(
    ("stars", "expected_status"),
    [(0, 400), (1, 200), (5, 200), (6, 400)],
)
def test_rating_update_boundaries(api, auth, rating, stars, expected_status):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected_status

    current = api.get(path, headers=auth).json()
    if expected_status == 200:
        assert current["stars"] == stars
        assert res.json()["stars"] == stars
    else:
        assert current["stars"] == 3
