def atualizar_quantidades(event):
    produto = event
    cursor.execute("SELECT Quantidade FROM Produtos WHERE Produto=?", (produto,))
    quantidades = [str(row[0]) for row in cursor.fetchall()]
    window['quantidade'].update(values=quantidades)
    window['quantidade'].set_value(quantidades[0])

