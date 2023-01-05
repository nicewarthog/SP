class OrdersAllConst:
    # Total Tables - sum in EUR
    TOTAL_SUM_IN_EUR_XPATH = ".//li[@class='report-total__list-item report-total__list-item_sum ng-star-inserted']/span[2]"

    # Total Tables - sum in currency
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

    # Orders List
    ORDERS_LIST_SUM_IN_EUR_XPATH = ".//mat-cell[contains(@class,'mat-cell cdk-cell cdk-column-sum mat-column-sum ng-tns-c137')]"

    ORDERS_LIST_PRICE_EUR_XPATH = ".//mat-cell[contains(text(),'EUR')]"
    ORDERS_LIST_PRICE_USD_XPATH = ".//mat-cell[contains(text(),'USD ')]"
    ORDERS_LIST_PRICE_USDT_XPATH = ".//mat-cell[contains(text(),'USDT')]"
    ORDERS_LIST_PRICE_UAH_XPATH = ".//mat-cell[contains(text(),'UAH')]"
    ORDERS_LIST_PRICE_GBP_XPATH = ".//mat-cell[contains(text(),'GBP')]"
    ORDERS_LIST_PRICE_RUB_XPATH = ".//mat-cell[contains(text(),'RUB')]"
