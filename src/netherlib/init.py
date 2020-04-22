import os
import toml

HELLO_HTML = '''<!DOCTYPE html>
<html>
<head>
    <title>Nether App</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <div id="root"></div>
    <script type="module">import * as app from './scripts/App.js';</script>
</body>
</html>
'''

HELLO_PY = '''from Logo import Logo

class App(Component):
    def render(self):
        return (
            <Logo />,
            <p>Edit <code>App.py</code>, save and reload.</p>,
            <a href="https://github.com/Maviek/nether/">Learn Nether</a>
        )

render(<App />, document.getElementById("root"))
'''

LOGO_PY = '''class Logo(Component):
    def render(self):
        return (<div class="rotating logo"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#d32f2f" d="M41,12l-7,1H24H14l-7-1c0,0,0,5,6,8c0,0-3,3-3,5c0,0,3,1,3,4l0.9,6.9c0.1,0.7,0.5,1.2,1.1,1.5l3,1.5 h6h6l3-1.5c0.6-0.3,1-0.9,1.1-1.5L35,29c0-3,3-4,3-4c0-2-3-5-3-5C41,17,41,12,41,12z"></path><path fill="#b71c1c" d="M11 3C8 3 0 4.7 0 15c0 3.7 2.5 7.6 4.8 10 .8 1 1.4 1.6 1.5 1.7C6.5 26.9 6.7 27 7 27s.5-.1.7-.3c.4-.4.4-1 0-1.4 0 0-4.7-4.8-4.7-9.3 0 0 0 0 0 0 0-6 4-7 6-7s4 2 4 4c0 0 1 2 1 2l8-4C21.8 10.3 19 3 11 3zM48 15C48 4.7 40 3 37 3c-8 0-10.8 7.3-11 8l8 4c0 0 1-2 1-2 0-2 2-4 4-4s6 1 6 7c0 0 0 0 0 0 0 4.5-4.7 9.2-4.7 9.3-.4.4-.4 1 0 1.4.2.2.5.3.7.3.3 0 .5-.1.7-.3.1-.1.7-.7 1.5-1.7C45.5 22.6 48 18.7 48 15z"></path><path fill="#870808" d="M24,28c0,0-2.4,0-3,0s-1-0.4-1-1s0.4-1,1-1C24,26,24,28,24,28z"></path><path fill="#ff5252" d="M20,27C20,27,20,27,20,27C20,27,20,27,20,27z"></path><path fill="#870808" d="M24,28c0,0,2.4,0,3,0s1-0.4,1-1s-0.4-1-1-1C24,26,24,28,24,28z"></path><path fill="#000001" d="M27,20c0,0,5-3,8-3c-1,3-2,5-4,5C28,22,27,20,27,20z"></path><path fill="#ffd600" d="M31,22c0,0-1-1-1-2s1-2,1-2s1,1,1,2S31,22,31,22z"></path><path fill="#000001" d="M21,20c0,0-5-3-8-3c1,3,2,5,4,5C20,22,21,20,21,20z"></path><path fill="#ffd600" d="M17,22c0,0,1-1,1-2s-1-2-1-2s-1,1-1,2S17,22,17,22z"></path><path fill="#ff5252" d="M33,12c-3-3-7-5-9-5s-6,2-9,5c0,0-4,0-8,0c0,0,2,0,6,6c4,0,6.3,3,9,3c0,0,0.2,0.5-0.8,2 c-0.7,1.1-1.2,2-1.2,4c0-0.2,0.1-1,1-1c2,0,1,2,3,2h0c2,0,1-2,3-2c0.9,0,1,0.8,1,1c0-2-0.5-2.9-1.2-4c-1-1.5-0.8-2-0.8-2 c5,0,5-3,9-3c3-6,6-6,6-6C37,12,33,12,33,12z"></path><path fill="#263238" d="M25,35h-1h-1c-0.6,3.2-5,4-5,4c0,2,2,6,2,6s2-3,2-4c0,3,2,6,2,6s2-3,2-6c0,1,2,4,2,4s2-4,2-6 C30,39,25.6,38.2,25,35z"></path><path fill="#870808" d="M30,33c-0.6,0-1-0.4-1-1c-0.5,0-0.8,0.1-1.3,0.3C26.9,32.6,25.9,33,24,33s-2.9-0.4-3.7-0.7 C19.8,32.1,19.5,32,19,32c0,0.6-0.4,1-1,1s-1-0.4-1-1c0-1,0.7-2,2-2c0.9,0,1.5,0.2,2,0.5c0.7,0.3,1.4,0.5,3,0.5c1.5,0,2.3-0.3,3-0.5 c0.6-0.2,1.2-0.5,2-0.5c1.3,0,2,1,2,2C31,32.6,30.6,33,30,33z"></path></svg></div>)

export(Logo)
'''

HELLO_CSS = '''@-webkit-keyframes rotating {
  from {
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes rotating {
  from {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

.rotating {
  animation: rotating 10s linear infinite;
}

body {
    margin-top: 20vh;
    margin-left: 10vw;
    margin-right: 10vw;
    text-align: center;
    background-color: #20202a;
}

.logo {
    position: relative;
    left: calc(50% - 100px);
    width: 200px;
    margin-bottom: 50px;
}

p, code {
    color: #fff;
}

code {
    font-size: 17px;
}

a {
    color: lightblue;
}

p, a {
    font-size: 16px;
    font-family: "Verdana";
    text-decoration: none;
}
'''


def init(args):
    # Create default package configuration.
    with open('Nether.toml', 'w') as file:
        cfg = {
            'package': {
                'name': os.path.basename(os.getcwd()),
                'version': "0.1.0",
                'authors': [os.environ.get('USER')],
            },
            'dependencies': {},
        }
        toml.dump(cfg, file)

    # Create source and static directory with hello world example.
    os.makedirs('src')

    with open('src/App.py', 'w') as file:
        file.write(HELLO_PY)

    with open('src/Logo.py', 'w') as file:
        file.write(LOGO_PY)

    os.makedirs('static')

    with open('static/index.html', 'w') as file:
        file.write(HELLO_HTML)

    with open('static/style.css', 'w') as file:
        file.write(HELLO_CSS)
