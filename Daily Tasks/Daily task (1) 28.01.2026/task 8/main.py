from add_text_command import AddTextCommand

doc = ["Hello"]

cmd = AddTextCommand(doc, " world!")
cmd.execute()
print(doc[0])

cmd.undo()
print(doc[0])