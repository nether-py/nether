from Logo import Logo

class App(Component):
    def render(self):
        return (
            <Logo />,
            <p>Edit <code>App.py</code>, save and reload.</p>,
            <a href="https://github.com/Maviek/nether/">Learn Nether</a>
        )

render(<App />, document.getElementById("root"))
