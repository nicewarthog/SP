class OrdersAllConst:
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
    TOTAL_ALL_CURRENCIES_SUM_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR']]" \
                                     "//li[@class='report-total__list-item report-total__list-item_sum ng-star-inserted']/span[2]"
    TOTAL_ALL_CURRENCIES_VALUES_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR']]" \
                                        "//li[@class='report-total__list-item ng-star-inserted']//span[2]"

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

    # Total Tables - sum by teams
    TOTAL_ALL_TEAMS_SUM_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR по командам']]" \
                                "//li[contains(@class,'report-total__list-item_sum')]/span[2]"
    TOTAL_ALL_TEAMS_VALUES_XPATH = ".//div[@class='card-body'][h4[text()='Сумма в EUR по командам']]" \
                                   "//li[@class='report-total__list-item ng-star-inserted']//span[2]"

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

    # Orders List - sum in EUR
    ORDERS_LIST_GENERAL_SUM_IN_EUR_XPATH = ".//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_LIST_EUR_EUR_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'EUR')]]" \
                                "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_LIST_EUR_UAH_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'UAH')]]" \
                                "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_LIST_EUR_GBP_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'GBP')]]" \
                                "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_LIST_EUR_RUB_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'RUB')]]" \
                                "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_LIST_EUR_USDT_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'USDT')]]" \
                                 "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_LIST_EUR_USD_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'USD ')]]" \
                                "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"

    # Orders List - sum in currency
    ORDERS_LIST_PRICE_EUR_XPATH = ".//mat-cell[contains(text(),'EUR')]"
    ORDERS_LIST_PRICE_USD_XPATH = ".//mat-cell[contains(text(),'USD ')]"
    ORDERS_LIST_PRICE_USDT_XPATH = ".//mat-cell[contains(text(),'USDT')]"
    ORDERS_LIST_PRICE_UAH_XPATH = ".//mat-cell[contains(text(),'UAH')]"
    ORDERS_LIST_PRICE_GBP_XPATH = ".//mat-cell[contains(text(),'GBP')]"
    ORDERS_LIST_PRICE_RUB_XPATH = ".//mat-cell[contains(text(),'RUB')]"

    # Orders List - sum by order type
    ORDERS_LIST_TYPE_CONTENT_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(@class,'mat-column-order_type')]" \
                                     "/span[contains(text(),'content')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_LIST_TYPE_LINK_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(@class,'mat-column-order_type')]" \
                                  "/span[contains(text(),'link')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_LIST_TYPE_OTHER_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(@class,'mat-column-order_type')]" \
                                   "/span[contains(text(),'other')]]//mat-cell[contains(@class,'mat-column-sum')]"
