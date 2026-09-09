def test_user_name():
    user = {"name": "Lola", 
            "job": "QA Engineer"
            }

    assert user["name"] == "Lola"
    assert user["job"] == "QA"
