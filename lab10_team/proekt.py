def create_file():
    text_df = pd.DataFrame(columns =    ["title",
                                        "category",
                                        "price",
                                        "discount_price",
                                        "link",
                                        "site",
                                        "catalog",
                                        "stock",
                                        "stock_name",
                                        "article",
                                        "unit",
                                        "order",
                                        "inventory",
                                        "city",
                                        "price_2",
                                        "discount_price_2",
                                        "unit_2"])
    text_df.to_csv("lerua.csv", index=False)


def parse_ler_by_city(city):
    parse_catalog("https://spb.leroymerlin.ru/catalogue/pribory-ucheta-i-izmereniy/", "Приборы учета и измерений", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/predohranitelnaya-armatura/", "Предохранительная арматура", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/truboprovod/", "Трубопровод", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/umnyy-dom/", "Умный дом", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/elementy-pitaniya-i-zaryadnye-ustroystva/", "Элементы питания и зарядные устройства", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/ventilyaciya/", "Вентиляция", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/raspredelitelnye-shchity-i-schetchiki-elektroenergii/", "Распределительные щиты и счетчики электроэнергии", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/kabel-i-montazh/", "Кабель и монтаж", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/rozetki-vyklyuchateli-i-ramki/", "Розетки, выключатели и рамки", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/dekorativnye-paneli-pvh-i-mdf/", "Декоративные панели ПВХ и МДФ", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/pilomaterialy/", "Пиломатериалы", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/drevesno-plitnye-materialy/", "Древесно-плитные материалы", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/stroitelnye-rashodnye-materialy/", "Строительные расходные материалы", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/stroitelnoe-oborudovanie/", "Строительное оборудование", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/podvesnye-potolki/", "Подвесные потолки", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/vodostochnye-i-drenazhnye-sistemy/", "Водосточные и дренажные системы", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/metalloprokat/", "Металлопрокат", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/bloki-dlya-stroitelstva/", "Блоки для строительства", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/oblicovochnye-materialy/", "Облицовочные материалы", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/krovlya/", "Кровля", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/listovye-materialy/", "Листовые материалы", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/izolyacionnye-materialy/", "Изоляционные материалы", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/suhie-smesi-i-gruntovki/", "Сухие смеси и грунтовки", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/oboi-dlya-sten-i-potolka/", "Обои для стен и потолка", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/napolnye-plintusy-porogi-i-aksessuary/", "Напольные плинтусы, пороги и аксессуары", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/otdelochnye-pokrytiya-dlya-pola/", "Отделочные покрытия для пола", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/klei-i-sredstva-dlya-ukladki-plitki/", "Клеи и средства для укладки плитки", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/zatirki-dlya-shvov-plitki/", "Затирки для швов плитки", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/plitka-keramogranit-i-mozaika/", "Плитка, керамогранит и мозаика", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/svetodiodnoe-osveshchenie/", "Светодиодное освещение", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/okna-i-podokonniki/", "Окна и подоконники", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/dveri/", "Двери", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/tehnicheskie-svetilniki/", "Технические светильники", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/osveshchenie-zhilyh-pomeshcheniy/", "Освещение жилых помещений", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/furnitura-dlya-okon/", "Фурнитура для окон", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/furnitura-dlya-dverey/", "Фурнитура для дверей", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/dvernye-ruchki/", "Дверные ручки", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/zamki-komplektuyushchie-i-aksessuary/", "Замки, комплектующие и аксессуары", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/bytovaya-tehnika-dlya-kuhni/", "Бытовая техника для кухни", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/moyki-i-smesiteli-dlya-kuhni/", "Мойки и смесители для кухни", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/stenovye-paneli/", "Стеновые панели", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/stoleshnicy-i-komplektuyushchie/", "Столешницы и комплектующие", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/mebel-dlya-kuhni/", "Мебель для кухни", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/melkaya-bytovaya-tehnika/", "Мелкая бытовая техника", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/vanny-i-komplektuyushchie/", "Ванны и комплектующие", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/unitazy-i-bide/", "Унитазы и биде", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/rakoviny-v-vannuyu-komnatu/", "Раковины в ванную комнату", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/smesiteli-dlya-vannoy-komnaty/", "Смесители для ванной комнаты", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/dushevoe-oborudovanie/", "Душевое оборудование", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/klei/", "Клеи", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/kraski-dlya-vnutrennih-rabot/", "Краски для внутренних работ", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/emali/", "Эмали", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/kraski-dlya-naruzhnyh-rabot/", "Краски для наружных работ", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/podgotovka-poverhnosti-k-pokraske-i-shtukaturke/", "Подготовка поверхности к покраске и штукатурке", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/radiatory-otopleniya/", "Радиаторы отопления", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/teplonositeli-dlya-sistem-otopleniya/", "Теплоносители для систем отопления", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/vodonagrevateli/", "Водонагреватели", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/nasosy/", "Насосы", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/sliv/", "Слив", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/sifony/", "Сифоны", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/teplyy-vodyanoy-pol/", "Тёплый водяной пол", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/polotencesushiteli/", "Полотенцесушители", city)
    parse_catalog("https://spb.leroymerlin.ru/catalogue/vodootvedenie/", "Водоотведение", city)


def csv2xlsx(filepath):
    read_file = pd.read_csv(filepath, encoding = "ISO-8859-1")
    read_file.to_excel(filepath.replace(".csv", "") + ".xlsx", index = None, header=True)


def parse_ler():
    create_file()
    parse_ler_by_city("Москва")
    parse_ler_by_city("СПб")
    csv2xlsx("lerua.csv")