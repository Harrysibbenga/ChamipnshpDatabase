def check_driver(first_name, last_name, nat, model):
    try:
        driver = model.objects.get(first_name=first_name, last_name=last_name, nat=nat)
        print(driver, 'Already exists')
        return driver
    except:
        driver = model.objects.create_driver(first_name=first_name, last_name=last_name, nat=nat)
        print(driver, 'Driver created')
        return driver
