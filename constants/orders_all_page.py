class OrdersAllConst:
    # Page elements
    H1_TEXT = "Все заказы"
    H1_XPATH = f".//h1[contains(text(),'{H1_TEXT}')]"
    H2_NOT_FOUND_TEXT = "Активных заказов не найдено"
    H2_NOT_FOUND_XPATH = f".//h2[contains(.,'{H2_NOT_FOUND_TEXT}')]"

    # Pagination elements
    PAGINATOR_XPATH = ".//mat-form-field[contains(@class,'mat-mdc-paginator-page-size-select')]"
    PAGINATOR_SELECTOR_300_XPATH = ".//span[@class='mdc-list-item__primary-text'][contains(.,'300')]"

    # Total Tables - sum in EUR
    TOTAL_IN_EUR_EUR_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR']]//" \
                             "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'EUR')]/following-sibling::span"
    TOTAL_IN_EUR_USD_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR']]//" \
                             "li[@class='report-total__list-item ng-star-inserted']/span[text()='USD']/following-sibling::span"
    TOTAL_IN_EUR_USDT_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR']]//" \
                              "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'USDT')]/following-sibling::span"
    TOTAL_IN_EUR_UAH_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR']]//" \
                             "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'UAH')]/following-sibling::span"
    TOTAL_IN_EUR_GBP_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR']]//" \
                             "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'GBP')]/following-sibling::span"
    TOTAL_IN_EUR_RUB_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR']]//" \
                             "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'RUB')]/following-sibling::span"
    TOTAL_IN_EUR_ALL_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR']]" \
                             "//li[@class='report-total__list-item report-total__list-item_sum ng-star-inserted']/span[2]"
    TOTAL_IN_EUR_TABLE_VALUES_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR']]//li[@class='report-total__list-item ng-star-inserted']//span[2]"

    # Orders List - sum in EUR
    ORDERS_EUR_EUR_XPATH = ".//mat-row[contains(@class,'ng-tns-c143')][mat-cell[contains(text(),'EUR')]]" \
                           "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_EUR_UAH_XPATH = ".//mat-row[contains(@class,'ng-tns-c143')][mat-cell[contains(text(),'UAH')]]" \
                           "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_EUR_GBP_XPATH = ".//mat-row[contains(@class,'ng-tns-c143')][mat-cell[contains(text(),'GBP')]]" \
                           "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_EUR_RUB_XPATH = ".//mat-row[contains(@class,'ng-tns-c143')][mat-cell[contains(text(),'RUB')]]" \
                           "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_EUR_USDT_XPATH = ".//mat-row[contains(@class,'ng-tns-c143')][mat-cell[contains(text(),'USDT')]]" \
                            "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_EUR_USD_XPATH = ".//mat-row[contains(@class,'ng-tns-c143')][mat-cell[contains(text(),'USD ')]]" \
                           "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_EUR_ALL_XPATH = ".//mat-cell[contains(@class,'mat-column-sum')]"

    # Total Tables - price in currency
    TOTAL_IN_CURRENCY_EUR_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сумма в валюте')]]//" \
                                  "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'EUR')]/following-sibling::span"
    TOTAL_IN_CURRENCY_USD_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сумма в валюте')]]//" \
                                  "li[@class='report-total__list-item ng-star-inserted']/span[text()='USD']/following-sibling::span"
    TOTAL_IN_CURRENCY_USDT_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сумма в валюте')]]//" \
                                   "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'USDT')]/following-sibling::span"
    TOTAL_IN_CURRENCY_UAH_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сумма в валюте')]]//" \
                                  "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'UAH')]/following-sibling::span"
    TOTAL_IN_CURRENCY_GBP_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сумма в валюте')]]//" \
                                  "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'GBP')]/following-sibling::span"
    TOTAL_IN_CURRENCY_RUB_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сумма в валюте')]]//" \
                                  "li[@class='report-total__list-item ng-star-inserted']/span[contains(text(),'RUB')]/following-sibling::span"

    # Orders List - price in currency
    ORDERS_PRICE_EUR_XPATH = ".//mat-cell[contains(text(),'EUR')]"
    ORDERS_PRICE_USD_XPATH = ".//mat-cell[contains(text(),'USD ')]"
    ORDERS_PRICE_USDT_XPATH = ".//mat-cell[contains(text(),'USDT')]"
    ORDERS_PRICE_UAH_XPATH = ".//mat-cell[contains(text(),'UAH')]"
    ORDERS_PRICE_GBP_XPATH = ".//mat-cell[contains(text(),'GBP')]"
    ORDERS_PRICE_RUB_XPATH = ".//mat-cell[contains(text(),'RUB')]"

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
    TOTAL_ALL_TEAMS_SUM_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR по командам']]" \
                                "//li[contains(@class,'report-total__list-item_sum')]/span[2]"
    TOTAL_ALL_TEAMS_VALUES_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR по командам']]" \
                                   "//li[@class='report-total__list-item ng-star-inserted']//span[2]"

    # Orders List - sum by teams
    # INT
    ORDERS_TEAMS_ALL_INT_XPATH = ".//mat-row[@role='row'][contains(.,'All INT')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                 "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_CORE_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'Core Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                   "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_MARKETING_XPATH = ".//mat-row[@role='row'][contains(.,'Marketing')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                   "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_MEGADEPH_INT_XPATH = ".//mat-row[@role='row'][contains(.,'MegaDeph INT')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                      "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_PL_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'PL Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                 "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_SLOTOZILLA_XPATH = ".//mat-row[@role='row'][contains(.,'Slotozilla Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                    "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_THE_FIRST_INT_XPATH = ".//mat-row[@role='row'][contains(.,'The_First INT')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                       "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_X_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'X-Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"

    ORDERS_TEAMS_PRODUCT_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'Product Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                      "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_YS_XPATH = ".//mat-row[@role='row'][contains(.,'YS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                            "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"

    ORDERS_TEAMS_SATELLITES_XPATH = ".//mat-row[@role='row'][contains(.,'Satellites Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                    "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_YS_SATELLITES_XPATH = ".//mat-row[@role='row'][contains(.,'YS Satellites')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                       "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"

    # CIS
    ORDERS_TEAMS_MEGADEPH_CIS_XPATH = ".//mat-row[@role='row'][contains(.,'MegaDeph CIS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                      "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_OTHER_XPATH = ".//mat-row[@role='row'][contains(.,'Other')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                               "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_PBN_XPATH = ".//mat-row[@role='row'][contains(.,'PBN')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                             "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_THE_FIRST_CIS_XPATH = ".//mat-row[@role='row'][contains(.,'The_First CIS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                       "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"

    ORDERS_TEAMS_TOP_SEO_XPATH = ".//mat-row[@role='row'][contains(.,'TOP SEO')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                 "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_MULTI_SEO_XPATH = ".//mat-row[@role='row'][contains(.,'Multi SEO')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                   "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"

    ORDERS_TEAMS_ALL_CIS_XPATH = ".//mat-row[@role='row'][contains(.,'All CIS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                 "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"
    ORDERS_TEAMS_DEV_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'Dev team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                  "//mat-cell[contains(@class,'mat-column-sum ng-tns-c143')]"

    # Total Tables - sum by order type
    TOTAL_TYPE_CONTENT_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сумма в EUR по типу расхода')]]" \
                               "//span[contains(text(),'content')]/following-sibling::span"
    TOTAL_TYPE_LINK_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сумма в EUR по типу расхода')]]" \
                            "//span[contains(text(),'link')]/following-sibling::span"
    TOTAL_TYPE_OTHER_XPATH = ".//div[@class='card-body'][h4[contains(text(),'Сумма в EUR по типу расхода')]]" \
                             "//span[contains(text(),'other')]/following-sibling::span"
    TOTAL_ALL_TYPES_SUM_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR по типу расхода']]" \
                                "//li[contains(@class,'report-total__list-item_sum')]/span[2]"
    TOTAL_ALL_TYPES_VALUES_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR по типу расхода']]" \
                                   "//li[@class='report-total__list-item ng-star-inserted']//span[2]"

    # Orders List - sum by order type
    ORDERS_TYPE_CONTENT_XPATH = ".//mat-row[contains(@class,'ng-tns-c143')][mat-cell[contains(@class,'mat-column-order_type')]" \
                                "/span[contains(text(),'content')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TYPE_LINK_XPATH = ".//mat-row[contains(@class,'ng-tns-c143')][mat-cell[contains(@class,'mat-column-order_type')]" \
                             "/span[contains(text(),'link')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TYPE_OTHER_XPATH = ".//mat-row[contains(@class,'ng-tns-c143')][mat-cell[contains(@class,'mat-column-order_type')]" \
                              "/span[contains(text(),'other')]]//mat-cell[contains(@class,'mat-column-sum')]"

    # _________________________________Filters_________________________________

    # Filters - Счет
    FILTERS_ACCOUNT_TITLE_TEXT = "Счет"
    FILTERS_ACCOUNT_TITLE_XPATH = f".//mat-label[contains(.,'{FILTERS_ACCOUNT_TITLE_TEXT}')]"
    FILTERS_ACCOUNT_XPATH = ".//input[contains(@formcontrolname,'payment_system_details')]"
    FILTERS_ACCOUNT_DETAILS_CELLS_XPATH = ".//div[@class='order__row ng-star-inserted'][contains(.,'Счет')]//div[@class='order__value']"

    # Filters - Имя сервиса
    FILTERS_SERV_NAME_TITLE_TEXT = "Имя сервиса"
    FILTERS_SERV_NAME_TITLE_XPATH = f".//mat-label[contains(.,'{FILTERS_SERV_NAME_TITLE_TEXT}')]"
    FILTERS_SERV_NAME_XPATH = ".//input[contains(@formcontrolname,'payment_service_name')]"
    FILTERS_SERV_NAME_CELLS_XPATH = ".//mat-cell[contains(@class,'cdk-column-payment_service_name')]"

    # Filters - Система оплаты
    FILTERS_PAY_SYS_TITLE_TEXT = "Система оплаты"
    FILTERS_PAY_SYS_TITLE_XPATH = f".//mat-label[contains(.,'{FILTERS_PAY_SYS_TITLE_TEXT}')]"
    FILTERS_PAY_SYS_XPATH = ".//mat-select[contains(@formcontrolname,'payment_system')]"
    FILTERS_PAY_SYS_CARD_TEXT = "Card"
    FILTERS_PAY_SYS_CARD_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_PAY_SYS_CARD_TEXT}')]"
    FILTERS_PAY_SYS_WEBMONEY_TEXT = "Webmoney"
    FILTERS_PAY_SYS_WEBMONEY_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_PAY_SYS_WEBMONEY_TEXT}')]"
    FILTERS_PAY_SYS_BITCOIN_TEXT = "Bitcoin"
    FILTERS_PAY_SYS_BITCOIN_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_PAY_SYS_BITCOIN_TEXT}')]"
    FILTERS_PAY_SYS_TRC20_TEXT = "USDT TRC20"
    FILTERS_PAY_SYS_TRC20_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_PAY_SYS_TRC20_TEXT}')]"
    FILTERS_PAY_SYS_ERC20_TEXT = "USDT ERC20"
    FILTERS_PAY_SYS_ERC20_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_PAY_SYS_ERC20_TEXT}')]"
    FILTERS_PAY_SYS_SKRILL_TEXT = "Skrill"
    FILTERS_PAY_SYS_SKRILL_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_PAY_SYS_SKRILL_TEXT}')]"
    FILTERS_PAY_SYS_NETELLER_TEXT = "Neteller"
    FILTERS_PAY_SYS_NETELLER_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_PAY_SYS_NETELLER_TEXT}')]"
    FILTERS_PAY_SYS_PAYPAL_TEXT = "PayPal"
    FILTERS_PAY_SYS_PAYPAL_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_PAY_SYS_PAYPAL_TEXT}')]"
    FILTERS_PAY_SYS_QIWI_TEXT = "Qiwi"
    FILTERS_PAY_SYS_QIWI_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_PAY_SYS_QIWI_TEXT}')]"
    FILTERS_PAY_SYS_CAPITALIST_TEXT = "Capitalist"
    FILTERS_PAY_SYS_CAPITALIST_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_PAY_SYS_CAPITALIST_TEXT}')]"

    # Filters - Тип заказа
    FILTERS_ORDER_TYPE_TITLE_TEXT = "Тип заказа"
    FILTERS_ORDER_TYPE_TITLE_XPATH = f".//mat-label[contains(.,'{FILTERS_ORDER_TYPE_TITLE_TEXT}')]"
    FILTERS_ORDER_TYPE_XPATH = ".//mat-select[contains(@formcontrolname,'order_type')]"
    FILTERS_ORDER_TYPE_LINK_TEXT = "Link"
    FILTERS_ORDER_TYPE_LINK_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_ORDER_TYPE_LINK_TEXT}')]"
    FILTERS_ORDER_TYPE_CONTENT_TEXT = "Content"
    FILTERS_ORDER_TYPE_CONTENT_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_ORDER_TYPE_CONTENT_TEXT}')]"
    FILTERS_ORDER_TYPE_OTHER_TEXT = "Other"
    FILTERS_ORDER_TYPE_OTHER_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_ORDER_TYPE_OTHER_TEXT}')]"
    FILTERS_ORDER_TYPE_CELLS_XPATH = ".//mat-cell[contains(@class,'cdk-column-order_type mat-column-order_type')]"

    # Filters - Департаменты
    FILTERS_DEPS_TITLE_TEXT = "Департаменты"
    FILTERS_DEPS_TITLE_XPATH = f".//mat-label[contains(.,'{FILTERS_DEPS_TITLE_TEXT}')]"
    FILTERS_DEPS_XPATH = ".//mat-select[contains(@formcontrolname,'departments')]"
    FILTERS_DEPS_INT_GMP_TEXT = "INT iGaming Media Project"
    FILTERS_DEPS_INT_GMP_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_DEPS_INT_GMP_TEXT}')]"
    FILTERS_DEPS_INT_PRODUCTS_TEXT = "INT Products"
    FILTERS_DEPS_INT_PRODUCTS_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_DEPS_INT_PRODUCTS_TEXT}')]"
    FILTERS_DEPS_INT_SATELLITES_TEXT = "INT Satellites"
    FILTERS_DEPS_INT_SATELLITES_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_DEPS_INT_SATELLITES_TEXT}')]"
    FILTERS_DEPS_CIS_GMP_TEXT = "CIS iGaming Media Project"
    FILTERS_DEPS_CIS_GMP_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_DEPS_CIS_GMP_TEXT}')]"
    FILTERS_DEPS_CIS_PRODUCTS_TEXT = "CIS Products"
    FILTERS_DEPS_CIS_PRODUCTS_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_DEPS_CIS_PRODUCTS_TEXT}')]"
    FILTERS_DEPS_CIS_GENERAL_TEXT = "CIS General"
    FILTERS_DEPS_CIS_GENERAL_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_DEPS_CIS_GENERAL_TEXT}')]"

    # Filters - Команды
    FILTERS_TEAMS_TITLE_TEXT = "Команды"
    FILTERS_TEAMS_TITLE_XPATH = f".//mat-label[contains(.,'{FILTERS_TEAMS_TITLE_TEXT}')]"
    FILTERS_TEAMS_XPATH = ".//mat-select[contains(@formcontrolname,'teams')]"
    FILTER_TEAMS_VALUES_LIST_XPATH = ".//mat-optgroup[@role='group']//span[@class='mdc-list-item__primary-text']"

    FILTERS_TEAMS_MEGADEPH_INT_TEXT = "MegaDeph INT"
    FILTERS_TEAMS_MEGADEPH_INT_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_MEGADEPH_INT_TEXT}')]"
    FILTERS_TEAMS_FIRST_INT_TEXT = "The_First INT"
    FILTERS_TEAMS_FIRST_INT_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_FIRST_INT_TEXT}')]"
    FILTERS_TEAMS_ALL_INT_TEXT = "All INT"
    FILTERS_TEAMS_ALL_INT_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_ALL_INT_TEXT}')]"
    FILTERS_TEAMS_MARKETING_TEXT = "Marketing"
    FILTERS_TEAMS_MARKETING_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_MARKETING_TEXT}')]"
    FILTERS_TEAMS_PL_TEXT = "PL Team"
    FILTERS_TEAMS_PL_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_PL_TEXT}')]"
    FILTERS_TEAMS_X_TEXT = "X-Team"
    FILTERS_TEAMS_X_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_X_TEXT}')]"
    FILTERS_TEAMS_CORE_TEXT = "Core Team"
    FILTERS_TEAMS_CORE_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_CORE_TEXT}')]"
    FILTERS_TEAMS_SLOTOZILLA_TEXT = "Slotozilla Team"
    FILTERS_TEAMS_SLOTOZILLA_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_SLOTOZILLA_TEXT}')]"

    FILTERS_TEAMS_PRODUCT_TEXT = "Product Team"
    FILTERS_TEAMS_PRODUCT_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_PRODUCT_TEXT}')]"
    FILTERS_TEAMS_YS_TEXT = "YS"
    FILTERS_TEAMS_YS_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_YS_TEXT}')]"

    FILTERS_TEAMS_YS_SAT_TEXT = "YS Satellites"
    FILTERS_TEAMS_YS_SAT_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_YS_SAT_TEXT}')]"
    FILTERS_TEAMS_SATELLITES_TEXT = "Satellites Team"
    FILTERS_TEAMS_SATELLITES_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_SATELLITES_TEXT}')]"

    FILTERS_TEAMS_FIRST_CIS_TEXT = "The_First CIS"
    FILTERS_TEAMS_FIRST_CIS_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_FIRST_CIS_TEXT}')]"
    FILTERS_TEAMS_MEGADEPH_CIS_TEXT = "MegaDeph CIS"
    FILTERS_TEAMS_MEGADEPH_CIS_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_MEGADEPH_CIS_TEXT}')]"
    FILTERS_TEAMS_PBN_TEXT = "PBN"
    FILTERS_TEAMS_PBN_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_PBN_TEXT}')]"
    FILTERS_TEAMS_OTHER_TEXT = "Other"
    FILTERS_TEAMS_OTHER_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_OTHER_TEXT}')]"

    FILTERS_TEAMS_TOP_SEO_TEXT = "TOP SEO"
    FILTERS_TEAMS_TOP_SEO_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_TOP_SEO_TEXT}')]"
    FILTERS_TEAMS_MULTI_SEO_TEXT = "Multi SEO"
    FILTERS_TEAMS_MULTI_SEO_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_MULTI_SEO_TEXT}')]"

    FILTERS_TEAMS_ALL_CIS_TEXT = "All CIS"
    FILTERS_TEAMS_ALL_CIS_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_ALL_CIS_TEXT}')]"
    FILTERS_TEAMS_DEV_TEXT = "Dev team"
    FILTERS_TEAMS_DEV_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_TEAMS_DEV_TEXT}')]"

    # Filters - Кем обновлено
    FILTERS_UPD_BY_XPATH = ".//mat-select[contains(@formcontrolname,'updated_by_role')]"
    FILTERS_UPD_BY_TITLE_TEXT = "Кем обновлено"
    FILTERS_UPD_BY_TITLE_XPATH = f".//mat-label[contains(.,'{FILTERS_UPD_BY_TITLE_TEXT}')]"
    FILTERS_UPD_BY_CUSTOMER_TEXT = "Заказчик"
    FILTERS_UPD_BY_CUSTOMER_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_UPD_BY_CUSTOMER_TEXT}')]"
    FILTERS_UPD_BY_TEAM_LEAD_TEXT = "Руководитель команды"
    FILTERS_UPD_BY_TEAM_LEAD_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_UPD_BY_TEAM_LEAD_TEXT}')]"
    FILTERS_UPD_BY_MODERATOR_TEXT = "Модератор"
    FILTERS_UPD_BY_MODERATOR_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_UPD_BY_MODERATOR_TEXT}')]"
    FILTERS_UPD_BY_ANALYST_TEXT = "Аналитик"
    FILTERS_UPD_BY_ANALYST_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_UPD_BY_ANALYST_TEXT}')]"
    FILTERS_UPD_BY_HEAD_DEP_TEXT = "Руководитель отдела"
    FILTERS_UPD_BY_HEAD_DEP_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_UPD_BY_HEAD_DEP_TEXT}')]"
    FILTERS_UPD_BY_CEO_COO_TEXT = "COO/CEO"
    FILTERS_UPD_BY_CEO_COO_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_UPD_BY_CEO_COO_TEXT}')]"
    FILTERS_UPD_BY_CELLS_XPATH = ".//mat-cell[contains(@class,'cdk-column-updated_by mat-column-updated_by')]//span[contains(@class,'user-role')]"

    # Filters - ID заказа
    FILTERS_ID_XPATH = ".//input[contains(@formcontrolname,'id')]"
    FILTERS_ID_TITLE_TEXT = "ID заказа"
    FILTERS_ID_TITLE_XPATH = f".//mat-label[contains(.,'{FILTERS_ID_TITLE_TEXT}')]"
    FILTERS_ID_CELLS_XPATH = ".//mat-cell[contains(@class,'cdk-column-id')]"

    # Filters - Статус
    FILTERS_STATUS_DEFAULT_TEXT = "active"
    FILTERS_STATUS_DEFAULT_XPATH = ".//mat-select[contains(@formcontrolname,'status')]//span[contains(@class,'mat-mdc-select-min-line')]"
    FILTERS_STATUS_XPATH = ".//mat-select[contains(@formcontrolname,'status')]"
    FILTER_STATUS_LISTBOX_XPATH = ".//div[@role='listbox']//span[contains(@class,'mdc-list-item__primary-text')]"
    FILTERS_STATUS_ALL_TEXT = "all"
    FILTERS_STATUS_ALL_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_STATUS_ALL_TEXT}')]"
    FILTERS_STATUS_COMPLETED_TEXT = "completed"
    FILTERS_STATUS_COMPLETED_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_STATUS_COMPLETED_TEXT}')]"
    FILTERS_STATUS_DECLINED_TEXT = "declined"
    FILTERS_STATUS_DECLINED_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_STATUS_DECLINED_TEXT}')]"
    FILTERS_STATUS_DELETED_TEXT = "deleted"
    FILTERS_STATUS_DELETED_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_STATUS_DELETED_TEXT}')]"
    FILTERS_STATUS_PAYMENT_TEXT = "payment"
    FILTERS_STATUS_PAYMENT_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_STATUS_PAYMENT_TEXT}')]"
    FILTERS_STATUS_PREPAYMENT_TEXT = "prepayment"
    FILTERS_STATUS_PREPAYMENT_XPATH = f".//span[@class='mdc-list-item__primary-text'][contains(.,'{FILTERS_STATUS_PREPAYMENT_TEXT}')]"
    FILTERS_STATUS_CELLS_XPATH = ".//mat-cell[contains(@class,'cdk-column-current_stage')]"
