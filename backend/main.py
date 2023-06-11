import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text

today_weekday = datetime.date.today().weekday()

app = Flask(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})
engine = create_engine("mysql+pymysql://gdsc:NCCUgdsc1234!@34.81.186.58:3306/bricksdata?charset=utf8mb4")

app.config.from_object(__name__)



def open_check(id, conn):
    open_query = """
            SELECT
                weekday, openning_time, closing_time
            FROM
                business_hour
            WHERE
                restaurant_id = {};
        """.format(id)
    open = query_data(conn, open_query)

    matching_dict = None
    for item in open:
        if item["weekday"] == today_weekday:
            matching_dict = item
            break
    opening_time = matching_dict["openning_time"]
    closing_time = matching_dict["closing_time"]
    if opening_time > datetime.datetime.now().time() > closing_time:
        open_status = {
            "operating_status": True,
            "time": closing_time
        }
    else:
        open_status = {
            "operating_status": False,
            "time": opening_time
        }

    return open_status

def query_data(conn, query):
    data = conn.execute(query)
    keys = list(data.keys())
    new_data = [dict(zip(keys, row)) for row in data.fetchall()]

    return new_data

# hello world route
@app.route("/", methods=["GET"])
def greetings():
    return("Hello, world!")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     response_object = {"status": "success"}
#     if request.method == "POST":
#         conn = engine.connect()
#         response_object = {"status": "success"}
#         post_data = request.get_json()
        
#     else:
#         response_object["items"] = U_DATA

#     return jsonify(response_object)

@app.route("/register", methods=["GET", "POST"])
def register():
    response_object = {"status": "success"}
    if request.method == "POST":
        try:
            conn = engine.connect()
            post_data = request.get_json()
            username = post_data.get("user_name")
            email = post_data.get("user_email")
            password = post_data.get("user_password")

            reg_query = """
                SELECT * FROM user WHERE user_name = '{}' OR user_email = '{}'
            """.format(post_data.get("user_name"), post_data.get("user_email"))
            result = conn.execute(reg_query)

            if result.fetchone():
                response_object["status"] = "failed"
                response_object["message"] = "註冊失敗"
            else:
                insert_query = f"INSERT INTO user (user_name, user_password, user_email) VALUES ('{username}', '{password}', '{email}')"
                response_object["message"] = "註冊成功"
                conn.execute(text(insert_query))
                conn.execute(text("COMMIT;"))
            conn.close()
        
        except Exception as e:
            response_object["status"] = "failed"
            response_object["message"] = str(e)



@app.route("/personal_info", methods=["POST"])
def get_personal_info():
    response_object = {"status": "success"}
    if request.method == "POST":
        try:
            conn = engine.connect()
            post_data = request.get_json()
            id = post_data.get("user_id")
            info_query = """
                SELECT user_name, followers, following, profile_photo
                FROM user
                WHERE user_id = {};
            """.format(id)

            diary_query = """
            SELECT resturant_id, date_visited, is_public, review, photo 
            FROM diary 
            WHERE user_id = {};
            """.format(id)

            follower_query = """
            SELECT user.user_name, user.following, user.profile_photo
            FROM 
                following_relation
                JOIN user ON following_relation.followers = user.user_id
            WHERE followers = {};
            """.format(id)

            following_query = """
            SELECT user_name, followers, profile_photo
            FROM 
                following_relation
                JOIN user ON following_relation.following = user.user_id
            WHERE following_relation.following = {};
            """.format(id)

            info = query_data(conn, info_query)
            diary = query_data(conn, diary_query)
            follower = query_data(conn, follower_query)
            following = query_data(conn, following_query)

            response_object["diary"] = diary
            response_object["info"] = info
            response_object["follower"] = follower
            response_object["following"] = following

            conn.close()
        
        except Exception as e:
            response_object["status"] = "failed"
            response_object["message"] = str(e)

@app.route("/follow", methods=["POST"])
def follow():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        following_id = post_data.get("following_id")
        user_id = post_data.get("user_id")

        follow_query = """
            INSERT INTO following_relation (follower, following)
            VALUES 
            ({}, {});
        """.format(following_id, user_id)

        diary = query_data(conn, follow_query)
        response_object["diary"] = diary
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("/disfollow", methods=["POST"])
def disfollow():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        following_id = post_data.get("following_id")
        user_id = post_data.get("user_id")

        diary_query = """
            DELETE FROM following_relation
            WHERE follower = {} AND following = {};
        """.format(following_id, user_id)

        diary = query_data(conn, diary_query)
        response_object["diary"] = diary
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("follower", methods=["POST"])
def follower():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        follower_id = post_data.get("following_id")
        user_id = post_data.get("user_id")

        follow_query = """
            INSERT INTO following_relation (follower, following)
            VALUES 
            ({}, {});
        """.format(user_id, follower_id)

        diary = query_data(conn, follow_query)
        response_object["diary"] = diary
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("disfollower", methods=["POST"])
def disfollower():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        follower_id = post_data.get("following_id")
        user_id = post_data.get("user_id")

        diary_query = """
            DELETE FROM following_relation
            WHERE follower = {} AND following = {};
        """.format(user_id, follower_id)

        diary = query_data(conn, diary_query)
        response_object["diary"] = diary
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)



@app.route("/diary", methods=["POST"])
def get_all_diary():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("user_id")
        diary_query = """
            SELECT
                diary.resturant_id, diary.date_visited, diary.is_public, diary.review, 
                diary.photo, diary.user_id, user.user_name, restaurant.name
            FROM
                diary
                JOIN user ON diary.user_id = user.user_id
                JOIN restaurant ON diary.resturant_id = restaurant.restaurant_id
            WHERE
                diary.user_id = {};
        """.format(id)
        diary = query_data(conn, diary_query)
        response_object["diary"] = diary
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("/diary_info", methods=["POST"])
def get_diary():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("dairy_id")
        diary_query = """
            SELECT
                diary.resturant_id, diary.date_visited, diary.is_public, diary.review, 
                diary.photo, diary.user_id, user.user_name, restaurant.name
            FROM
                diary
                JOIN user ON diary.user_id = user.user_id
                JOIN restaurant ON diary.resturant_id = restaurant.restaurant_id
            WHERE
                diary.diary_id = {};
        """.format(id)
        diary = query_data(conn, diary_query)
        response_object["diary"] = diary
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("/diary_post", methods=["POST"])
def post_diary():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        res_id = post_data.get("restaurant_id")
        user_id = post_data.get("user_id")
        content = post_data.get("content")
        photo = post_data.get("photo")

        diary_query = """
            INSERT INTO diary (restaurant_id, user_id, content, photo)
            VALUES 
            ({}, {}, "{}", "{}");
        """.format(res_id, user_id, content, photo)

        conn.execute(text(diary_query))
        conn.execute(text("COMMIT;"))

        conn.close()

        response_object["message"] = "新增成功"
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("/diary_edit", methods=["POST"])
def edit_diary():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        user_id = post_data.get("user_id")
        content = post_data.get("content")
        photo = post_data.get("photo")

        diary_query = """
            UPDATE diary
            SET content = "{}", photo = "{}"
            WHERE
            user_id = {};
        """.format(content, photo, user_id)

        conn.execute(text(diary_query))
        conn.execute(text("COMMIT;"))

        conn.close()

        response_object["message"] = "新增成功"
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)



@app.route("/list", methods=["POST"])
def get_all_list():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("user_id")
        diary_query = """
            SELECT
                list_id, list_name
            FROM
                list
            WHERE
                user_id = {};
        """.format(id)
        diary = query_data(conn, diary_query)
        response_object["diary"] = diary
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("/list_info", methods=["POST"])
def get_list_info():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("list_id")
        diary_query = """
            SELECT
                list_id, list_name
            FROM
                list
            WHERE
                list_id = {};
        """.format(id)
        diary = query_data(conn, diary_query)
        response_object["diary"] = diary
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)



@app.route("/restaurant", methods=["POST"])
def get_restaurant():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("restaurant_id")
        res_query = """
            SELECT
                restaurant_id, name,address, latitude, longitude, is_open, 
                food_type, phone, email, website, menu_id
            FROM
                restaurant
            WHERE
                restaurant_id = {};
        """.format(id)
        restaurant = query_data(conn, res_query)
        response_object["restaurant"] = restaurant

        open_status = open_check(id, conn)
        response_object["open_status"] = open_status
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("/restaurant_info", methods=["POST"])
def get_restaurant_info():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("restaurant_id")
        res_query = """
            SELECT
                restaurant_id, name,address, is_open, 
                phone, email, website, menu_id
            FROM
                restaurant
            WHERE
                restaurant_id = {};
        """.format(id)
        res_data = conn.execute(res_query)
        keys = list(res_data.keys())
        restaurant = [dict(zip(keys, row)) for row in res_data.fetchall()]
        response_object["restaurant"] = restaurant

        open_status = open_check(id, conn)
        response_object["open_status"] = open_status
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("/restaurant_menu", methods=["POST"])
def get_menu_info():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("menu_id")
        menu_query = """
            SELECT
                menu_id
            FROM
                menu
            WHERE
                menu_id = {};
        """.format(id)
        menu = query_data(conn, menu_query)
        response_object["restaurant"] = menu

        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("/restaurant_comment", methods=["POST"])
def get_comment():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("restaurant_id")
        rating_query = """
            SELECT AVG(deliciousness_rating) AS avg_deliciousness,
                AVG(environment_rating) AS avg_environment,
                AVG(cp_rating) AS avg_cp
                AVG(total_rating) AS avg_total
            FROM feedback_rating
            WHERE restaurant_id = {};
        """.format(id)
        rating = query_data(conn, rating_query)
        response_object["rating"] = rating

        comment_query = """
            SELECT user_id, total_rating, feedback, photo, date_visited
                FROM feedback_rating
                WHERE restaurant_id = {};
        """.format(id)
        comment = query_data(conn, comment_query)
        response_object["comment"] = comment

        diary_query = """
            SELECT user.user_name, user.profile_photo
                FROM diary
                JOIN user ON diary.user_id = user.user_id
                WHERE restaurant_id = {};
        """.format(id)
        diary = query_data(conn, diary_query)
        response_object["comment"] = diary

        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("/restaurant_comment_post", methods=["POST"])
def post_comment():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        res_id = post_data.get("restaurant_id")
        user_id = post_data.get("user_id")
        del_rating = post_data.get("deliciousness_rating")
        env_rating = post_data.get("environment_rating")
        cp_rating = post_data.get("cp_rating")
        comment = post_data.get("comment")
        photo = post_data.get("photo")
        total_rating = (del_rating + cp_rating + env_rating) / 3


        comment_query = """
            INSERT INTO feedback_rating (restaurant_id, user_id, deliciousness_rating,
            environment_rating, cp_rating, total_rating, comment, photo)
            VALUES 
            ({}, {}, {}, {}, {}, {}, "{}", "{}");
        """.format(res_id, user_id, del_rating, env_rating, cp_rating, total_rating, comment, photo)

        conn.execute(text(comment_query))
        conn.execute(text("COMMIT;"))

        conn.close()

        response_object["message"] = "新增成功"
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

@app.route("/restaurant_add_list", methods=["POST"])
def add_list():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        res_id = post_data.get("restaurant_id")
        user_id = post_data.get("user_id")
        list_id = post_data.get("list_id")
        is_visited = post_data.get("is_visited")
        is_favorite = post_data.get("is_favorite")
        is_wanted = post_data.get("is_wanted")

        




        insert_query = """
            INSERT INTO list (restaurant_id, user_id)
            VALUES 
            ({}, {}, {}, {}, {}, {}, "{}", {}, "{}");
        """.format()

        conn.execute(text(insert_query))
        conn.execute(text("COMMIT;"))

        conn.close()

        response_object["message"] = "新增成功"
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)


if __name__ == "__main__":
    app.run(debug=True)