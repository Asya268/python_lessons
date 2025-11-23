from smartphone import Smartphone
catalog = [
    Smartphone("Samsung", "Galaxy n56", "+79175468265"),
    Smartphone("Iphone", "16", "+79275478265"),
    Smartphone("Sony", "F546", "+79065465475"),
    Smartphone("Poco", "С75", "+79375468954"),
    Smartphone("Xiaomi", "A5", "+79668549863")
]
for smartphone in catalog:
    print(f"{smartphone.brand_phone} - "
          f"{smartphone.model_phone} . "
          f"{smartphone.number_phone}")
