from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour = 5)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    if 6 <= current_time.hour < 22:
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """

    def dark_theme_switcher_is_on(current_time=time(hour = 0), dark_theme_enabled_by_user=None):
        if (6 <= current_time.hour < 22 and dark_theme_enabled_by_user is None) or dark_theme_enabled_by_user is False:
            return False
        else:
            return True

    assert dark_theme_switcher_is_on(time(hour = 5), True) is True
    assert dark_theme_switcher_is_on(time(hour = 6), True) is True
    assert dark_theme_switcher_is_on(time(hour = 7), False) is False
    assert dark_theme_switcher_is_on(time(hour = 22), False) is False
    assert dark_theme_switcher_is_on(time(hour = 5), None) is True
    assert dark_theme_switcher_is_on(time(hour = 6), None) is False
    assert dark_theme_switcher_is_on(time(hour = 21), None) is False
    assert dark_theme_switcher_is_on(time(hour = 22), None) is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = None
    for user in users:
        if user["name"] == "Olga":
            suitable_users = user
            break
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def format_function_name(function_name, *args):
    new_format_name = function_name.__name__.replace('_', ' ').title()

    args_list = [arg for arg in args]

    args_str = ', '.join(args_list)
    args_str_list = f"[{args_str}]"

    new_format_function = f"{new_format_name} {args_str_list}"

    print(new_format_function)
    return new_format_function


def test_readable_function():
    open_browser(browser_name = "Chrome")
    go_to_companyname_homepage(page_url = "https://companyname.com")
    find_registration_button_on_login_page(page_url = "https://companyname.com/login", button_text = "Register")


def open_browser(browser_name):
    actual_result = format_function_name(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = format_function_name(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = format_function_name(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
