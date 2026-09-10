def test_user_name():
    user = {
        "name": "Lola", 
        "job": "QA Engineer"
        }

    assert user["name"] == "Lola"


def test_user_job():
      user = {
                "name": "Lola", 
                "job": "QA Engineer"
        }
      assert user["job"] == "QA"
