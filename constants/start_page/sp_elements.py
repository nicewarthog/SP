class StPgElementsConst:
    MAIN_LOGO_XPATH = ".//img[@class='main__site-logo site-logo']"
    H3_XPATH = ".//h3[@class='form-title']"
    H3_TEXT = "Вхід"
    LOGIN_FIELD_TITLE_TEXT = "Логін"
    LOGIN_FIELD_TITLE_XPATH = f".//mat-label[contains(text(),'{LOGIN_FIELD_TITLE_TEXT}')]"
    PASSWORD_FIELD_TITLE_TEXT = "Пароль"
    PASSWORD_FIELD_TITLE_XPATH = f".//mat-label[contains(text(),'{PASSWORD_FIELD_TITLE_TEXT}')]"
