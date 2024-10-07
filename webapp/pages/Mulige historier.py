import streamlit as st
import uuid
from datetime import datetime
from config import set_pandas_options, set_streamlit_options
from utils.data_processing import load_css, write_markdown_sidebar

# Apply the settings
set_pandas_options()
set_streamlit_options()

load_css("webapp/style.css")

# Generate or retrieve session ID
if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())  # Generate a unique ID

# Get the current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log the user session with a print statement
user_id = st.session_state["user_id"]
print(f"[{timestamp}] New user session: {user_id} (Mulige historier)")

st.logo("webapp/images/GC_png_oneline_lockup_Outline_Blaa_RGB.png")

with st.sidebar:
    write_markdown_sidebar()

# Side-titel
st.header("Mulige historier")

# Overordnede afsnit
st.markdown(
    """
            Her kan du få inspiration til, hvilke vinkler og historier, du kan lave med baggrund i det data, du finder her på siden. \n
Databasen kortlægger alle de investeringer i værdipapirer, som kommuner og regioner havde i sommeren 2024. \n
På forsiden kan du eksempelvis søge på en kommune og se, hvilke værdipapirer kommunen har investeret i samt om der skulle være nogle problematiske værdipapirer imellem. \n
Altså om en dansk bank, pensionsselskab eller FN har udpeget værdipapiret som problematisk og sat det på en såkaldt eksklusionsliste. \n

I det følgende finder du en liste over mulige historier, der kunne laves på baggrund af data:\n
"""
)

with st.expander("**Kommuner og regioner har investeringer for 68,5 milliarder**"):
    st.write(
        """
        Kommunerne og regioner har oplyst til Gravercentret og Danwatch, at de samlet set har 140.954 værdipapirer til en samlet værdi af 68,5 mia. kroner. Der er kun to kommuner – Læsø og Samsø, der ikke har investeret i værdipapirer.\n
        Midlerne er typisk sat i obligationer (51,2 mia.), men en stor andel er også sat i aktier (10,7 mia.). 
        Derudover er 924 mio. investeret i virksomhedsobligationer, der er udstedt af firmaer og i bund og grund minder meget om aktier. 
        Endelig er der investeringer for 5,6 mia., hvor investeringskategorien typisk ikke er blevet oplyst.\n
        """
    )

with st.expander("**Kommuner og regioner har penge i 6.162 problematiske værdipapirer**"):
    st.write(
        """
        Landets kommuner og regioner har investeret i mere end 6.000 værdipapirer, der er udpeget som problematiske af enten danske banker, pensionsselskaber eller FN. Helt præcist er der tale om 6.162 værdipapirer. Dertil kommer 1.419 værdipapirer som Gravercentret vurderer potentielt kan være kontroversielle, selv om de ikke er decideret sortlistet.\n
        I alt har 81 kommuner og regioner investeret 456 millioner kroner i problematiske aktier.\n
        Kalundborg Kommune er topscoreren med hele 631 værdipapirer, der er udpeget som problematiske, mens Rødovre Kommune har 358 problematiske værdipapirer og Fanø har 354.\n
        Beløbsmæssigt er det ikke overraskende de tre store kommuner, der har flest midler placeret i problematiske aktier. København har 287,3 millioner i problematiske aktier, Odense Kommune har 30,8 millioner og Århus har 29,8 millioner.
        """
    )

with st.expander(
    "**Kommuner har penge i firmaer med aktiviteter i besatte områder på Vestbredden**"
):
    st.write(
        """
        62 kommuner og regioner investerer i selskaber på FN's sortliste over firmaer med aktiviteter i besatte områder på Vestbredden. I alt er der investeret for 17 millioner kroner.\n
        Guldborgsund Kommuner har flest af disse værdipapirer – 16 i alt, mens Rødovre har 15 og Mariagerfjord, Høje Taastrup og Aabenraa alle har 11 investeringer.\n
        Beløbsmæssigt er det Odense med 3,4 millioner samlet og Region Nordjylland med 1,9 millioner samlet, der er topscorerne.
        """
    )

with st.expander("**Kommuner med sundhedspolitik investerer i sodavand og fastfood**"):
    st.write(
        """
        Alle kommuner har vedtaget udførlige sundhedspolitikker, hvis mål det er, at få borgerne til at leve så sundt som muligt. Men samtidig med, at børnene ikke må have pålægschokolademadder med i madpakkerne og visionen i praktisk talt alle kommuner og regioner er, at borgerne skal være mere sunde, så investeres der på livet løs i usunde fødevarer.\n
        Det kan også undre, at regionerne, der skal behandle syge danskere, vælger at investere i usunde fødevarer.\n
        Investeringer i Coca-cola forekommer i 75 kommuner og regioner for i alt 36,9 millioner kroner. Odense Kommune har sat flest penge i selskabet med 3,8 millioner kroner, mens Københavns Kommune har investeret 2,6 millioner i Coca-cola.\n
        Konkurrenten Pepsi har 71 kommuner og regioner investeret samlet 25,9 millioner kroner i. Igen har Odense sat flest penge i selskabet med 2,8 millioner kroner, mens Region Sjælland har investeret 2,1 millioner.\n
        McDonald’s har 44 kommuner og regioner købt sig ind i og her har Region Sjælland investeret mest – nemlig 2,6 millioner kroner, mens Køge Kommune er på andenpladsen med 1,7 millioner kroner. I alt er der investeret for 13,9 millioner kroner.\n
        Disse investeringer kan anses som problematiske idet kommunerne og især regionerne har et ansvar for befolkningens sundhed. Samtidig at tjene på salg af usunde fødevarer kan betragtes som dobbeltmoralsk.
        """
    )

with st.expander("**Kommuner har sat penge i sortlistede lande**"):
    st.write(
        """
        22 kommuner og regioner har investeringer i statsobligationer fra såkaldt kontroversielle stater. Det er lande, som eksempelvis Saudi Arabien, Kina, Pakistan, Venezuela og Qatar, som er sat på eksklusionslisten af danske banker eller pensionsselskaber. I tabellen på forsiden er disse investeringer markeret med orange og i kollonnen "Eksklusion (Af hvem og hvorfor)" kan du se, hvorfor de enkelte banker og pensionsselskaber har udelukket investeringer i de pågældende lande. I alt har kommuner og regioner 837 værdipapirer af denne type til en samlet værdi af 25,6 millioner kroner.\n
        Region Nordjylland har investeret 6,9 millioner i disse sortlistede statsobligationer, mens Ringkøbing-Skjern har investeret 6,3 millioner.
        """
    )

with st.expander("**Kommuner og regioner investerer millioner i krydstogtsselskaber**"):
    st.write(
        """
        44 kommuner og regioner har aktier i f.eks. Carnival Corp og Royal Caribbean, der driver krydstogtsturisme. De har et dårligt ry for at skabe masseturisme og skabe negative effekter i europæiske storbyer. Senest har krydstogtturismen også været under beskydning for at være en klima- og miljøbelastning.\n
        Der er samlet investeret for 12,1 millioner kroner. Flest penge har Region Hovedstaden og Region Sjælland sat i krydstogtsselskaber med investeringer på henholdsvis 2,6 millioner kroner og 1,5 millioner kroner.
        """
    )

with st.expander("**Kommuner har penge i Blackstone**"):
    st.write(
        """
        31 kommuner og regioner er små "medejere" af kapitalfonden og boligspekulanten Blackstone, der er blevet kritiseret skarpt for at opkøbe ejendomme og lejligheder i større danske byer, istandsætte dem og sætte lejen kraftigt op.\n
        Samlet er der investeret for 1,5 millioner kroner. Paradoksalt nok er Aarhus Kommune topscoreren her med en samlet investering på 333.000 kroner, mens Esbjerg har investeret 170.000 kroner.
        """
    )

with st.expander("**Kommuner investerer i selskaber med ringe rettigheder for medarbejderne**"):
    st.write(
        """
        Firmaer som amerikanske Walmart og Amazon er nogle af de selskaber, som har et dårligt omdømme med hensyn til deres medarbejderes rettigheder og derfor er sortlistet af nogle banker og pensionsselskaber.\n
        Det forhindrer dog ikke en lang række kommuner og regioner i at investere i dem.\n
        75 kommuner og regioner har denne type investeringer. Beløbsmæssigt er det Frederiksberg Kommune med 14,1 millioner kroner i disse selskaber, der har flest, mens Aarhus Kommune har investeret 11,8 millioner.\n
        I tabellen på [forsiden](/Forside) er denne type problematiske investeringer beskrevet som "arbejdstagerrettigheder" i søgefeltet "Vælg problemkategori" i venstre side.
        """
    )

with st.expander(
    "**Kommuner investerer i værdipapirer, der sammenkædes med brud på menneskerettighederne**"
):
    st.write(
        """
        63 kommuner og regioner har investeret samlet 149,6 millioner kroner i værdipapirer, der er udpeget til at være problematiske på grund af overtrædelser af menneskerettigheder.\n
        Her har Aarhus Kommune investeret mest med 2 millioner kroner, mens Københavns Kommune har investeret 1,9 millioner.\n
        I tabellen på [forsiden](/Forside) er denne type problematiske investeringer beskrevet som "menneskerettigheder" i søgefeltet "Vælg problemkategori" i venstre side.
        """
    )

with st.expander("**Regioner og kommuner har aktier i flyselskaber**"):
    st.write(
        """
        Kommunerne og regioner er tilsyneladende ikke ramt af flyskam. Flyselskaber som American Airlines, Emirates, Southwest Airlines, China Southern Airlines, China Airlines, Ryanair m.fl. kan betragtes som en uhensigtsmæssig og klima-uvenlig investering, men 65 kommuner og regioner har penge netop i flyselskaber.\n
        I alt er der investeret 6,4 millioner kroner. Region Hovedstaden har investeret 1 million kroner i flyselskaber og Region Nordjylland har investeret 606.000 kroner.
        """
    )

with st.expander("**Regioner investerer i medicinalfirmaer**"):
    st.write(
        """
        Det kan udgøre en interessekonflikt, når regionerne investerer i medicinalselskaber som eksempelvis Novo Nordisk, fordi regionerne samtidig driver sygehuse og er storkunder i medicinalindustrien. Alligevel investerer regionerne i et stort antal medicinalfirmaer. Disse er dog ikke markeret i vores base og man skal selv løbe listerne igennem for at finde dem. Eksempelvis ved at søge på virksomhedsnavne som Novo Nordisk i tabellen på forsiden i venstre sides fritekstsøgefelt.\n
        F.eks. har Region Sjælland investeret 6 millioner i Novo Nordisk.
        """
    )

with st.expander("**Kommuner investerer millioner i fossile brændstoffer**"):
    st.write(
        """
        Man skulle tro, at kommuner og regioner med deres grønne profiler ikke ville røre selskaber, der beskæftigede sig med fossile brændstoffer – hvilket de har fået kritik for før - men 78 kommuner og regioner har fortsat investeringer i branchen for samlet 50,9 millioner kroner.\n
        Odense Kommune har investeringer for 4,3 millioner kroner i denne kategori og Region Sjælland har for 3,2 millioner kroner.\n
        Det er også værd at bemærke, at Kalundborg Kommune har intet mindre end 208 forskellige værdipapirer for samlet 1,1 millioner kroner i selskaber, der beskæftiger sig med fossile brændstoffer.\n
        Undersøg, hvordan det står til i de kommuner, du dækker, på [forsiden](/Forside) ved at vælge "fossile brændstoffer" som problemkategori i venstre side. 
        """
    )

with st.expander("**Kommuner investerer i atomvåben**"):
    st.write(
        """
        76 kommuner og regioner har investeret i såkaldt kontroversielle våben - herunder atomvåben og klyngebomber. Samlet set er der investeret for 102,2 millioner kroner, men hovedparten står Københavns Kommune for. Her har man investeret 76,7 millioner i kontroversielle våben, mens Odense Kommune har investeret 4 millioner.\n
        Hvis du gerne vil kigge nærmere på, hvilke kommuner og regioner, der har investeret i våben, kan du på [forsiden](/Forside) vælge "kontroversielle våben" som problemkategori i venstre side. Du kan også vælge "våben og militær" i samme menu, for at se på, hvor meget kommuner og regioner har investeret i våben og militær, som ikke er på den kontroversielle liste over våben.\n
        """
    )

with st.expander("**Kommuner sætter penge i firmaer, der sælger alkohol**"):
    st.write(
        """
        Selv om kommunerne både skal forebygge og behandle misbrug af alkohol, investerer 10 af dem i firmaer, der producerer og markedsfører alkohol. Bl.a Rødovre kommune har en del af disse investeringer – de har aktier i 18 forskellige alkoholselskaber.\n
        Flest penge har Herning Kommune investeret med 483.000 kroner og Vejen Kommune med 393.000 kroner.\n
        Se om de kommuner, du dækker, har sat penge i selskaber, der producerer og markedsfører alkohol, på [forsiden](/Forside) ved at vælge "alkohol" som problemkategori i kollonen til venstre.

        """
    )

with st.expander("**Kommuner investerer i casinoer og gambling**"):
    st.write(
        """
        Man skulle ikke tro det, men 45 kommuner og regioner har investeret 1,9 millioner samlet i selskaber, der beskæftiger sig med gambling, casinoer og pengespil selv om ludomani er et samfundsproblem. Aarhus Kommune har investeret 318.000 kroner i pengespil og Furesø Kommune har investeret 297.000 kroner.\n
        Kalundborg har satset på flest heste – de har investeret småbeløb i 21 forskellige gamblingfirmaer.\n
        Undersøg, hvordan det står til i de kommuner, du dækker, på [forsiden](/Forside) ved at vælge "gambling" som problemkategori i venstre side. 
        """
    )

# Footer
st.markdown(
    """##### Videre research:
Der kan være flere kontroversielle værdipapirer blandt de omkring 140.000 investeringer, som kommunerne og regioner har foretaget. \n
Hvis man vil dykke længere ned i materialet kan man få hjælp fra disse NGO-lister over kontroversielle selskaber indenfor forskellige kategorier:\n
- [Olie- og gassektoren](https://gogel.org/)
- [Kulsektoren](https://www.coalexit.org/)
- [Største banker, der finansierer den fossile sektor](https://www.bankingonclimatechaos.org/)
- [Israel-Palæstina konflikten](https://www.whoprofits.org/)
- [Våben](https://www.sipri.org/databases/armsindustry)
- [Menneskerettigheder](https://www.business-humanrights.org/en/companies/)

"""
)
