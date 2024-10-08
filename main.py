import flet as ft


class Calculator:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.height = 500
        self.page.window.width = 400
        self.page.bgcolor = ft.colors.BLACK
        self.page.window.resizable = False
        self.page.window.always_on_top = True
        self.page.title = "Ortodox Lettuce's Calculator"
        self.current_input = []
        self.result = ft.Text(value='0', size=30)
        self.mainPage()
        self.page.update()
    
    def onClick(self, e):
        button_value = e.control.data
        self.current_input.append(button_value)
        self.result.value = ''.join(self.current_input)
        print(self.current_input)
        self.page.update()

    def onClickCalculate(self, e):
        button_value = e.control.data
        self.current_input.append(button_value)
        self.result.value = ''.join(self.current_input)
        print(self.current_input)
        self.page.update()
        try:
            expression = ''.join(self.current_input)
            calculated_value = eval(expression)
            self.result.value = str(calculated_value)
            self.current_input.clear()
            self.current_input.append(str(self.result.value))
            print(self.current_input)
        except Exception as err:
            self.result.value = 'Error'
        self.page.update()       


    def clear(self):
        self.current_input.clear()
        self.result.value = '0'
        print(self.current_input)
        self.page.update()

    def buttonsArithmetic(self):
        return ft.Container(
            height=self.page.height * 0.1,
            #bgcolor= ft.colors.GREY,
            content = ft.Row(
                spacing=30,
                alignment= 'center',
                controls=[
                ft.FloatingActionButton(text='C', data='C', on_click= self.clear()),
                ft.FloatingActionButton(text='x²', data='**2', on_click=self.onClickCalculate),
                ft.FloatingActionButton(text='%', data='*0.01', on_click=self.onClickCalculate),
                ft.FloatingActionButton(text='÷', data='/', on_click=self.onClick)
                ]
            )
        )
    
    def buttonsFirstRow(self):
        return ft.Container(
            height=self.page.height * 0.1,
            content = ft.Row(
                spacing=30,
                alignment= 'center',
                controls=[
                ft.FloatingActionButton(text='7', data='7', on_click=self.onClick),
                ft.FloatingActionButton(text='8', data='8', on_click=self.onClick),
                ft.FloatingActionButton(text='9', data='9', on_click=self.onClick),
                ft.FloatingActionButton(text='X', data='*', on_click=self.onClick)
                ]
            )
        )

    def buttonsSecondRow(self):
        return ft.Container(
            height=self.page.height * 0.1,
            content = ft.Row(
                spacing=30,
                alignment= 'center',
                controls=[
                ft.FloatingActionButton(text='4', data='4', on_click=self.onClick),
                ft.FloatingActionButton(text='5', data='5', on_click=self.onClick),
                ft.FloatingActionButton(text='6', data='6', on_click=self.onClick),
                ft.FloatingActionButton(text='-', data='-', on_click=self.onClick)
                ]
            )
        )

    def buttonsThirdRow(self):
        return ft.Container(
            height=self.page.height * 0.1,
            content = ft.Row(
                spacing=30,
                alignment= 'center',
                controls=[
                ft.FloatingActionButton(text='1', data='1', on_click=self.onClick),
                ft.FloatingActionButton(text='2', data='2', on_click=self.onClick),
                ft.FloatingActionButton(text='3', data='3', on_click=self.onClick),
                ft.FloatingActionButton(text='+', data='+', on_click=self.onClick)
                ]
            )
        )

    def buttonsFourthRow(self):
        return ft.Container(
            height=self.page.height * 0.1,
            content = ft.Row(
                spacing=30,
                alignment= 'center',
                controls=[
                ft.FloatingActionButton(text='+/-', data='*(-1)', on_click=self.onClickCalculate),
                ft.FloatingActionButton(text='0', data='0', on_click=self.onClick),
                ft.FloatingActionButton(text=',', data='.', on_click=self.onClick),
                ft.FloatingActionButton(text='=', data='=', bgcolor=ft.colors.RED, on_click=self.calculate, key="enter")
                ]
            )
        )
    
    def calculate(self, e):
        try:
            expression = ''.join(self.current_input)
            calculated_value = eval(expression)
            self.result.value = str(calculated_value)
            self.current_input.clear()
            self.current_input.append(str(self.result.value))
            print(self.current_input)
        except Exception as err:
            self.result.value = 'Error'
        self.page.update()



    def mainPage(self):
        input_field = ft.TextField(
            fill_color= ft.colors.GREY_900,
            text_align='left',
            height= 300,
            #cursor_height= 150
            expand= True,
            border_radius=300
        )


        arithmetic_buttons = self.buttonsArithmetic()
        first_row = self.buttonsFirstRow()
        second_row = self.buttonsSecondRow()
        third_row = self.buttonsThirdRow()
        fourth_row = self.buttonsFourthRow()

        self.page.add(input_field, arithmetic_buttons, first_row, second_row, third_row, fourth_row)
        self.page.update()

ft.app(target=Calculator)


    