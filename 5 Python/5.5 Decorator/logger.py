import logging

def logger(old_function):
    logging.basicConfig(level=logging.INFO, filename="main.log", force =True,
                        filemode="a", encoding='utf-8', 
                        format='%(asctime)s %(levelname)s %(message)s')

    def new_function(*args, **kwargs):

        text = (f'Вызываем функцию {old_function.__name__}' 
                f' c аргументами {args=} и {kwargs=}')
        
        result = old_function(*args, **kwargs)
        
        text += str(f' {result=}')[:100]
        with open("main.log", "a", encoding='utf-8'):
            logging.info(text)
        return result

    return new_function


