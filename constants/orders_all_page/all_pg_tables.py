class OrdersAllTablesConst:
    # Total Tables - sum in EUR
    TOTAL_IN_EUR_EUR_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR']]//" \
                             "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'EUR')]/following-sibling::span"
    TOTAL_IN_EUR_USD_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR']]//" \
                             "li[@class='report-total__list-item ng-star-inserted']/span[text()='USD']/following-sibling::span"
    TOTAL_IN_EUR_USDT_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR']]//" \
                              "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'USDT')]/following-sibling::span"
    TOTAL_IN_EUR_UAH_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR']]//" \
                             "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'UAH')]/following-sibling::span"
    TOTAL_IN_EUR_GBP_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR']]//" \
                             "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'GBP')]/following-sibling::span"
    TOTAL_IN_EUR_RUB_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR']]//" \
                             "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'RUB')]/following-sibling::span"
    TOTAL_IN_EUR_ALL_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR']]" \
                             "//li[@class='report-total__list-item report-total__list-item_sum ng-star-inserted']/span[2]"
    TOTAL_IN_EUR_TABLE_VALUES_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR']]//li[@class='report-total__list-item ng-star-inserted']//span[2]"

    # Total Tables - price in currency
    TOTAL_IN_CURRENCY_EUR_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сума у валюті')]]//" \
                                  "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'EUR')]/following-sibling::span"
    TOTAL_IN_CURRENCY_USD_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сума у валюті')]]//" \
                                  "li[@class='report-total__list-item ng-star-inserted']/span[text()='USD']/following-sibling::span"
    TOTAL_IN_CURRENCY_USDT_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сума у валюті')]]//" \
                                   "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'USDT')]/following-sibling::span"
    TOTAL_IN_CURRENCY_UAH_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сума у валюті')]]//" \
                                  "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'UAH')]/following-sibling::span"
    TOTAL_IN_CURRENCY_GBP_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сума у валюті')]]//" \
                                  "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'GBP')]/following-sibling::span"
    TOTAL_IN_CURRENCY_RUB_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сума у валюті')]]//" \
                                  "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'RUB')]/following-sibling::span"

    # Total Tables - sum by teams
    # INT
    TOTAL_TEAMS_ALL_INT_XPATH = ".//span[contains(text(),'All INT')]/following-sibling::span"
    TOTAL_TEAMS_CORE_TEAM_XPATH = ".//span[contains(text(),'Core Team')]/following-sibling::span"
    TOTAL_TEAMS_MARKETING_XPATH = ".//span[contains(text(),'Marketing')]/following-sibling::span"
    TOTAL_TEAMS_MEGADEPH_INT_XPATH = ".//span[contains(text(),'MegaDeph INT')]/following-sibling::span"
    TOTAL_TEAMS_PL_TEAM_XPATH = ".//span[contains(text(),'PL Team')]/following-sibling::span"
    TOTAL_TEAMS_SLOTOZILLA_XPATH = ".//span[contains(text(),'Slotozilla Team')]/following-sibling::span"
    TOTAL_TEAMS_THE_FIRST_INT_XPATH = ".//span[contains(text(),'The_First INT')]/following-sibling::span"
    TOTAL_TEAMS_X_TEAM_XPATH = ".//span[contains(text(),'X-Team')]/following-sibling::span"

    TOTAL_TEAMS_PRODUCT_TEAM_XPATH = ".//span[contains(text(),'Product Team')]/following-sibling::span"
    TOTAL_TEAMS_YS_XPATH = ".//span[contains(text(),'YS')]/following-sibling::span"

    TOTAL_TEAMS_SATELLITES_XPATH = ".//span[contains(text(),'Satellites Team')]/following-sibling::span"
    TOTAL_TEAMS_YS_SATELLITES_XPATH = ".//span[contains(text(),'YS Satellites')]/following-sibling::span"

    # CIS
    TOTAL_TEAMS_MEGADEPH_CIS_XPATH = ".//span[contains(text(),'MegaDeph CIS')]/following-sibling::span"
    TOTAL_TEAMS_OTHER_XPATH = ".//span[contains(text(),'Other')]/following-sibling::span"
    TOTAL_TEAMS_PBN_XPATH = ".//span[contains(text(),'PBN')]/following-sibling::span"
    TOTAL_TEAMS_THE_FIRST_CIS_XPATH = ".//span[contains(text(),'The_First CIS')]/following-sibling::span"

    TOTAL_TEAMS_TOP_SEO_XPATH = ".//span[contains(text(),'TOP SEO')]/following-sibling::span"
    TOTAL_TEAMS_MULTI_SEO_XPATH = ".//span[contains(text(),'Multi SEO')]/following-sibling::span"

    TOTAL_TEAMS_ALL_CIS_XPATH = ".//span[contains(text(),'All CIS')]/following-sibling::span"
    TOTAL_TEAMS_DEV_TEAM_XPATH = ".//span[contains(text(),'Dev team')]/following-sibling::span"

    # All
    TOTAL_ALL_TEAMS_SUM_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR по командах']]" \
                                "//li[contains(@class,'report-total__list-item_sum')]/span[2]"
    TOTAL_ALL_TEAMS_VALUES_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR по командах']]" \
                                   "//li[@class='report-total__list-item ng-star-inserted']//span[2]"

    # Total Tables - sum by order type
    TOTAL_TYPE_CONTENT_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сума в EUR за типом витрат')]]" \
                               "//span[contains(text(),'content')]/following-sibling::span"
    TOTAL_TYPE_LINK_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сума в EUR за типом витрат')]]" \
                            "//span[contains(text(),'link')]/following-sibling::span"
    TOTAL_TYPE_OTHER_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сума в EUR за типом витрат')]]" \
                             "//span[contains(text(),'other')]/following-sibling::span"
    TOTAL_ALL_TYPES_SUM_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR за типом витрат']]" \
                                "//li[contains(@class,'report-total__list-item_sum')]/span[2]"
    TOTAL_ALL_TYPES_VALUES_XPATH = ".//div[@class='card-body'][h4[text()='Сума в EUR за типом витрат']]" \
                                   "//li[@class='report-total__list-item ng-star-inserted']//span[2]"
