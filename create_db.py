# функція для ініціалізації бази даних та додавання даних

def create_db():
    from app import app
    from models import db, Moni, Arls, Dop, Sti

    with app.app_context():
        # db.drop_all() # видаляє всі таблиці (для навчання)
        db.create_all()  # створює заново

        if not Sti.query.first():
        # ТИПИ МОНІТОР
            st1 = Sti(name="Комп'ютер", description="Дуже потужний комп'ютер", price=23867,
                        image="images/st1.jpg")
            st2 = Sti(name="Комп'ютер", description="Тягне навіть геншин імпакт", price=67696,
                        image="images/st2.jpg")
            st3 = Sti(name="Комп'ютер",description="Надновий комп'ютер, тягне всі ігри, найпотужніший коип'ютер з усіх що ви коли-небуть бачили",
                        price=999999999, image="images/st3.jpg")

            # Додаємо всі суші в чергу (session) БД
            db.session.add_all([st1, st2, st3])

        if not Moni.query.first():
            # ТИПИ МОНІТОР
            mon1 = Moni(name="Монітор MSI 26.5 ", description="MAG 273QP QD-OLED X24 Black / QD-OLED / 240 Гц", price=24942,
                                    image="images/mon1.jpg")
            mon2 = Moni(name="Монітор Acer 23.8", description="EK241YP6bi (UM.QE1EE.601) Black / IPS / 144 Гц", price=3734,
                                    image="images/mon2.jpg")
            mon3 = Moni(name="Монітор Asus 26.5", description="ROG Swift OLED PG27AQDP (90LM0A20-B01A70) Black / OLED / 480 Гц",
                                    price=46000, image="images/mon3.jpg")

            # Додаємо всі суші в чергу (session) БД
            db.session.add_all([mon1, mon2, mon3])

        if not Arls.query.first():
            # ГОЛОВНІ ІНГРЕДІЄНТИ
            arl1 = Arls(name="Системний блок Expert PC ", price=47999, image="images/arl1.jpg")
            arl2 = Arls(name="Системний блок Expert PC Ultimate ", price=46999, image="images/arl2.jpg")
            arl3 = Arls(name="Системний блок QUBE QB Ryzen ", price=90999, image="images/arl3.jpg")

            # Додаємо всі головні інгредієнти в чергу (session) БД
            db.session.add_all([ arl1,  arl2,  arl3])

        if not Dop.query.first():
            # ДОПОВНЕННЯ
            dop1 = Dop(name="Веб-камера для комп'ютера", price=1799, image="images/kyk.jpg")
            dop2 = Dop(name="Клавіатура MCHOSE", price=3599, image="images/key2.jpg")
            dop3 = Dop(name="Килимок для миші ігровий", price=1559, image="images/opo.jpg")
            dop4 = Dop(name="Миша бездротова Logitech ", price=5745, image="images/mum3.jpg")


            # Додаємо всі доповнення в чергу (session) БД
            db.session.add_all([dop1, dop2, dop3, dop4 ])

         # Зберігаємо всі зміни з черги (сесії) у БД
        db.session.commit()

if __name__ == '__main__':
    create_db()
    print("Базу даних успішно ініціалізовано!")