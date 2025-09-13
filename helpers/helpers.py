from faker import Faker

faker = Faker('ru_RU')

class UserDataGenerator:

    @staticmethod
    def generate_email():

        return f"{faker.first_name().lower()}{faker.random_int(0, 9999)}@gmail.com"

    @staticmethod
    def generate_password():
        return faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

    @staticmethod
    def generate_name():
        return faker.first_name()

    @staticmethod
    def generate_user_data():

        return {
            'email': UserDataGenerator.generate_email(),
            'password': UserDataGenerator.generate_password(),
            'name': UserDataGenerator.generate_name()
        }