class OrdersAllConst:
    # Page elements
    H1_TEXT = "Все заказы"
    H1_XPATH = ".//h1[contains(text(),'Все заказы')]"

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
    ORDERS_EUR_EUR_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'EUR')]]" \
                           "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_EUR_UAH_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'UAH')]]" \
                           "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_EUR_GBP_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'GBP')]]" \
                           "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_EUR_RUB_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'RUB')]]" \
                           "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_EUR_USDT_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'USDT')]]" \
                            "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_EUR_USD_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(text(),'USD ')]]" \
                           "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
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
                                 "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_CORE_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'Core Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                   "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_MARKETING_XPATH = ".//mat-row[@role='row'][contains(.,'Marketing')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                   "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_MEGADEPH_INT_XPATH = ".//mat-row[@role='row'][contains(.,'MegaDeph INT')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                      "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_PL_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'PL Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                 "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_SLOTOZILLA_XPATH = ".//mat-row[@role='row'][contains(.,'Slotozilla Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                    "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_THE_FIRST_INT_XPATH = ".//mat-row[@role='row'][contains(.,'The_First INT')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                       "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_X_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'X-Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"

    ORDERS_TEAMS_PRODUCT_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'Product Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                      "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_YS_XPATH = ".//mat-row[@role='row'][contains(.,'YS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                            "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"

    ORDERS_TEAMS_SATELLITES_XPATH = ".//mat-row[@role='row'][contains(.,'Satellites Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                    "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_YS_SATELLITES_XPATH = ".//mat-row[@role='row'][contains(.,'YS Satellites')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                       "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"

    # CIS
    ORDERS_TEAMS_MEGADEPH_CIS_XPATH = ".//mat-row[@role='row'][contains(.,'MegaDeph CIS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                      "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_OTHER_XPATH = ".//mat-row[@role='row'][contains(.,'Other')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                               "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_PBN_XPATH = ".//mat-row[@role='row'][contains(.,'PBN')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                             "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_THE_FIRST_CIS_XPATH = ".//mat-row[@role='row'][contains(.,'The_First CIS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                       "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"

    ORDERS_TEAMS_TOP_SEO_XPATH = ".//mat-row[@role='row'][contains(.,'TOP SEO')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                 "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_MULTI_SEO_XPATH = ".//mat-row[@role='row'][contains(.,'Multi SEO')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                   "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"

    ORDERS_TEAMS_ALL_CIS_XPATH = ".//mat-row[@role='row'][contains(.,'All CIS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                 "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"
    ORDERS_TEAMS_DEV_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'Dev team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                  "//mat-cell[contains(@class,'mat-column-sum ng-tns-c137')]"

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
    ORDERS_TYPE_CONTENT_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(@class,'mat-column-order_type')]" \
                                "/span[contains(text(),'content')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TYPE_LINK_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(@class,'mat-column-order_type')]" \
                             "/span[contains(text(),'link')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TYPE_OTHER_XPATH = ".//mat-row[contains(@class,'ng-tns-c137')][mat-cell[contains(@class,'mat-column-order_type')]" \
                              "/span[contains(text(),'other')]]//mat-cell[contains(@class,'mat-column-sum')]"

    # Filters - Order type

    FILTERS_ORDER_TYPE_TITLE_TEXT = "Тип заказа"
    FILTERS_ORDER_TYPE_TITLE_XPATH = f".//mat-label[contains(.,'{FILTERS_ORDER_TYPE_TITLE_TEXT}')]"
    FILTERS_ORDER_TYPE_XPATH = ".//mat-select[contains(@formcontrolname,'order_type')]"
    FILTERS_ORDER_TYPE_LINK_TEXT = "Link"
    FILTERS_ORDER_TYPE_LINK_XPATH = f".//span[@class='mat-option-text'][contains(.,'{FILTERS_ORDER_TYPE_LINK_TEXT}')]"
    FILTERS_ORDER_TYPE_CONTENT_TEXT = "Content"
    FILTERS_ORDER_TYPE_CONTENT_XPATH = f".//span[@class='mat-option-text'][contains(.,'{FILTERS_ORDER_TYPE_CONTENT_TEXT}')]"
    FILTERS_ORDER_TYPE_OTHER_TEXT = "Other"
    FILTERS_ORDER_TYPE_OTHER_XPATH = f".//span[@class='mat-option-text'][contains(.,'{FILTERS_ORDER_TYPE_OTHER_TEXT}')]"
    FILTERS_ORDER_TYPE_CELLS_XPATH = ".//mat-cell[contains(@class,'cdk-column-order_type mat-column-order_type')]"

    H2_NOT_FOUND_TEXT = "Активных заказов не найдено"
    H2_NOT_FOUND_XPATH = f".//h2[contains(.,'{H2_NOT_FOUND_TEXT}')]"
