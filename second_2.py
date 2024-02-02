def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as cat:
            lines = cat.readlines()
            for line in lines:
                cat_data = line.strip().split(',')
                cat_info = {'id': cat_data[0], 'name': cat_data[1], 'age': int(cat_data[2])}
                cats_info.append(cat_info)
    except Exception as e:
                print(f'Error: {e}')
    return cats_info
cats_info = get_cats_info("//Users//mac//Desktop//hw_4//cats_info.txt")
print(cats_info)
                                            