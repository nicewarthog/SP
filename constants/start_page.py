class StartPageConst:
    # Page elements
    MAIN_LOGO_XPATH = ".//img[@class='main__logo']"
    H3_XPATH = ".//h3[@class='form-title']"
    H3_TEXT = "Для продолжения войдите в систему"
    LOGIN_FIELD_TITLE_TEXT = "Логин"
    LOGIN_FIELD_TITLE_XPATH = f".//mat-label[contains(text(),'{LOGIN_FIELD_TITLE_TEXT}')]"
    PASSWORD_FIELD_TITLE_TEXT = "Пароль"
    PASSWORD_FIELD_TITLE_XPATH = f".//mat-label[contains(text(),'{PASSWORD_FIELD_TITLE_TEXT}')]"

    # Sign In
    SIGN_IN_LOGIN_FIELD_XPATH = ".//input[@id='mat-input-0']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@id='mat-input-1']"
    SIGN_IN_BUTTON_TEXT = "Войти"
    SIGN_IN_BUTTON_XPATH = ".//button[@class='btn btn-success']"
    EMPTY_LOGIN_MESSAGE_XPATH = ".//mat-error[@id='mat-mdc-error-0']"
    EMPTY_LOGIN_PASSWORD_MESSAGE_TEXT = "Должно быть заполнено"
    EMPTY_PASSWORD_MESSAGE_XPATH = ".//mat-error[@id='mat-mdc-error-0']"
    INCORRECT_CREDENTIALS_MESSAGE_TEXT = "Incorrect login or password."
    INCORRECT_CREDENTIALS_MESSAGE_XPATH = f".//div[contains(text(),'{INCORRECT_CREDENTIALS_MESSAGE_TEXT}')]"
