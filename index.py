import streamlit as st

# Configurações da página
st.set_page_config(page_title="Meu Portfólio", page_icon=":briefcase:", layout="wide")

# Foto e cabeçalho principal
st.sidebar.image("foto.jpg", width=150)
st.sidebar.title("Navegação")
selecao = st.sidebar.radio("Ir para:", [
    "Resumo das Qualificações", 
    "Experiência Profissional", 
    "Educação", 
    "Habilidades Técnicas", 
    "Projetos e Realizações", 
    "Idiomas", 
    "Cursos e Treinamentos", 
    "Referências Profissionais", 
    "Contato", 
    "Portfólio de Projetos"
])

st.title("Meu Portfólio")

# Seção "Resumo das Qualificações"
if selecao == "Resumo das Qualificações":
    st.header("Resumo das Qualificações")
    st.write("""
    Profissional experiente em tecnologia da informação com 30 anos de carreira. Atuo como instrutor, desenvolvedor de sistemas, analista, gestor de infraestrutura e gerente de projetos. Fundou sua própria empresa e possui vasta experiência em diferentes portes e segmentos de mercado. Atualmente, ministra cursos de formação profissional em instituição renomada.

    Habilidades e experiências:

    * Ampla vivência em desenvolvimento de sistemas, incluindo análise, programação e implementação.
    * Sólida experiência em gestão de projetos e infraestrutura de TI.
    * Capacidade de liderança e trabalho em equipe.
    * Habilidades de comunicação e ensino eficazes.
    * Experiência em diversos setores, incluindo educação, saúde e odontologia.
    """)

# Seção "Experiência Profissional"
elif selecao == "Experiência Profissional":
    st.header("Experiência Profissional")
    st.write("""
    - SENAI - Serviço Nacional de Aprendizagem Industrial
        - Instrutor de Formação Profissional
        - junho de 2022 - Present (2 anos 6 meses)
        - Araraquara, São Paulo, Brasil
    
    - FI Sistemas
        - Programador
        - junho de 2019 - agosto de 2022 (3 anos 3 meses)
        - Araraquara
        - Desenvolvimento de sistema para Cooperativas Odontológicas utilizando linguagem Delphi e banco de dados Firebird
    """)

# Seção "Educação"
elif selecao == "Educação":
    st.header("Educação")
    st.write("""
    - Mestrado em Ciência da Computação - Universidade Z (2019)
    - Bacharelado em Engenharia de Software - Universidade Y (2015)
    """)

# Seção "Habilidades Técnicas"
elif selecao == "Habilidades Técnicas":
    st.header("Habilidades Técnicas")
    st.write("""
    - Linguagens: Python, JavaScript, SQL
    - Frameworks: Flask, Django, Streamlit
    - Ferramentas de Análise: Pandas, NumPy, Scikit-learn
    - Visualização de Dados: Power BI, Matplotlib, Seaborn
    """)

# Seção "Projetos e Realizações"
elif selecao == "Projetos e Realizações":
    st.header("Projetos e Realizações")
    st.write("""
    - Sistema de Recomendação para E-commerce
    - Dashboard Interativo para Análise de Dados do Mercado
    - Modelo de IA para Detecção de Anomalias em Produção
    """)

# Seção "Idiomas"
elif selecao == "Idiomas":
    st.header("Idiomas")
    st.write("""
    - Português: Nativo
    - Inglês: Fluente
    - Espanhol: Intermediário
    """)

# Seção "Cursos e Treinamentos"
elif selecao == "Cursos e Treinamentos":
    st.header("Cursos e Treinamentos")
    st.write("""
    - Certificação em Ciência de Dados (Coursera, 2021)
    - Curso de Machine Learning Avançado (DataCamp, 2020)
    """)

# Seção "Referências Profissionais"
elif selecao == "Referências Profissionais":
    st.header("Referências Profissionais")
    st.write("""
    - João Silva, Gerente de Desenvolvimento, Empresa XYZ (joao.silva@exemplo.com)
    - Maria Oliveira, Cientista de Dados Sênior, Empresa ABC (maria.oliveira@exemplo.com)
    """)

# Seção "Contato"
elif selecao == "Contato":
    st.header("Contato")
    st.write("""
    - **E-mail:** seuemail@exemplo.com
    - **LinkedIn:** [linkedin.com/in/seu-perfil](https://www.linkedin.com/in/seu-perfil)
    - **GitHub:** [github.com/seu-usuario](https://github.com/seu-usuario)
    - **Site:** [seu-portfolio.com](https://seu-portfolio.com)
    """)

# Seção "Portfólio de Projetos"
elif selecao == "Portfólio de Projetos":
    st.header("Portfólio de Projetos")

    st.subheader("Projeto 1: Análise de Dados")
    st.write("""
    Descrição: Uma análise de dados para prever tendências de mercado.
    [GitHub](https://github.com/seu-usuario/projeto1) | [Demo](https://demo-do-projeto.com)
    """)

    st.subheader("Projeto 2: Sistema de Recomendação")
    st.write("""
    Descrição: Um sistema de recomendação para produtos personalizados.
    [GitHub](https://github.com/seu-usuario/projeto2) | [Demo](https://demo-do-projeto2.com)
    """)

    st.subheader("Projeto 3: Classificador de Imagens")
    st.write("""
    Descrição: Modelo de IA para classificar imagens.
    [GitHub](https://github.com/seu-usuario/projeto3) | [Demo](https://demo-do-projeto3.com)
    """)

# Rodapé
st.write("Obrigado por visitar meu portfólio! :)")
