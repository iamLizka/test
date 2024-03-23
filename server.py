from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.news import News
from data.jobs import Jobs
from forms.user import RegisterForm



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'





@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()

    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form, message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form, message="Такой пользователь уже есть")
        user = User(name=form.name.data, email=form.email.data, about=form.about.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


# def main():
#     db_session.global_init("db/blogs.db")
    # db_session.global_init(f"db/{bd}")
    # db_sess = db_session.create_session()

    # for user in db_sess.query(User).filter(User.address=="module_1",
    #                                        User.speciality.notlike('%engineer%'),
    #                                        User.position.notlike('%engineer%')):
    #     print(user.id)

    # job = Jobs(team_leader=2, job="deployment modules 1 and 2", work_size=11,
    #            collaborators="2, 4", is_finished=True)
    #
    # db_sess.add(job)
    # db_sess.query(Jobs).filter(Jobs.id >= 1).delete()


    # user = db_sess.query(User).filter(User.id == 1).first()
    # print(user.check_password("123456789"))

    # news = News(title="Четкая запись", content="Четкий контент", is_private=False)
    # user.news.append(news)
    # db_sess.commit()



    # user = User(name="Четкий чел", about="Инфа четкого чела", email="clearperson@email.ru")
    # db_sess.add(user)
    # db_sess.commit()

    # app.run()

    # app.run(port=8080, host='127.0.0.1', debug=True)


from data.users import User
from data import db_session


def main():
    db_session.global_init("db/blogs.db")
    # db_sess = db_session.create_session()
    #
    # for user in db_sess.query(User).filter(User.address == "module_1"):
    #     print(user)
    app.run(port=8080, host='127.0.0.1', debug=True)



if __name__ == '__main__':
    main()

# if __name__ == '__main__':
#     main()

