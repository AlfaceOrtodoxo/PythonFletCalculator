import flet as ft


class Calculator:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.height = 520
        self.page.window.width = 400
        self.page.bgcolor = ft.colors.BLACK
        self.page.window.resizable = False
        self.page.window.always_on_top = True
        self.page.title = "Calculator"
        self.current_input = []
        self.result = ft.Text(value='0', size=30)
        self.last_op_was_res = False
        self.mainPage()
    
    def onClick(self, e=None):
        button_value = e.control.data
        if not isinstance(self.current_input, list):
            self.current_input = list(self.result.value)
        self.current_input.append(button_value)
        self.result.value = ''.join(self.current_input)
        self.last_op_was_res = False
        self.updateDisplay(self.current_input)

    def onClickNumber(self, e=None):
        button_value = e.control.data
        
        if self.last_op_was_res:
            self.current_input.clear()
            self.result.value = ''
            self.last_op_was_res = False
        
        self.current_input.append(button_value)
        self.result.value = ''.join(self.current_input)
        self.updateDisplay(self.current_input)    
    
    def onClickCalculate(self, e=None):
        button_value = e.control.data
        self.current_input.append(button_value)
        self.result.value = ''.join(self.current_input)
        try:
            expression = ''.join(self.current_input)
            calculated_value = eval(expression)
            self.result.value = str(calculated_value)
            self.current_input = [self.result.value]
            self.last_op_was_res = True
        except Exception as err:
            self.result.value = 'Error'
        self.updateDisplay(list(self.current_input))  

    def equalsCalculate(self, e):
        try:
            expression = ''.join(self.current_input)
            calculated_value = eval(expression)
            self.result.value = str(calculated_value)
            self.current_input = [self.result.value]
            self.last_op_was_res = True
        except Exception as err:
            self.result.value = 'Error'
            self.current_input.clear()

        self.updateDisplay(list(self.current_input))

    def mainClear(self, e=None):
        self.current_input.clear()
        self.result.value = ''
        self.updateDisplay(list(self.result.value))

    def mainNumbers(self):
        return ft.Container(
            height=self.page.height * 0.07,
            width=self.page.width * 0.9,
            border_radius=50,
            bgcolor= ft.colors.GREY_800,
            margin= 10,
            padding= ft.padding.only(right= 20, bottom= 5),
            alignment= ft.alignment.center_right,
            content= self.result
            )

    def buttonsArithmetic(self):
        return ft.Container(
            height=self.page.height * 0.1,
            #bgcolor= ft.colors.GREY,
            content = ft.Row(                
                spacing=30,
                alignment= 'center',
                controls=[
                ft.FloatingActionButton(text='C', data='C', on_click= self.mainClear),
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
                ft.FloatingActionButton(text='7', data='7', on_click=self.onClickNumber),
                ft.FloatingActionButton(text='8', data='8', on_click=self.onClickNumber),
                ft.FloatingActionButton(text='9', data='9', on_click=self.onClickNumber),
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
                ft.FloatingActionButton(text='4', data='4', on_click=self.onClickNumber),
                ft.FloatingActionButton(text='5', data='5', on_click=self.onClickNumber),
                ft.FloatingActionButton(text='6', data='6', on_click=self.onClickNumber),
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
                ft.FloatingActionButton(text='1', data='1', on_click=self.onClickNumber),
                ft.FloatingActionButton(text='2', data='2', on_click=self.onClickNumber),
                ft.FloatingActionButton(text='3', data='3', on_click=self.onClickNumber),
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
                ft.FloatingActionButton(text='0', data='0', on_click=self.onClickNumber),
                ft.FloatingActionButton(text=',', data='.', on_click=self.onClick),
                ft.FloatingActionButton(text='=', data='=', bgcolor=ft.colors.RED, on_click=self.equalsCalculate, key="enter")
                ]
            )
        )
    
    def updateDisplay(self, new_value):
            self.current_input = new_value
            self.page.update()

    def mainPage(self):
        numbers = self.mainNumbers()
        arithmetic_buttons = self.buttonsArithmetic()
        first_row = self.buttonsFirstRow()
        second_row = self.buttonsSecondRow()
        third_row = self.buttonsThirdRow()
        fourth_row = self.buttonsFourthRow()

        self.page.add(numbers, arithmetic_buttons, first_row, second_row, third_row, fourth_row)
        self.updateDisplay(self.current_input)
        self.page.update()

def main(page: ft.Page):
    Calculator(page)


ft.app(target=Calculator)


    