import streamlit as st

def CalcoloCoefficiente(commissione,iva,cedolare):
    return 1 - (commissione + (commissione * iva)) - cedolare


st.title("CALCOLATORE TARIFFE AIRBNB - CSL")
st.write("V1.01")
st.divider()

colUno, colDue = st.columns([1,1])

with colUno:

    numeroNotti = st.number_input("Numero Notti", min_value=1,value=1,step=1, max_value=30)

    #colPulizie, colCheck = st.columns([3,2])

    #with colCheck:
    attivaPulizie = st.checkbox("Attiva Pulizie", value=False)

    #with colPulizie:
    costoPulizie = st.number_input("Costo Pulizie", min_value=0.0, value=15.0, step=0.5, disabled=not attivaPulizie)   
    pulizie = costoPulizie if attivaPulizie else 0

    st.write(f"Spesa pulizie per giorno: {pulizie:.2f}€")

with colDue:    

    nettoVoluto = st.number_input("Inserisci il netto desiderato", min_value=25.0, value=50.0, step=0.5)

    cedolareSeccaPerc = st.selectbox("Seleziona la percentuale della cedolare secca", options=[0.21, 0.26, 0.30], index=0, format_func=lambda x: f"{x*100:.0f}%")

    ivaPercentuale = st.selectbox("Seleziona la percentuale dell'IVA", options=[0.20, 0.22, 0.25], index=1, format_func=lambda x: f"{x*100:.0f}%")

st.divider()

col1, col2 = st.columns([1,1])

with col1:

    st.subheader("NUOVO CALCOLO")

    commissionePercentualeNuova = 0.155
    st.write(f"Nuove commissioni {commissionePercentualeNuova*100:.2f}%")

    #st.metric(label="Nuova Commissione", value=f"{commissionePercentualeNuova*100:.2f}%")

    coefficiente = CalcoloCoefficiente(commissionePercentualeNuova,ivaPercentuale,cedolareSeccaPerc)

    lordoCalcolato = ((nettoVoluto) * numeroNotti / (coefficiente))
    st.metric(label="Lordo Nuovo", value=f"€ {lordoCalcolato:.2f}", border= True)

    commissioneAirBnb = lordoCalcolato * commissionePercentualeNuova
    ivaCommissione = commissioneAirBnb * ivaPercentuale
    cedolareSecca = lordoCalcolato * (cedolareSeccaPerc)
    nettoVerificato = lordoCalcolato - commissioneAirBnb - ivaCommissione - cedolareSecca - pulizie

    st.metric(label="Tot. Netto", value=f"€ {nettoVerificato:.2f}", border=True)

    st.write(f"Netto Notte: € {nettoVerificato / numeroNotti:.2f}")
    
    st.write(f"Commissione AirBnb: {commissioneAirBnb:.2f}€")
    
    st.write(f"IVA sulla commissione: {ivaCommissione:.2f}€")
    
    st.write(f"Cedolare secca: {cedolareSecca:.2f}€")

with col2:
    st.subheader("VECCIO CALCOLO")

    commissionePercentualeVecchia = 0.03
    st.write(f"Vecchie Commissioni {commissionePercentualeVecchia*100:.2f}%")
    #st.metric(label="Vecchia commissione", value=f"{commissionePercentualeVecchia*100:.2f}%")

    coefficienteVecchio = CalcoloCoefficiente(commissionePercentualeVecchia,ivaPercentuale,cedolareSeccaPerc)

    lordoCalcolatoVecchio = (nettoVoluto) * numeroNotti / (coefficienteVecchio)
    st.metric(label="Lordo vecchio",  value=f"€ {lordoCalcolatoVecchio:.2f}", border= True)

    commissioneAirBnbVecchio = lordoCalcolatoVecchio * 0.03

    ivaCommissioneVecchio = commissioneAirBnbVecchio * ivaPercentuale

    cedolareSeccaVecchio = lordoCalcolatoVecchio * (cedolareSeccaPerc)

    nettoVerificatoVecchio = lordoCalcolatoVecchio - commissioneAirBnbVecchio - ivaCommissioneVecchio - cedolareSeccaVecchio - pulizie
    st.metric(label="Tot. Netto [Vecchio]", value=f"€ {nettoVerificatoVecchio:.2f}", border=True)
    st.write(f"Netto Notte (vecchio): € {nettoVerificatoVecchio / numeroNotti:.2f}")

    commissioniGuestVecchiemin = 0.141
    commissioniGuestVecchiemax = 0.165

    prezzoEspostoGuestmin = lordoCalcolatoVecchio * (1 + commissioniGuestVecchiemin)
    prezzoEspostoGuestmax = lordoCalcolatoVecchio * (1 + commissioniGuestVecchiemax)

    st.write(f"Prezzo esposto al guest variava da un minimo di {prezzoEspostoGuestmin:.2f}€ con commissioni del {(commissioniGuestVecchiemin * 100):.1f}%")
    st.write(f"a un massimo di {prezzoEspostoGuestmax:.2f}€ con commissioni del {(commissioniGuestVecchiemax * 100):.1f}%")
    st.write(f"Commissione AirBnb (vecchio): {commissioneAirBnbVecchio:.2f}€")
    st.write(f"IVA sulla commissione (vecchio): {ivaCommissioneVecchio:.2f}€")
    st.write(f"Cedolare secca (vecchio): {cedolareSeccaVecchio:.2f}€")