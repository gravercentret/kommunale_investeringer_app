import streamlit as st
from config import set_pandas_options, set_streamlit_options
from utils.data_processing import load_css, write_markdown_sidebar, create_user_session_log

create_user_session_log("Mulige kilder og citater")

st.logo("webapp/images/GC_png_oneline_lockup_Outline_Blaa_RGB.png")

# Apply the settings
set_pandas_options()
set_streamlit_options()
load_css("webapp/style.css")

with st.sidebar:
    write_markdown_sidebar()

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Citater og mulige kilder",
        "Sådan kommer du i gang",
        "Baggrundsviden om FN's liste",
        "Kommuner og regioner uden problematiske værdipapirer",
    ]
)

with tab1:
    st.header("Citater til fri afbenyttelse")

    st.markdown(
        " ###### Følgende citater er til fri afbenyttelse i forbindelse med omtale af informationer fra dette datasæt:"
    )

    with st.expander(
        "**Per Nikolaj Bukh, professor i økonomistyring fra Aalborg Universitet**", expanded=True
    ):
        st.markdown(
            """
    “Kommunerne må investere i samme investeringsbeviser som fonde og forventes at være økonomisk ansvarlige. De bør faktisk investere deres overskydende likviditet. Men de må kun investere i bestemte typer af obligationer og investeringsforeninger”, siger professor i økonomistyring, Per Nikolaj Bukh fra Aalborg Universitet. \n

    “Forskellene i hvilke af de potentielt problematiske investeringer, som kommunerne har, kan i høj grad forklares med, hvilke forvaltere kommunerne har hyret.  Forvalterne har forskellige tilbud om ESG-screenede (bæredygtighedsindsatser red.) fonde og dermed også på hvilke selskaber, som man investerer i”, siger Per Nikolaj Bukh. 
    """
        )

    with st.expander(
        "**Søren Larsen, uafhængig ESG-rådgiver og tidligere chef for bæredygtige investeringer i Nykredit.**",
        expanded=True,
    ):
        st.markdown(
            """
    "Generelt så indikerer investering i få kontroversielle selskaber, at investor har en systematisk tilgang til at undgå disse blandt de mange tusinde aktieselskaber, der handles på verdens børser”, vurderer Søren Larsen, uafhængig ESG-rådgiver og tidligere chef for bæredygtige investeringer i Nykredit.\n

    "Det er ret vigtigt at formulere en ansvarlig investeringspolitik og sikre, at man har en aftale med en forvalter, som kan gennemføre politikken. Derefter skal kommunerne som alle andre investorer sikre sig, at politikken faktisk bliver ført ud i livet, siger Søren Larsen, der har rådgivet både store private og offentlige investorer. \n

    """
        )

    with st.expander("**KL og Danske Regioner**", expanded=True):
        st.markdown(
            """
        Hverken KL eller Danske Regioner ønsker at komme med nogle råd eller anbefalinger til deres medlemmer vedrørende investeringer.

        KL er kommet med følgende skriftlige kommentar: "KL yder ikke finansiel rådgivning til kommunerne, så vi har ikke råd og anbefalinger ift. kommunernes placering af midler. Det er op til kommunerne inden for styrelseslovens rammer."

        Og Danske Regioner svarer følgende: "Det er ikke noget Danske Regioner rådgiver om."
        """
        )

    st.header("Mulige kilder")

    st.markdown(
        """
                De oplagte kilder til historier på baggrund af data er naturligvis kommunen eller regionen selv. 
                Det vil typisk være de politiske valgte, der vil være mest interessante at tale med, 
                for der er ikke noget ulovligt i at investere i problematiske værdipapirer. Det er mere et spørgsmål om moral og etik.\n
    I kommunerne vil det være borgmesteren, der er født formand for økonomiudvalget og repræsentanter for oppositionen i kommunen, 
                der vil være interessante at få en kommentar fra.\n
    Det samme gør sig gældende for regionerne.\n
    Det kunne også være interessant at tale med presseafdelingerne for de banker og pensionskasser, 
                der havde sortlistet nogle bestemte papirer for at få en uddybning af årsagen til eksklusionen.\n
    """
    )

with tab2:
    st.subheader("Sådan kommer du i gang:")

    st.markdown(
        """
    Hvis du vil se oplysninger om investeringerne i en bestemt kommune eller region, så kan du vælge den i menuen ude til venstre på forsiden.\n
    Data bliver så automatisk sorteret, så du kun ser oplysninger fra den ønskede kommune på siden.\n
    Nedenunder hovedtallene er der et skema med detaljerede oplysninger om alle værdipapirerne i den valgte kommune. Farven indikerer, om et bestemt værdipapir er fra et problematisk selskab (rød), en problematisk statsobligation (orange) eller potentielt kontroversielt (gul).\n
    Kolonnen ”Eksklusion (af hvem og hvorfor)” viser, hvem, der har udpeget det som problematisk og hvilken grund, der er oplyst. Ved at scrolle til højre i skemaet kan man se en anden kolonne, der hedder ”sortlistet”. Her kan man se, hvor mange sorte lister fra danske banker, pensionsselskaber og FN det pågældende værdipapir er på. Står der eksempelvis 5, så er værdipapiret altså sortlistet af fem forskellige parter.\n
    Som tommelfingerregel kan man sige, at jo flere sorte lister et bestemt værdipapir er på, jo mere problematisk er det.\n
    Fokuserer man på en håndfuld bestemte værdipapirer er det god ide at få bekræftet af kommunen eller regionen, at de fortsat ejer det gennem deres investeringsforening eller fond – men selv hvis de ikke længere skulle eje det, så har de selv oplyst, at de i 2024 havde investeret i det.\n
    Vil man vide mere om, hvorfor et papir er problematisk, kan man scrolle længere ud til højre og finde ISIN nummeret – det er et unikt nummer ligesom et CPR-nummer, der gør det muligt at finde flere oplysninger om værdipapiret.\n
    Man kan også vælge at kontakte de forskellige banker og pensionsselskaber og bede dem uddybe, hvorfor de ikke vil investere i værdipapiret.\n

    """
    )

with tab3:
    st.subheader("Baggrundsviden om FN's liste")

    st.markdown(
        """
        **Liste fra FN’s højkommissær for menneskerettigheder**\n
        Sekretariatet for FN’s højkommissær for menneskerettigheder (OHCHR), som har til opgave at fremme, overvåge og beskytte menneskerettighederne over hele verden, har oprettet [en liste over virksomheder](https://www.ohchr.org/sites/default/files/documents/hrbodies/hrcouncil/sessions-regular/session31/database-hrc3136/23-06-30-Update-israeli-settlement-opt-database-hrc3136.pdf), der er involveret i aktiviteter relateret til israelske bosættelser i besatte palæstinensiske områder - Vestbredden, Østjerusalem og Gazastriben. \n
        Disse områder er under israelsk besættelse, og bosættelserne anses for at være i strid med international lov, særligt Genèvekonventionen. \n

        Listen er baseret på FN’s Menneskerettighedsråds undersøgelse og inkluderer virksomheder, der for eksempel leverer udstyr til bosættelser eller udnytter naturressourcer fra de besatte områder. Databasen bliver løbende opdateret for at vise, hvilke virksomheder der fortsat er involveret i disse aktiviteter.\n

    """
    )

with tab4:
    st.subheader("Kommuner og regioner uden problematiske værdipapierer")

    st.markdown(
        """
    23 kommuner og en region har ingen problematiske investeringer, som optræder på eksklusionslister fra banker, pensionsselskaber eller FN.\n

    Der er tale om følgende kommuner: Glostrup, Odsherred, Frederikssund, Hjørring, Stevns, Gladsaxe, Vordingborg, Halsnæs, Frederikshavn, Tårnby, Odder, Dragør, Albertslund, Ishøj, Langeland, Herlev, Gentofte, Sønderborg, Allerød, Ærø, Ringsted samt Læsø og Samsø, der slet ikke har investeringer.\n
    Region Syddanmark har heller ingen problematiske investeringer.\n

    """
    )

    st.markdown(
        """
        **Den Internationale Domstols (ICJ) vurdering**\n
        Det er i den forbindelse relevant at se på [Den Internationale Domstols (ICJ) vurdering fra den 19. juli 2024.](https://www.icj-cij.org/sites/default/files/case-related/186/186-20240719-sum-01-00-en.pdf) Den omhandler de juridiske konsekvenser af Israels politikker og praksisser i de besatte palæstinensiske områder. \n

        ICJ konkluderer, at Israels fortsatte tilstedeværelse i disse områder er ulovlig ifølge international lov. Besættelsen strider imod folkeretten, herunder palæstinensernes ret til selvbestemmelse. \n

        Dette betyder, at også investeringer eller finansieringsaktiviteter, der direkte eller indirekte støtter Israels ulovlige bosættelser eller udnyttelse af ressourcer i de besatte områder, kan være i strid med international lov, da de kan opfattes som en medvirken til at opretholde den ulovlige besættelse. \n

    """
    )
