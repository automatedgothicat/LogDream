import flet as ft
from flet import RouteChangeEvent, Text

def main(page: ft.Page):
    page.title = "Bloco de Notas"

    """ def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        page.views.append(
            View(
                route = '/',
                controls=[
                    ft.AppBar(title=Text('Home')),
                    Text(value='Home'),
                    ft.ElevatedButton(text='Go to notes', on_click=lambda_: page.go('/notepage'))
                ],
            )
        ) """

    notes = []
    
    note_area = ft.TextField(
        label="Nota",
        multiline=True,
        border_color= ft.colors.BLUE_100,
        text_align=ft.TextAlign.START
    )
    notes.append(note_area)
    
    save_button = ft.ElevatedButton(
        text="Salvar Anotações",
        on_click=lambda _: save_notes(note_area.value, page)
    )

    create_button = ft.ElevatedButton(
        text="Criar nova nota",
        on_click=lambda _: create_notes(page)
    )

    def menu_option_selected(e):
        snackbar = ft.SnackBar(ft.Text(f"Opção selecionada: {e.control.text}"))
        page.overlay.append(snackbar) 
        snackbar.open = True
        page.update()

    def create_notes(page):
        new_note_area = ft.TextField(
            label="Nova nota",
            multiline=True,
            border_color= ft.colors.BLUE_100,
            text_align=ft.TextAlign.START
        )
        notes.append(new_note_area)
        page.add(new_note_area)
        page.update()

    def save_notes(content, page):
        try:
            for i, note in enumerate(notes):
                file_name = f"./nota{i + 1}.txt"
                with open(file_name, "w") as file:
                    file.write(f"{note.value}")
            snackbar = ft.SnackBar(ft.Text(f"Anotações salvas com sucesso!"))
            page.overlay.append(snackbar)
            snackbar.open = True 
            page.update()
        except Exception as e:
            snackbar = ft.SnackBar(ft.Text(f"Erro ao salvar: {e}"))
            page.overlay.append(snackbar)
            snackbar.open = True 
            page.update()

    top_line = ft.Row(
        controls=[
            save_button,
            create_button,
        ]
    )

    menu = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(text="Nova Nota", on_click=lambda e: create_notes(e)),
            ft.PopupMenuItem(text="Salvar Todas", on_click=lambda e: save_notes(e)),
            ft.PopupMenuItem(text="Sair", on_click=menu_option_selected)
        ]
    )

    page.appbar = ft.AppBar(
        title=ft.Text("Bloco de Notas"),
        actions=[menu]
    )

    page.add(top_line,note_area)

if __name__ == "__main__":
    ft.app(target=main)
