def run():
    my_dict = {
        'nombre': 'aldo',
        'edad':33,
        'empresa': 'oncosalud'
    }
    my_dict2 = {key:val for elements in my_dict.items()}
    print  (my_dict2)


if __name__ == '__main__':
    run()