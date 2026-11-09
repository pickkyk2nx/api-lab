# A different user may not read, change or delete a rating that belongs to someone else.
def test_other_user_cannot_read_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.get(path, headers=other_auth)
    assert 400 <= res.status_code < 500
    assert api.get(path, headers=auth).json() == rating


def test_other_user_cannot_update_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 4}, headers=other_auth)
    assert 400 <= res.status_code < 500
    assert api.get(path, headers=auth).json() == rating


def test_other_user_cannot_delete_rating(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.delete(path, headers=other_auth)
    assert 400 <= res.status_code < 500
    assert api.get(path, headers=auth).json() == rating
