import tkinter
from timeit import default_timer as timer
import random


def speed_test():
    # Предложения для проверки скорости печати
    тестовые_предложения = [
        'Это случайное предложение для проверки скорости.',
        'Скорость, я - Молния Маккуин.'
    ]

    предложение = random.choice(тестовые_предложения)
    начало = timer()
    
    # Создание главного окна
    основное_окно = tkinter.Tk()
    основное_окно.geometry('600x400')
    основное_окно.title('Тест скорости печати')

    # Метка с предложением для набора
    метка_1 = tkinter.Label(основное_окно, text=предложение, font='times 20')
    метка_1.place(x=150, y=10)

    # Инструкция для пользователя
    метка_2 = tkinter.Label(основное_окно, text='Начинайте печатать:', font='times 20')
    метка_2.place(x=10, y=50)

    # Поле для ввода текста
    поле_ввода = tkinter.Entry(основное_окно, width=40)
    поле_ввода.place(x=280, y=55)

    def проверить_результат():
        """Проверка введённого текста и расчёт времени"""
        if поле_ввода.get() == предложение:
            конец = timer()
            метка_3.configure(text=f'Время: {round((конец-начало), 4)} сек.')
        else:
            метка_3.configure(text='Неверный ввод!')

    # Кнопка завершения теста
    кнопка_1 = tkinter.Button(основное_окно, text='Готово',
                             command=проверить_результат, width=12, bg='grey')
    кнопка_1.place(x=150, y=100)

    # Кнопка повторного теста
    кнопка_2 = tkinter.Button(основное_окно, text='Попробовать снова',
                             command=speed_test, width=12, bg='grey')
    кнопка_2.place(x=250, y=100)

    # Метка для вывода результата
    метка_3 = tkinter.Label(основное_окно, text='', font='times 20')
    метка_3.place(x=10, y=300)

    основное_окно.mainloop()


if __name__ == '__main__':
    speed_test()