import typer

app = typer.Typer()

@app.command()
def foo():
    """A simple command that prints 'foo'."""
    print("foo")

@app.command()
def bar():
    """A simple command that prints 'bar'."""
    print("bar")

if __name__ == "__main__":
    app()
