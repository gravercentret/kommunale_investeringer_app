import streamlit as st
from config import set_pandas_options, set_streamlit_options
from utils.data_processing import load_css, write_markdown_sidebar, create_user_session_log

# Apply the settings
set_pandas_options()
set_streamlit_options()

load_css("webapp/style.css")

create_user_session_log("Publicerede artikler")

st.logo("webapp/images/GC_png_oneline_lockup_Outline_Blaa_RGB.png")

with st.sidebar:
    write_markdown_sidebar()

# Side-titel
st.header("Eksempler på publiceret journalistik")

# Overordnede afsnit
st.markdown(
    """
På denne side vil vi samle nogle eksempler på journalistiske historier, som er blevet til på baggrund af data her fra sitet. \n
"""
)

with st.expander("**Danwatch: Kommuner investerer millioner i sortlistede virksomheder**", expanded=True):
    st.write(
        """
### Kommuner investerer millioner i sortlistede virksomheder
#### Atomvåben, oliegiganter, mineselskaber, besat land og gambling er blandt kommunernes investeringer, der også havner i statsobligationer fra skattelylande og regimer, der ikke lever op til menneskerettigheder.

*Udgivet d. 21. oktober 2024 kl. 00.01*\n
*Joachim Kattrup, Lasse Egeris og Charlotte Aagaard*

Trods høje ambitioner om bæredygtighed, klimaindsats og social ansvarlighed har danske kommuner investeret millioner af skatteborgernes penge i lande og virksomheder, der udvinder fossile brændstoffer, krænker menneskerettigheder, er i skattely og mange andre alvorlige problematikker. \n
Det afslører en helt ny database over kommunale investeringer i mere end 140.000 værdipapirer for i alt 66,7 milliarder kroner. \n
Danwatch har i samarbejde med Gravercentret - Danmarks Center for Undersøgende Journalistisk – undersøgt alle 98 kommuner og 5 regioners investeringer. Kortlægningen er den første af sin art nogensinde. \n
414 millioner kommunale kroner er placeret i 5.133 værdipapirer udstedt af selskaber eller lande, som danske pensionskasser ikke vil investere i af forskellige etiske årsager og derfor har sat på en sortliste over problematiske investeringer.\n
Kortlægningen afslører kommunale investeringer fordelt på mere end 20 "problem-kategorier”, som bl.a. tæller klima, våben, menneskerettigheder, Rusland, tobak, skattely, fossile brændsler, gambling og usunde fødevarer.\n
Kortlægningen afslører meget store forskelle i kommunernes etiske hensyn i deres finansielle investeringer.\n
For eksempel har København investeret i kun elleve problematiske selskaber, imens man på Kalundborgs investerings liste finder 286 værdipapirer fordelt på mere end 70 selskaber, som er ekskluderet af danske pensionskasser.\n
Danwatch har forelagt resultaterne for professor i økonomistyring, Per Nikolaj Bukh fra Aalborg Universitet.  \n
“Forskellene i hvilke af de potentielt problematiske investeringer, som kommunerne har, kan i høj grad forklares med, hvilke forvaltere kommunerne har hyret.  Forvalterne har forskellige tilbud om ESG-screenede (bæredygtighedsindsatser, red.) fonde og dermed også på hvilke selskaber, som man investerer i”, siger Per Nikolaj Bukh.\n

##### Verdens største olieselskaber
Danske kommuner har investeret betydelige beløb i nogle af verdens mest forurenende olieselskaber, herunder TotalEnergies, Shell, Chevron og Aramco. \n
Men det stopper ikke ved det. Også statskontrollerede fossile giganter som mexicanske Pemex, brasilianske Petrobras og Kasakhstanske KazMunayGas er blandt kommunernes investeringer. \n
Disse fossile selskaber er kendt for deres massive CO2-udledninger og fortsatte satsning på udvikling af fossile brændstoffer.\n

##### Investeringer i ulovlige bosættelser
Ud over olieselskaber investerer danske kommuner også i virksomheder, der er involveret i aktiviteter i de besatte palæstinensiske områder. Det kan være i strid med FN, ifølge en vurdering fra Den Internationale Domstol (ICJ).  ICJ konkluderer, at Israels fortsatte tilstedeværelse i disse områder er ulovlig ifølge international lov.\n
Eksempler inkluderer flere israelske banker og internationale rejsebureauer som TripAdvisor og Booking.com. De står på FN´s liste over virksomheder, der er involveret i aktiviteter i israelske besatte områder. Mange på listen har danske kommuner i ejerkredsen.  \n
Og selv om kommunerne hyrer forvaltere, som investerer deres penge, så har den enkelte kommune også et stort ansvar for at sikre, at borgernes penge ikke ender i problematiske aktiviteter og virksomheder. Det vurderer uafhængig ESG-rådgiver og tidligere chef for bæredygtige investeringer i Nykredit, Søren Larsen.\n
“Investor skal have afklaret, at selskabet ikke modarbejder FN's afgørelser og i øvrigt respekterer menneskerettighederne.  Det kan være svært at afgøre i de konkrete tilfælde.  Men det skal afklares, hvis investeringen skal være i overensstemmelse med FN”, siger Søren Larsen. \n
Kortlægningen viser også, at landets store kommuner har flest penge investeret i kontroversielle selskaber, fordi de også har de største økonomier. \n
Men de problematiske investeringer i de store kommuner er fordelt på færre selskaber end mange af landets mindre kommuner.  \n
"Generelt så indikerer investering i få kontroversielle selskaber, at investor har en systematisk tilgang til at undgå disse blandt de mange tusinde aktieselskaber, der handles på verdens børser”, vurderer Søren Larsen, der har rådgivet både store private og offentlige investorer.\n
København skiller sig ud ved kun at have investeret i få problematiske virksomheder.\n
"Det er ret vigtigt at formulere en ansvarlig investeringspolitik og sikre, at man har en aftale med en forvalter, som kan gennemføre politikken. Derefter skal kommunerne som alle andre investorer sikre sig, at politikken faktisk bliver ført ud i livet, siger Søren Larsen.\n
Som den eneste af landets kommuner har København etableret sin egen investeringsforening. Det sikre, at forvalterne handler ud fra de kriterier som kommunen fastsætter.\n
“Det er et politisk ønske, at midlerne bliver investeret på en ansvarlig måde. Det indebærer , at kommunen ikke ønsker at investere i selskaber, der ikke tager ansvar for miljø, menneskerettigheder og arbejdstagerrettigheder m.v. på niveau med anerkendte, internationale regler og normer”, oplyser Københavns Kommunes Økonomiforvaltning i en mail til Danwatch. \n

##### Kontroversielle stater og skattelylande
I et ministerbrev fra 2012 opfordrede økonomiminister, Margrethe Vestager, landets kommunalbestyrelser til at “drøfte etiske hensyn”, når kommunale midler investeres.\n
En række kommuner, blandt andet Herning, Kalundborg og Ringkøbing-Skjern, har investeret i investeringsforeninger indeholdende statsobligationer udstedt af Panama og Trinidad & Tobago. Begge lande er skattely ifølge EU’s officielle liste over skattelylande.\n
“En af de udfordringer, der er med investeringsforeninger, er, at sammensætningen af værdipapirer i foreningen kan ændre sig, så en investering kan gå fra at overholde vores ønsker til at overtræde dem uden, at der umiddelbart tilgår os information om dette,” siger Mads Damkjær Nielsen, Kommunikationschef i Kalundborg Kommune. \n
Kortlægningen afslører også, at flere kommuner har investeringer i Saudi Arabiske statsobligationer - et land som blandt andet Akademikerpension har ekskluderet på grund af både krænkelser af menneskerettigheder og klimaskadelige aktiviteter.   \n
De fleste kommuner har vedtaget investeringspolitikker og trods store forskelle i udfaldet af de konkrete investeringer, har blandt andet Københavns Kommune haft en betydningsfuld rolle i udviklingen af ansvarlige investeringer. Det gælder især inden for klima.\n
"Nogle af de største kommuner har faktisk sammen med flere pensionskasser været førende inden for ansvarlige investeringer. De var blandt de første til at koble klimamål til investeringer”, siger Søren Larsen.\n
Databasen over kommunernes investeringer er tilgængelig for alle pr. 21. oktober 2024. 75 af de 98 kommuner har problematiske investeringer. Fire  af fem regioner har problematiske investeringer.\n

        """
    )
