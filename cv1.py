import streamlit as st

st.info("PROFIL")
st.text("Téchnicien supérieur en Géomatique,motivé,déterminé et avec une bonne capacité physique et mentale.Je travaille toujours avec rigueur et munitie pour un résultat à la hauteur des attentes fixées.Grace à ma capacité d'adaptation et à mon ouverture d'esptit,j'assimile avec serieux et détermination l'objectif à atteindre.")

st.info("PARCOURS ACADEMIQUE")
st.markdown("""
* Licence en Géographie 2026          
* Brevet de Téchnicien Supérieur en Géomatique 2026
* Baccalaureat Sciences Humaines et Sociales 2023
""")

st.divider()
st.info("EXPERIENCE PERSONNELLE")
st.text("Pratique continue du sport pendant 13ans en parellèle d'un parcours academique.\n" \
"Cette double implication m'a permis de develloper une forte discipline ,une excelente gestion du temps et une grande capacite à travaller sous pression. ")
st.text("Cette experience m'a permis de forger un profil équilibrer,dynamique et orienté vers la performance.")

st.divider()
st.info("SPORT")
st.markdown("""
* Maitre de Dojo            
* Ceinture Noire 2e Duan-Kungfu Wushu 2024
* Ceinture Noire 1ere Duan-kungfu Wushu 2022
* Ceinture Rouge superieure-Kungfu Wushu 2020
* Plusieurs fois Champion du Sénégal
            """)

with st.sidebar:
    st.subheader("MOHAMED MOUNTABA DIALLO")
    st.markdown("""
* 📍Citee Lycee-Joal
* ✉️diallomohamed922@gmail.com
                """)
    st.success(""" LANGUE
* Anglais
                 """)
            
    st.divider()
    st.success("COMPETENCES")
with st.col1:
    st.write("Bonne maitrise des logiciels d'architecture(Autocad,SketchUp)")
    st.write("Bonne maitrise des logiciels cartographique(Arcgis,QGiS)")
    st.write("Capacite d'adaptation")
    st.write("Ouverture d'esprit")
with st.col2:
    st.write("Methodique")
    st.write("Proactif")
    st.write("Social")
    st.write("Bonne capacité d'analyse et d'interprétation des résultats expérimentaux")
    st.write("Bonne connaissances culturelle et littéraire")
    st.write("Bonne capacité à analyser les pensees et les affaires humaines,les critiquer et realiser des discours autour de ces sujets")
    
