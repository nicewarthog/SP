class OrdersAllElementsConst:
    # Page elements
    H1_TEXT = "Всі замовлення"
    H1_XPATH = f".//h1[contains(text(),'{H1_TEXT}')]"
    H2_NOT_FOUND_TEXT = "Активних замовлень не знайдено"
    H2_NOT_FOUND_XPATH = f".//h2[contains(.,'{H2_NOT_FOUND_TEXT}')]"
    H4_TYPE_XPATH = ".//h4[contains(.,'Сума в EUR за типом витрат')]"

    # Pagination elements
    PAGINATOR_XPATH = ".//mat-form-field[contains(@class,'mat-mdc-paginator-page-size-select')]"
    PAGINATOR_SELECTOR_300_XPATH = ".//span[@class='mdc-list-item__primary-text'][contains(.,'300')]"
