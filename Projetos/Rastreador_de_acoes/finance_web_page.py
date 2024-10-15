import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.DEEP_PURPLE
    
    layout = ft.Container(
        width=900,
        height=250,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
    )

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)
