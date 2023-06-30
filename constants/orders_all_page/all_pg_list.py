class OrdersAllListConst:
    # Orders List - sum in EUR
    ORDERS_EUR_EUR_XPATH = ".//mat-row[contains(@class,'example-element-row')][mat-cell[contains(text(),'EUR')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_EUR_UAH_XPATH = ".//mat-row[contains(@class,'example-element-row')][mat-cell[contains(text(),'UAH')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_EUR_GBP_XPATH = ".//mat-row[contains(@class,'example-element-row')][mat-cell[contains(text(),'GBP')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_EUR_RUB_XPATH = ".//mat-row[contains(@class,'example-element-row')][mat-cell[contains(text(),'RUB')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_EUR_USDT_XPATH = ".//mat-row[contains(@class,'example-element-row')][mat-cell[contains(text(),'USDT')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_EUR_USD_XPATH = ".//mat-row[contains(@class,'example-element-row')][mat-cell[contains(text(),'USD ')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_EUR_ALL_XPATH = ".//mat-cell[contains(@class,'mat-column-sum')]"

    # Orders List - price in currency
    ORDERS_PRICE_EUR_XPATH = ".//mat-cell[contains(text(),'EUR')]"
    ORDERS_PRICE_USD_XPATH = ".//mat-cell[contains(text(),'USD ')]"
    ORDERS_PRICE_USDT_XPATH = ".//mat-cell[contains(text(),'USDT')]"
    ORDERS_PRICE_UAH_XPATH = ".//mat-cell[contains(text(),'UAH')]"
    ORDERS_PRICE_GBP_XPATH = ".//mat-cell[contains(text(),'GBP')]"
    ORDERS_PRICE_RUB_XPATH = ".//mat-cell[contains(text(),'RUB')]"

    # Orders List - sum by teams
    # INT
    ORDERS_TEAMS_ALL_INT_XPATH = ".//mat-row[@role='row'][contains(.,'All INT')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                 "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_CORE_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'Core Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                   "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_MARKETING_XPATH = ".//mat-row[@role='row'][contains(.,'Marketing')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                   "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_MEGADEPH_INT_XPATH = ".//mat-row[@role='row'][contains(.,'MegaDeph INT')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                      "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_PL_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'PL Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                 "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_SLOTOZILLA_XPATH = ".//mat-row[@role='row'][contains(.,'Slotozilla Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                    "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_THE_FIRST_INT_XPATH = ".//mat-row[@role='row'][contains(.,'The_First INT')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                       "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_X_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'X-Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                "//mat-cell[contains(@class,'mat-column-sum')]"

    ORDERS_TEAMS_PRODUCT_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'Product Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                      "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_YS_XPATH = ".//mat-row[@role='row'][contains(.,'YS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                            "//mat-cell[contains(@class,'mat-column-sum')]"

    ORDERS_TEAMS_SATELLITES_XPATH = ".//mat-row[@role='row'][contains(.,'Satellites Team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                    "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_YS_SATELLITES_XPATH = ".//mat-row[@role='row'][contains(.,'YS Satellites')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                       "//mat-cell[contains(@class,'mat-column-sum')]"

    # CIS
    ORDERS_TEAMS_MEGADEPH_CIS_XPATH = ".//mat-row[@role='row'][contains(.,'MegaDeph CIS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                      "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_OTHER_XPATH = ".//mat-row[@role='row'][contains(.,'Other')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                               "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_PBN_XPATH = ".//mat-row[@role='row'][contains(.,'PBN')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                             "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_THE_FIRST_CIS_XPATH = ".//mat-row[@role='row'][contains(.,'The_First CIS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                       "//mat-cell[contains(@class,'mat-column-sum')]"

    ORDERS_TEAMS_TOP_SEO_XPATH = ".//mat-row[@role='row'][contains(.,'TOP SEO')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                 "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_MULTI_SEO_XPATH = ".//mat-row[@role='row'][contains(.,'Multi SEO')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                   "//mat-cell[contains(@class,'mat-column-sum')]"

    ORDERS_TEAMS_ALL_CIS_XPATH = ".//mat-row[@role='row'][contains(.,'All CIS')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                 "//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TEAMS_DEV_TEAM_XPATH = ".//mat-row[@role='row'][contains(.,'Dev team')]/preceding::mat-row[contains(@class,'element-row')][1]" \
                                  "//mat-cell[contains(@class,'mat-column-sum')]"

    # Orders List - sum by order type
    ORDERS_TYPE_CONTENT_XPATH = ".//mat-row[contains(@class,'example-element-row')][mat-cell[contains(@class,'mat-column-order_type')]" \
                                "/span[contains(text(),'content')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TYPE_LINK_XPATH = ".//mat-row[contains(@class,'example-element-row')][mat-cell[contains(@class,'mat-column-order_type')]" \
                             "/span[contains(text(),'link')]]//mat-cell[contains(@class,'mat-column-sum')]"
    ORDERS_TYPE_OTHER_XPATH = ".//mat-row[contains(@class,'example-element-row')][mat-cell[contains(@class,'mat-column-order_type')]" \
                              "/span[contains(text(),'other')]]//mat-cell[contains(@class,'mat-column-sum')]"
