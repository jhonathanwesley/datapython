import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.scroll = ft.ScrollMode.AUTO

    def change_main_image(event):
        for elem in options.controls:
            if elem == event.control:
                elem.opacity = 1
                main_image.src = elem.image_src
            else:
                elem.opacity = 0.5
        
        main_image.update()
        options.update()

    graph_images = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=8/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(
                    value='Prices',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                    size=28,
                ),

                main_image := ft.Image(
                    src='https://i.postimg.cc/vTk712XH/BTCUSD-2024-10-18-11-15-03.png',
                ),

                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='https://i.postimg.cc/vTk712XH/BTCUSD-2024-10-18-11-15-03.png',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                        ),

                        ft.Container(
                            image_src='https://i.postimg.cc/3J0FM7Jy/MGLU3-2024-10-18-11-15-07.png',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        ),

                        ft.Container(
                            image_src='https://i.postimg.cc/wxGQb3H8/SPX-2024-10-18-11-14-58.png',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                        )
                    ]
                )
            ]
        )
    )

    market_details = ft.Container(
        col={'xs': 12, 'md': 6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=8/16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='Finance',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    value='Taxa de Juros',
                    color=ft.colors.PURPLE,
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),

                ft.Text(
                    value='VIX Index',
                    color=ft.colors.PINK,
                    size=15,
                    italic=True,
                ),

                ft.Text(
                    value='Sentimento de Mercado',
                    color=ft.colors.RED_700,
                    size=18,
                ),

                ft.Text(
                    value='Fluxo de Ordens',
                    color=ft.colors.BLUE_ACCENT,
                    size=20,
                ),

                ft.Text(
                    value='Ajuste Diário',
                    color=ft.colors.AMBER_ACCENT_700,
                    weight=ft.FontWeight.BOLD,
                    size=36,
                ),

                ft.ResponsiveRow(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    columns=12,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6},
                            value='',
                            color=ft.colors.YELLOW_ACCENT,
                            italic=True,
                            size=20,
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            spacing=8,
                            wrap=False,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR_BORDER,
                                    color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
                                ) for _ in range(6)
                            ]
                        )
                    ]
                ),

                ft.Tabs(
                    selected_index=0,
                    indicator_color=ft.colors.DEEP_PURPLE,
                    label_color=ft.colors.PURPLE,
                    unselected_label_color=ft.colors.PINK,
                    indicator_tab_size=16,
                    height=180,
                    tabs=[
                        ft.Tab(
                            text='BTCUSD',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='O Bitcoin é uma criptomoeda descentralizada baseada em tecnologia blockchain, criada em 2009. Ele permite transações digitais seguras e sem intermediários, utilizando um sistema de prova de trabalho (mineração) para validar e registrar as operações.',
                                    color=ft.colors.CYAN_ACCENT_700,
                                    size=12,
                                )
                            )
                        ),

                        ft.Tab(
                            text='PETRO3',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='A Petrobras é uma empresa estatal brasileira de petróleo e gás, fundada em 1953. É uma das maiores do setor, atuando na exploração, produção, refino e distribuição de petróleo, gás natural e derivados, com destaque para a exploração em águas profundas.',
                                    color=ft.colors.BLUE,
                                    size=12,
                                )
                            )
                        ),

                        ft.Tab(
                            text='MAGALU3',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='A Magazine Luiza é uma varejista brasileira fundada em 1957, que atua no comércio de eletrônicos, eletrodomésticos, móveis e outros produtos. Nos últimos anos, se destacou pela forte presença digital, integrando lojas físicas e e-commerce, tornando-se uma referência em transformação digital no varejo brasileiro.',
                                    color=ft.colors.BLUE,
                                    size=11,
                                )
                            )
                        )
                    ]
                ),

                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label='Opere',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.WHITE,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text='BTCUSD'),
                                ft.dropdown.Option(text='PETRO3'),
                                ft.dropdown.Option(text='MAGALU3'),
                            ]
                        ),

                        ft.Dropdown(
                            col=6,
                            label='Contratos',
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.WHITE,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text=f'{num} contratos') for num in range(1, 1151)
                            ]
                        ),
                    ]
                ),

                ft.Container(expand=True),

                ft.ElevatedButton(
                    width=900,
                    text='COMPRAR',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.GREEN
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            ft.MaterialState.HOVERED: ft.colors.BLACK,
                        }
                    )
                ),
                
                ft.ElevatedButton(
                    width=900,
                    text='VENDER',
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.RED
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            ft.MaterialState.HOVERED: ft.colors.BLACK,
                        }
                    )
                )
            ]
        )
    )


    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                graph_images,
                market_details
            ]
        )
    )

    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)
    