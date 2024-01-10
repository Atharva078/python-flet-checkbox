import flet as ft

def main(page):
    options = ["Option A", "Option B", "Option C", "Option D","option z"]

    def button_clicked(e):
        selected_options = [option for option, checkbox in zip(options, checkboxes) if checkbox.value]
        t.value = f"Selected options are: {', '.join(selected_options)}"
        page.update()

    checkboxes = [ft.Checkbox(label=option, value=False) for option in options]

    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    t = ft.Text()

    page.add(*checkboxes, b, t)


ft.app(target=main)
