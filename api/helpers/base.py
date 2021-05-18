def check_item(name, model):
    try:
        item = model.objects.get(name=name)
        print(item, 'Already exists')
        return item
    except:
        item = model.objects.create_item(name=name)
        print(item, 'Item created')
        return item
