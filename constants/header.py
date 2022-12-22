class HeaderConst:
    # Account
    ACCOUNT_USERNAME_XPATH = ".//span[contains(text(),'{login_option}')]"
    ACCOUNT_LOGO_XPATH = ".//span[@class='photo']"
    SIGN_OUT_BUTTON_TEXT = "Выйти"
    SIGN_OUT_BUTTON_XPATH = f".//span[contains(text(),'{SIGN_OUT_BUTTON_TEXT}')]"
    SIGN_OUT_ICON_XPATH = ".//mat-icon[contains(text(),'logout')]"
