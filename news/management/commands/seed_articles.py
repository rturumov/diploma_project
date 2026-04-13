from django.core.management.base import BaseCommand
from django.utils import timezone
from news.models import Article


ARTICLES = [
    {
        "title_ru": "Обвинение ничего не исправляет — принцип HOP",
        "title_en": "Blame Fixes Nothing — HOP Principle",
        "title_kz": "Кінәлау ештеңені түзетпейді — HOP қағидасы",

        "description_ru": "Второй принцип Human Organizational Performance: почему поиск виноватых мешает расследованию инцидентов.",
        "description_en": "The second principle of Human Organizational Performance: why blame culture undermines incident investigation.",
        "description_kz": "Human Organizational Performance екінші қағидасы: кінәлау мәдениеті оқиғаларды тергеуге неге кедергі келтіреді.",

        "content_ru": (
            "<p>Приветствую друзья, продолжаю писать о построении сильной культуры безопасного труда. "
            "В продолжении темы построения культуры я сегодня я хотел бы продолжить фундаментальную тему — "
            "Human Organizational Performance (далее НОР).</p>"
            "<p>Начинаем обсуждать второй принцип <b>Обвинение ничего не исправляет</b></p>"
            "<p>В постсоветском пространстве у нас в ДНК вшит принцип – произошел инцидент, обязательно должен быть "
            "кто-то виноватый! С психологической точки зрения руководства тот факт, что в результате инцидента найден "
            "виноватый, снимает с руководства ответственность за неэффективные процессы и слабую систему управления "
            "процессом БИОТ.</p>"
            "<p>Поэтому в классической системе расследования происшествий упор делается на поиск виноватых по схеме – "
            "проходил инструктаж? – соблюдал процедуру? Виновен!</p>"
            "<p>По аналогии с расследованием преступлений, никто не расследует какие факторы системы привели преступника "
            "к совершению преступления, так как никто не ставит под сомнение что система может быть неправильной, "
            "упор сделан на степень вины преступника учитывая влияние системы.</p>"
            "<p>Когда мы говорим про производственную среду, данный подход выглядит как выстрел по ногам, то есть "
            "в результате инцидента все причастные автоматически становятся обвиняемыми, в роли обвиняемого никто "
            "не будет заинтересован в обсуждении того, что произошло и как это предотвратить, все будут защищать себя. "
            "Таким образом компания теряет возможность узнать важную информацию про системные недостатки, которые можно "
            "исправить и получит лишь оправдания. Также немаловажно то что после нахождения виноватого в большинстве "
            "случаев расследование прекращается и закрывается.</p>"
            "<p>При таком подходе большинство инцидентов будет скрываться, пока есть возможность не докладывать "
            "руководству/клиенту, так как причастные, как и их непосредственное руководство будет понимать, "
            "что будут обвинены независимо от результатов расследования.</p>"
            "<p>Как мы уже говорили раннее ошибки/инциденты возникают в большинстве случаев из-за системных "
            "пробелов и организационных факторов, а не из-за плохих работников, никто не приходит на работу "
            "с намерением получить травму или нарушить процесс.</p>"
            "<p>На одном из проектов при анализе так называемых красных нарушений (категория нарушений при которых "
            "автоматически аннулируется доступ на объект) мы заметили что в последнее время у одного из подрядчиков "
            "выросло количество нарушений при работе на высоте и было удалено с объекта 5 сотрудников из-за того "
            "что они не использовали пояс безопасности, при дальнейшей проверке и беседе с подрядчиком выяснилось "
            "что 3 недели назад, сократили должность одного из кладовщиков и оставшийся кладовщик, тот что был "
            "ответственным за выдачу поясов безопасности, также стал отвечать за другой склад контейнер на другом "
            "конце объекта, таким образом, те монтажники которые приходили за поясом, должны были ждать пока он "
            "придет, либо идти за ним и приводить самим на склад чтобы под подпись получить пояс. Как стало ясно, "
            "кто-то ждал, а кто-то не стал ждать и лез наверх без пояса, надеясь не попасться. Таким образом нам "
            "повезло что мы смогли разрешить ситуацию до того, как кто-то получил бы травму.</p>"
        ),
        "content_en": (
            "<p>Hello friends, I continue writing about building a strong safety culture. "
            "Today I would like to continue the fundamental topic — Human Organizational Performance (HOP).</p>"
            "<p>We begin discussing the second principle: <b>Blame Fixes Nothing</b></p>"
            "<p>In the post-Soviet space, a principle is embedded in our DNA — when an incident occurs, "
            "someone must be guilty! From a psychological standpoint, finding someone to blame relieves "
            "management of responsibility for ineffective processes and a weak OHS management system.</p>"
            "<p>Therefore, the classic incident investigation system focuses on finding the guilty party: "
            "Did they attend the briefing? Did they follow the procedure? Guilty!</p>"
            "<p>Similar to criminal investigations, no one investigates what systemic factors led the offender "
            "to commit the crime, because no one questions whether the system itself might be flawed — "
            "the focus is on the degree of the offender's guilt considering systemic influence.</p>"
            "<p>In a production environment, this approach is like shooting yourself in the foot. After an incident, "
            "everyone involved automatically becomes the accused. No one in the role of the accused will be interested "
            "in discussing what happened and how to prevent it — everyone will defend themselves. The company loses "
            "the opportunity to learn about systemic flaws and receives only excuses. Furthermore, once the guilty "
            "party is found, the investigation usually stops.</p>"
            "<p>With this approach, most incidents will be concealed as long as there is an opportunity not to report "
            "to management, since everyone involved understands they will be blamed regardless of the investigation results.</p>"
            "<p>As we discussed earlier, errors and incidents mostly arise from systemic gaps and organizational "
            "factors, not from bad workers — no one comes to work intending to get injured or violate procedures.</p>"
            "<p>At one project, while analyzing so-called red violations (violations that automatically revoke site access), "
            "we noticed that one contractor had a growing number of violations for working at height — 5 employees "
            "were removed from the site for not using safety harnesses. After further investigation and discussion "
            "with the contractor, it turned out that 3 weeks earlier, a warehouse clerk position had been cut. "
            "The remaining clerk, responsible for issuing safety harnesses, also became responsible for another "
            "storage container at the other end of the site. Workers who came for harnesses had to wait or go "
            "fetch the clerk themselves. Some waited, others climbed up without a harness hoping not to get caught. "
            "Fortunately, we resolved the situation before anyone was injured.</p>"
        ),
        "content_kz": (
            "<p>Сәлем достар, қауіпсіз еңбек мәдениетін қалыптастыру туралы жазуды жалғастырамын. "
            "Бүгін мен негізгі тақырыпты жалғастырғым келеді — Human Organizational Performance (HOP).</p>"
            "<p>Екінші қағиданы талқылауды бастаймыз: <b>Кінәлау ештеңені түзетпейді</b></p>"
            "<p>Посткеңестік кеңістікте бізде «оқиға болды — міндетті түрде кінәлі болуы керек» деген қағида "
            "ДНҚ-ға сіңіп кеткен! Психологиялық тұрғыдан алғанда, кінәлі адамды тапқан кезде басшылық "
            "тиімсіз процестер мен әлсіз ЕҚҚ басқару жүйесі үшін жауапкершіліктен босатылады.</p>"
            "<p>Сондықтан классикалық оқиғаларды тергеу жүйесі кінәлілерді іздеуге бағытталған: "
            "нұсқаулықтан өтті ме? — рәсімді сақтады ма? Кінәлі!</p>"
            "<p>Қылмысты тергеу сияқты, ешкім жүйенің қандай факторлары қылмыскерді қылмыс жасауға "
            "итермелегенін тергемейді, өйткені жүйенің өзі қате болуы мүмкін деп ешкім күмән туғызбайды.</p>"
            "<p>Өндірістік ортада бұл тәсіл өз аяғыңнан атқандай көрінеді. Оқиғадан кейін барлық қатысушылар "
            "автоматты түрде айыпталушыға айналады. Айыпталушы рөлінде ешкім не болғанын және оны қалай "
            "болдырмауды талқылауға мүдделі болмайды — барлығы өзін қорғайды. Компания жүйелік кемшіліктер "
            "туралы маңызды ақпарат алу мүмкіндігінен айырылады.</p>"
            "<p>Бұл тәсілмен инциденттердің көпшілігі басшылыққа хабарламау мүмкіндігі бар кезде жасырылады, "
            "себебі қатысушылар тергеу нәтижелеріне қарамастан кінәланатынын түсінеді.</p>"
            "<p>Бұрын айтқанымыздай, қателер мен оқиғалар көп жағдайда жүйелік олқылықтар мен "
            "ұйымдастырушылық факторларға байланысты туындайды, нашар жұмысшылардан емес.</p>"
            "<p>Бір жобада «қызыл бұзушылықтарды» талдау кезінде бір мердігердің биіктікте жұмыс "
            "істеу кезіндегі бұзушылықтар саны өскенін байқадық — 5 қызметкер қауіпсіздік белбеуін "
            "пайдаланбағаны үшін объектіден шығарылды. Тергеу барысында 3 апта бұрын қоймашы "
            "лауазымының біреуі қысқартылғаны белгілі болды. Қалған қоймашы объектінің екінші "
            "жағындағы басқа қоймаға да жауапты болды. Монтаждаушылар белбеуді алу үшін күтуге "
            "мәжбүр болды. Біреулер күтті, ал біреулер белбеусіз жоғары көтерілді. "
            "Бақытымызға орай, біреу жарақат алғанға дейін жағдайды шеше алдық.</p>"
        ),
        "published_date": "2025-04-10",
    },
    {
        "title_ru": "Казгидромет предупреждает о загрязнении воздуха в городах Казахстана",
        "title_en": "Kazhydromet warns of air pollution in cities of Kazakhstan",
        "title_kz": "Қазгидромет Қазақстан қалаларындағы ауа ластануы туралы ескертеді",

        "description_ru": "В ряде городов Казахстана ожидается ухудшение состояния воздуха из-за метеорологических условий.",
        "description_en": "Several cities in Kazakhstan are expected to experience worsening air quality due to weather conditions.",
        "description_kz": "Қазақстанның бірқатар қалаларында ауа райы жағдайына байланысты ауа сапасының нашарлауы күтілуде.",

        "content_ru": (
            "<p>Республиканский центр по гидрометеорологии (РУЦ «Казгидромет») распространил информацию о потенциальных "
            "изменениях в состоянии воздушной среды на территории Казахстана. Специалисты предупреждают, что в ближайшие "
            "дни в определённых населённых пунктах могут сформироваться условия, способствующие накоплению загрязняющих веществ.</p>"
            "<p>В рамках обновлённого прогноза указаны города, где ожидается ухудшение атмосферной обстановки: "
            "Алматы, Атырау, Шымкент, Павлодар, Жезказган, Балхаш и Усть-Каменогорск. Такие явления, как туман, "
            "слабые ветра и температурная инверсия, могут привести к концентрации вредных компонентов в приземном "
            "слое воздуха.</p>"
            "<p>Эксперты отмечают, что неблагоприятные метеорологические факторы временные, но их влияние на "
            "экологическую обстановку требует внимания. Жителям рекомендуется соблюдать осторожность и ограничивать "
            "пребывание на улице в периоды повышенной загрязнённости.</p>"
        ),
        "content_en": (
            "<p>The Republican Center for Hydrometeorology (Kazhydromet) has issued information about potential "
            "changes in air quality across Kazakhstan. Specialists warn that in the coming days, certain populated "
            "areas may experience conditions conducive to the accumulation of pollutants.</p>"
            "<p>The updated forecast identifies cities where atmospheric conditions are expected to worsen: "
            "Almaty, Atyrau, Shymkent, Pavlodar, Zhezkazgan, Balkhash and Ust-Kamenogorsk. Phenomena such as fog, "
            "weak winds and temperature inversions may lead to concentration of harmful substances in the ground-level "
            "air layer.</p>"
            "<p>Experts note that the unfavorable meteorological factors are temporary, but their impact on the "
            "environmental situation requires attention. Residents are advised to exercise caution and limit outdoor "
            "activities during periods of elevated pollution.</p>"
        ),
        "content_kz": (
            "<p>Республикалық гидрометеорология орталығы (Қазгидромет) Қазақстан аумағындағы ауа сапасының "
            "өзгеруі туралы ақпарат таратты. Мамандар жақын күндері белгілі бір елді мекендерде ластаушы "
            "заттардың жинақталуына ықпал ететін жағдайлар қалыптасуы мүмкін екенін ескертеді.</p>"
            "<p>Жаңартылған болжамда атмосфералық жағдайдың нашарлауы күтілетін қалалар көрсетілген: "
            "Алматы, Атырау, Шымкент, Павлодар, Жезқазған, Балқаш және Өскемен. Тұман, әлсіз жел "
            "және температуралық инверсия сияқты құбылыстар жер бетіне жақын ауа қабатында зиянды "
            "компоненттердің шоғырлануына әкелуі мүмкін.</p>"
            "<p>Сарапшылар қолайсыз метеорологиялық факторлардың уақытша екенін, бірақ олардың экологиялық "
            "жағдайға әсері назар аударуды қажет ететінін атап өтеді. Тұрғындарға ластану деңгейі жоғары "
            "кезеңдерде сақтық шараларын сақтау және сыртта болуды шектеу ұсынылады.</p>"
        ),
        "published_date": "2025-04-12",
    },
    {
        "title_ru": "В Астане погиб фельдшер из-за падения кондиционера — Минтруда берёт расследование под контроль",
        "title_en": "Paramedic dies in Astana after air conditioner falls — Ministry of Labour takes control of investigation",
        "title_kz": "Астанада кондиционер құлауынан фельдшер қайтыс болды — Еңбек министрлігі тергеуді бақылауға алды",

        "description_ru": "23-летний фельдшер скончался после падения кондиционера. Министерство труда определяет компенсации семье.",
        "description_en": "A 23-year-old paramedic died after an air conditioner fell on him. The Ministry of Labour is determining compensation for the family.",
        "description_kz": "23 жастағы фельдшер кондиционер құлағаннан кейін қайтыс болды. Еңбек министрлігі отбасына өтемақы мөлшерін анықтауда.",

        "content_ru": (
            "<p>Вчера в Астане произошла трагедия: 23-летний фельдшер скончался, получив тяжелые травмы "
            "после падения кондиционера. Инцидент вызвал значительный резонанс в обществе, а Министерство "
            "труда и социальной защиты населения уже начало работу над поддержкой родственников погибшего.</p>"
            "<p>По информации, поступившей от представителей ведомства, специальная рабочая группа занимается "
            "рассмотрением всех вопросов, связанных с компенсациями и обязанностями работодателя. Вице-министр "
            "Аскарбек Эртаев подчеркнул, что единовременные выплаты будут определены в ходе расследования, "
            "а также учитываться особенности семейного положения пострадавшего.</p>"
            "<p>Если у умершего родится ребенок, семья будет получать социальные пособия в рамках «потери опекуна». "
            "В случае наличия супруги или супруга, право на компенсацию может получить и один, и другой. Размер "
            "выплаты составит 95 минимальных размеров пособий, если у погибшего были обязательные социальные отчисления.</p>"
            "<p>Кроме того, страховщики обязаны выполнить условия договора, если такие имеются. Все детали будут "
            "уточнены в процессе деятельности комиссии. Напомним, что ранее сообщалось о трагическом случае, "
            "а Президент Казахстана посмертно наградил молодого сотрудника медалью «За отвагу».</p>"
        ),
        "content_en": (
            "<p>Yesterday a tragedy occurred in Astana: a 23-year-old paramedic died after sustaining severe "
            "injuries from a falling air conditioner. The incident caused significant public outcry, and the "
            "Ministry of Labour and Social Protection has already begun working on supporting the victim's family.</p>"
            "<p>According to information from ministry representatives, a special working group is reviewing all "
            "matters related to compensation and employer obligations. Vice-Minister Askarbek Yertayev emphasized "
            "that lump-sum payments will be determined during the investigation, taking into account the victim's "
            "family circumstances.</p>"
            "<p>If the deceased has a child to be born, the family will receive social benefits under the "
            "'loss of guardian' program. If there is a spouse, both parties may be entitled to compensation. "
            "The payment amount will be 95 minimum benefit sizes if the deceased had mandatory social contributions.</p>"
            "<p>Additionally, insurers are obligated to fulfill contract terms if applicable. All details will be "
            "clarified during the commission's work. It was previously reported that the President of Kazakhstan "
            "posthumously awarded the young worker the Medal for Bravery.</p>"
        ),
        "content_kz": (
            "<p>Кеше Астанада қайғылы оқиға болды: 23 жастағы фельдшер кондиционер құлауынан ауыр жарақат алып, "
            "қайтыс болды. Оқиға қоғамда үлкен резонанс тудырды, ал Еңбек және халықты әлеуметтік қорғау "
            "министрлігі қаза тапқанның туыстарын қолдау жұмысын бастады.</p>"
            "<p>Ведомство өкілдерінен түскен ақпаратқа сәйкес, арнайы жұмыс тобы өтемақылар мен жұмыс "
            "берушінің міндеттеріне қатысты барлық мәселелерді қарастыруда. Вице-министр Асқарбек Ертаев "
            "біржолғы төлемдер тергеу барысында анықталатынын және зардап шегушінің отбасылық жағдайы "
            "ескерілетінін атап өтті.</p>"
            "<p>Егер қайтыс болғанның баласы туылатын болса, отбасы «қамқоршысынан айырылу» аясында "
            "әлеуметтік жәрдемақы алады. Жұбайы болған жағдайда, екеуі де өтемақы алуға құқылы. "
            "Қайтыс болғанның міндетті әлеуметтік аударымдары болса, төлем мөлшері жәрдемақының "
            "95 ең төменгі мөлшерін құрайды.</p>"
            "<p>Сонымен қатар, сақтандырушылар шарт талаптарын орындауға міндетті. Барлық мәліметтер "
            "комиссия жұмысы барысында нақтыланады. Бұрын хабарланғандай, Қазақстан Президенті жас "
            "қызметкерді «Ерлігі үшін» медалімен марапаттаған болатын.</p>"
        ),
        "published_date": "2025-04-13",
    },
]


class Command(BaseCommand):
    help = "Seed the database with initial news articles (ru/en/kz)"

    def handle(self, *args, **options):
        for data in ARTICLES:
            article, created = Article.objects.get_or_create(
                title_ru=data["title_ru"],
                defaults={
                    "title_en": data["title_en"],
                    "title_kz": data["title_kz"],
                    "description_ru": data["description_ru"],
                    "description_en": data["description_en"],
                    "description_kz": data["description_kz"],
                    "content_ru": data["content_ru"],
                    "content_en": data["content_en"],
                    "content_kz": data["content_kz"],
                    "published_date": data["published_date"],
                    "article_status": True,
                },
            )
            status = "created" if created else "already exists"
            self.stdout.write(f"  [{status}] {data['title_ru'][:60]}")

        self.stdout.write(self.style.SUCCESS(f"\nDone! {len(ARTICLES)} articles processed."))
