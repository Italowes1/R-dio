from flask import Flask, render_template, redirect, request, render_template_string, session
from flask_htmx import HTMX
from firebird.driver import connect

app = Flask(__name__)
htmx = HTMX(app)
app.secret_key = '1092837465'

con = connect(
    database='C:\Radio-Maffei\\JMRadio\\database\\JMRADIODB.FDB',
    user='SYSDBA',
    password='masterkey',
    charset='UTF8'
    )

@app.route("/")
def index():           
    cursor = con.cursor()
    cursor.execute("select * from programacao p order by p.diasemana, p.horaini")
    row = cursor.fetchall()   
    cursor.close()      

    dom = []
    seg = []
    ter = []
    qua = []
    qui = []
    sex = []
    sab = []
    col = []

    for i in row:
        col.append(str(i[0])[:5])
        col.append(str(i[1])[:5])
        col.append(i[2])
        col.append(str(i[3]).encode('windows-1251').decode('latin1'))
        if i[2] == 1:    
            dom.append(col)
        elif i[2] == 2:
            seg.append(col)
        elif i[2] == 3:
            ter.append(col)
        elif i[2] == 4:
            qua.append(col)
        elif i[2] == 5:
            qui.append(col)
        elif i[2] == 6:
            sex.append(col)
        elif i[2] == 7:
            sab.append(col)                   
        col = []

    return render_template("index.html", dom=dom, seg=seg, ter=ter, qua=qua, qui=qui, sex=sex, sab=sab)

@app.route("/inicio", methods=['POST'])
def inicio():               
    cursor = con.cursor()
    cursor.execute("select * from programacao p order by p.diasemana, p.horaini")
    row = cursor.fetchall()   
    cursor.close()       

    dom = []
    seg = []
    ter = []
    qua = []
    qui = []
    sex = []
    sab = []
    col = []

    for i in row:
        col.append(str(i[0])[:5])
        col.append(str(i[1])[:5])
        col.append(i[2])
        col.append(str(i[3]).encode('windows-1251').decode('latin1'))
        if i[2] == 1:    
            dom.append(col)
        elif i[2] == 2:
            seg.append(col)
        elif i[2] == 3:
            ter.append(col)
        elif i[2] == 4:
            qua.append(col)
        elif i[2] == 5:
            qui.append(col)
        elif i[2] == 6:
            sex.append(col)
        elif i[2] == 7:
            sab.append(col)                   
        col = []

    doms = ''    
    segs = ''    
    ters = ''    
    quas = ''    
    quis = ''    
    sexs = ''    
    sabs = ''    

    for i in dom:
        doms = doms +  f"""
                            <li>{ i[3] } - { i[0] }/{ i[1] }</li>
                        """         
    for i in seg:
        segs = segs +  f"""
                            <li>{ i[3] } - { i[0] }/{ i[1] }</li>
                        """         
    for i in ter:
        ters = ters +  f"""
                            <li>{ i[3] } - { i[0] }/{ i[1] }</li>
                        """         
    for i in qua:
        quas = quas +  f"""
                            <li>{ i[3] } - { i[0] }/{ i[1] }</li>
                        """         
    for i in qui:
        quis = quis +  f"""
                            <li>{ i[3] } - { i[0] }/{ i[1] }</li>
                        """         
    for i in sex:
        sexs = sexs +  f"""
                            <li>{ i[3] } - { i[0] }/{ i[1] }</li>
                        """         
    for i in sab:
        sabs = sabs +  f"""
                            <li>{ i[3] } - { i[0] }/{ i[1] }</li>
                        """         
                                      
    return render_template_string("""
                                    <div class="divmenu">
                                        <img onclick="MenuO()" id="MenuOpen" src="{{ url_for('static', filename='img/Menu.png') }}" alt="Menu">
                                        <div id="menu" class="menu">
                                            <a id="ativado" hx-post="/" hx-target=".container">Início</a>
                                            <a hx-post="/quemsomos" hx-target=".container">Quem Somos</a>
                                            <a hx-post="/coordenacao" hx-target=".container">Coordenação</a>
                                            <a hx-post="/programacao" hx-target=".container">Programação</a>
                                            <a hx-post="/midia" hx-target=".container">Mídia</a>
                                            <a hx-post="/roteiro" hx-target=".container">Roteiro</a>
                                            <a hx-post="/locucao" hx-target=".container">Locução</a>
                                        </div>
                                    </div>
                                    <div class="box">
                                        <div class="program">
                                            <div class="boxdia">
                                                <p class="dia">Domingo</p>
                                                <ul>
                                                """ + doms + """
                                                </ul>
                                                <p class="dia">Segunda</p>
                                                <ul>
                                                """ + segs + """
                                                </ul>
                                                <p class="dia">Terça</p>
                                                <ul>
                                                """ + ters + """
                                                </ul>
                                                <p class="dia">Quarta</p>
                                                <ul>
                                                """ + quas + """
                                                </ul>
                                                <p class="dia">Quinta</p>
                                                <ul>
                                                """ + quis + """
                                                </ul>
                                                <p class="dia">Sexta</p>
                                                <ul>
                                                """ + sexs + """
                                                </ul>
                                                <p class="dia">Sábado</p>
                                                <ul>
                                                """ + sabs + """
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                """)

@app.route("/quemsomos", methods=['POST'])
def qmsomos():
    if request.method == 'POST':
        return render_template_string("""
                                        <div class="divmenu">
                                            <img onclick="MenuO()" id="MenuOpen" src="{{ url_for('static', filename='img/Menu.png') }}" alt="Menu">
                                            <div id="menu" class="menu">
                                                <a hx-post="/inicio" hx-target=".container">Início</a>
                                                <a id="ativado" hx-post="/quemsomos" hx-target=".container">Quem Somos</a>
                                                <a hx-post="/coordenacao" hx-target=".container">Coordenação</a>
                                                <a hx-post="/programacao" hx-target=".container">Programação</a>
                                                <a hx-post="/midia" hx-target=".container">Mídia</a>
                                                <a hx-post="/roteiro" hx-target=".container">Roteiro</a>
                                                <a hx-post="/locucao" hx-target=".container">Locução</a>
                                            </div>
                                        </div>
                                    """)

@app.route("/coordenacao", methods=['POST'])
def coordenacao():
    if request.method == 'POST':
        return render_template_string("""
                                        <div class="divmenu">
                                            <img onclick="MenuO()" id="MenuOpen" src="{{ url_for('static', filename='img/Menu.png') }}" alt="Menu">
                                            <div id="menu" class="menu">
                                                <a hx-post="/inicio" hx-target=".container">Início</a>
                                                <a hx-post="/quemsomos" hx-target=".container">Quem Somos</a>
                                                <a id="ativado" hx-post="/coordenacao" hx-target=".container">Coordenação</a>
                                                <a hx-post="/programacao" hx-target=".container">Programação</a>
                                                <a hx-post="/midia" hx-target=".container">Mídia</a>
                                                <a hx-post="/roteiro" hx-target=".container">Roteiro</a>
                                                <a hx-post="/locucao" hx-target=".container">Locução</a>
                                            </div>
                                        </div>
                                        <div class="box">
                                            <div class="divpessoas">
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Marla.jpg') }}" alt="Marla">
                                                    <p class="nomep">Marla</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Matheus.jpg') }}" alt="Matheus">
                                                    <p class="nomep">Matheus</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Italo.jpg') }}" alt="Italo">
                                                    <p class="nomep">Italo</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Camila.jpeg') }}" alt="Camila">
                                                    <p class="nomep">Camila</p>
                                                </div>
                                            </div>
                                        </div>
                                    """)
    
@app.route("/programacao", methods=['POST'])
def programacao():
    if request.method == 'POST':
        return render_template_string("""
                                        <div class="divmenu">
                                            <img onclick="MenuO()" id="MenuOpen" src="{{ url_for('static', filename='img/Menu.png') }}" alt="Menu">
                                            <div id="menu" class="menu">
                                                <a hx-post="/inicio" hx-target=".container">Início</a>
                                                <a hx-post="/quemsomos" hx-target=".container">Quem Somos</a>
                                                <a hx-post="/coordenacao" hx-target=".container">Coordenação</a>
                                                <a id="ativado" hx-post="/programacao" hx-target=".container">Programação</a>
                                                <a hx-post="/midia" hx-target=".container">Mídia</a>
                                                <a hx-post="/roteiro" hx-target=".container">Roteiro</a>
                                                <a hx-post="/locucao" hx-target=".container">Locução</a>
                                            </div>
                                        </div>
                                        <div class="box">
                                            <div class="divpessoas">
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Matheus.jpg') }}" alt="Matheus">
                                                    <p class="nomep">Matheus</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Italo.jpg') }}" alt="Italo">
                                                    <p class="nomep">Italo</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/LuizB.jpg') }}" alt="Luiz Bramé">
                                                    <p class="nomep">Luiz Bramé</p>
                                                </div>
                                            </div>
                                        </div>                               
                                    """)

@app.route("/midia", methods=['POST'])
def midia():
    if request.method == 'POST':
        return render_template_string("""
                                        <div class="divmenu">
                                            <img onclick="MenuO()" id="MenuOpen" src="{{ url_for('static', filename='img/Menu.png') }}" alt="Menu">
                                            <div id="menu" class="menu">
                                                <a hx-post="/inicio" hx-target=".container">Início</a>
                                                <a hx-post="/quemsomos" hx-target=".container">Quem Somos</a>
                                                <a hx-post="/coordenacao" hx-target=".container">Coordenação</a>
                                                <a hx-post="/programacao" hx-target=".container">Programação</a>
                                                <a id="ativado" hx-post="/midia" hx-target=".container">Mídia</a>
                                                <a hx-post="/roteiro" hx-target=".container">Roteiro</a>
                                                <a hx-post="/locucao" hx-target=".container">Locução</a>
                                            </div>
                                        </div>
                                        <div class="box">
                                            <div class="divpessoas">
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Camila.jpeg') }}" alt="Camila">
                                                    <p class="nomep">Camila</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Lucas.jpg') }}" alt="Lucas">
                                                    <p class="nomep">Lucas</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Alicya.jpg') }}" alt="Alicya">
                                                    <p class="nomep">Alicya</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Letícia.jpg') }}" alt="Letícia">
                                                    <p class="nomep">Letícia</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Isabel.jpg') }}" alt="Isabel">
                                                    <p class="nomep">Isabel</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Emanuelly.jpg') }}" alt="Emanuelly">
                                                    <p class="nomep">Emanuelly</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Gaby.jpg') }}" alt="Gaby">
                                                    <p class="nomep">Gaby</p>
                                                </div>
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Emillyana.jpeg') }}" alt="Emillyana">
                                                    <p class="nomep">Emillyana</p>
                                                </div>
                                      <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/luis.jpg') }}" alt="Luis Gustavo">
                                                    <p class="nomep">Luis Gustavo</p>
                                                </div>
                                            </div>
                                        </div> 
                                    """)
    
@app.route("/roteiro", methods=['POST'])
def roteiro():
    if request.method == 'POST':
        return render_template_string("""
                                        <div class="divmenu">
                                            <img onclick="MenuO()" id="MenuOpen" src="{{ url_for('static', filename='img/Menu.png') }}" alt="Menu">
                                            <div id="menu" class="menu">
                                                <a hx-post="/inicio" hx-target=".container">Início</a>
                                                <a hx-post="/quemsomos" hx-target=".container">Quem Somos</a>
                                                <a hx-post="/coordenacao" hx-target=".container">Coordenação</a>
                                                <a hx-post="/programacao" hx-target=".container">Programação</a>
                                                <a hx-post="/midia" hx-target=".container">Mídia</a>
                                                <a id="ativado" hx-post="/roteiro" hx-target=".container">Roteiro</a>
                                                <a hx-post="/locucao" hx-target=".container">Locução</a>
                                            </div>
                                        </div>
                                        <div class="box">
                                            <div class="divpessoas">
                                      <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Alicya.jpg') }}" alt="Alycia">
                                                    <p class="nomep">Alicya</p>
                                                </div>
                                       <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/nicolly.jpg') }}" alt="Nicolly">
                                                    <p class="nomep">Nicolly</p>
                                                </div>
                                       <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Letícia.jpg') }}" alt="Letícia">
                                                    <p class="nomep">Letícia</p>
                                                </div>
                                       <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Lucas.jpg') }}" alt="Lucas">
                                                    <p class="nomep">Lucas</p>
                                                </div>
                                            </div>
                                        </div> 
                                    """)
@app.route("/locucao", methods=['POST'])
def locucao():
    if request.method == 'POST':
        return render_template_string("""
                                        <div class="divmenu">
                                            <img onclick="MenuO()" id="MenuOpen" src="{{ url_for('static', filename='img/Menu.png') }}" alt="Menu">
                                            <div id="menu" class="menu">
                                                <a hx-post="/inicio" hx-target=".container">Início</a>
                                                <a hx-post="/quemsomos" hx-target=".container">Quem Somos</a>
                                                <a hx-post="/coordenacao" hx-target=".container">Coordenação</a>
                                                <a hx-post="/programacao" hx-target=".container">Programação</a>
                                                <a hx-post="/midia" hx-target=".container">Mídia</a>
                                                <a hx-post="/roteiro" hx-target=".container">Roteiro</a>
                                                <a id="ativado" hx-post="/locucao" hx-target=".container">Locução</a>
                                            </div>
                                        </div>
                                        <div class="box">
                                            <div class="divpessoas">
                                                <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Italo.jpg') }}" alt="Italo">
                                                    <p class="nomep">Italo</p>
                                                </div>
                                       <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Emillyana.jpeg') }}" alt="Emillyana">
                                                    <p class="nomep">Emillyana</p>
                                                </div>
                                       <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Emanuelly.jpg') }}" alt="Emanuelly">
                                                    <p class="nomep">Emanuelly</p>
                                                </div>
                                       <div class="p">
                                                    <img class="imgp" src="{{ url_for('static', filename='img/SelfieRadio/Camila.jpeg') }}" alt="Camila">
                                                    <p class="nomep">Camila</p>
                                                </div>
                                            </div>
                                        </div>            
                                    """)
 
  
  
  
  
if __name__ == "__main__":
    app.run(host="10.136.123.218", port="5000")
