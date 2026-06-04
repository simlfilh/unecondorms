import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Общежития СПбГЭУ",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏠 | Общежития для заселения - СПбГЭУ")
st.divider()

st.markdown(
    """
    <style>
    .stApp {
        min-height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    Добро пожаловать на портал общежитий Санкт-Петербургского государственного экономического университета.  
    Ниже вы найдете актуальную информацию о каждом общежитии, правила проживания и контакты администрации.
""")
st.divider()

st.markdown("""
<style>
    div[data-testid="column"] {
        gap: 0 !important;
    }
    .custom-button {
        margin-bottom: 10px !important;  /* Отступ снизу кнопки */
    }
    .stImage {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

def create_button(url, text):
    return f"""
    <div class="custom-button">
        <a href="{url}" style="text-decoration: none;">
            <button style="
                width: 100%;
                color: white;
                background-color: #26B28C;
                border: none;
                padding: 10px 0;
                border-radius: 5px;
                font-weight: bold;
                cursor: pointer;
            ">{text}</button>
        </a>
    </div>
    """

with col1:
    st.markdown(create_button("https://chkalovski27.streamlit.app/", "Общежитие №2 | Чкаловский пр., д. 27"), unsafe_allow_html=True)
    st.markdown(create_button("https://unecon.ru/wp-content/uploads/2025/08/chkal.pdf", "Путеводитель по общежитию №2"), unsafe_allow_html=True)
    st.image("здание_общежития_ч27.jpg", use_container_width=True)

with col2:
    st.markdown(create_button("https://kosigina19k2.streamlit.app/", "Общежитие №3 | пр. Косыгина, д. 19, к. 2"), unsafe_allow_html=True)
    st.markdown(create_button("https://unecon.ru/wp-content/uploads/2025/08/kosyg.pdf", "Путеводитель по общежитию №3"), unsafe_allow_html=True)
    st.image("здание общежития.jpg", use_container_width=True)

with col3:
    st.markdown(create_button("https://voronezhskaya69.streamlit.app/", "Общежитие №4 | ул. Воронежская, д. 69"), unsafe_allow_html=True)
    st.markdown(create_button("https://unecon.ru/wp-content/uploads/2025/08/voronezhskaya69.pdf", "Путеводитель по общежитию №4"), unsafe_allow_html=True)
    st.image("здание_общежития_в69.jpg", use_container_width=True)

with col4:
    st.markdown(create_button("https://voronezhskaya38.streamlit.app/", "Общежитие №7 | ул. Воронежская, д. 38"), unsafe_allow_html=True)
    st.markdown(create_button("https://unecon.ru/wp-content/uploads/2025/08/v38.pdf", "Путеводитель по общежитию №7"), unsafe_allow_html=True)
    st.image("здание_общежития_в38.jpg", use_container_width=True)
st.divider()

st.subheader("❓ Часто задаваемые вопросы: заселение в общежитие")
st.markdown("""
    Заселение в общежитие всегда вызывает много вопросов. Страшно, сложно и непонятно, знаем. 
    Поэтому мы подготовили для тебя FAQ по общежитиям — ответы начальника Жилищно-бытового управления.
    """)
faq = {
    "— Какие условия нужны, чтобы заселиться в общежитие?":
        "<p>Общежитие предоставляется иногородним студентам, в приоритете — очная форма обучения.</p>"
        "<p>Заселение осуществляется через личный кабинет с помощью онлайн бронирования, в зависимости от баллов ЕГЭ.</p>"
        "<p>Общежитие не предоставляется студентам, проживающим в ближайших пригородах Санкт-Петербурга.</p>"
        "<p>Все документы и информация о поселении размещены на сайте Университета в разделе «общежития».</p>",

    "— Какие из общежитий блочного, а какие коридорного типа?":
        "<p><b>Коридорный тип:</b></p>"
        "<ul><li>Общежитие №2 пр. Чкаловский 27</li><li>Общежитие №7 ул. Воронежская 38</li></ul>"
        "<p><b>Блочный тип:</b></p>"
        "<ul><li>Общежитие №3 пр. Косыгина 19/2</li><li>Общежитие №4 ул. Воронежская 69</li></ul>",

    "— Что запрещено в общежитии?":
        "<ul>"
        "<li>Употреблять спиртные напитки</li>"
        "<li>Курить</li>"
        "<li>Находиться на территории общежития в нетрезвом виде</li>"
        "<li>Использовать пожароопасные бытовые приборы</li>"
        "<li>Пользоваться открытым огнем</li>"
        "<li>Содержать животных</li>"
        "</ul>",

    "— Есть ли вероятность того, что я поступлю в вуз, но не получу общежитие?":
        "<p>Как правило, все иногородние студенты очной формы обучения получают место в общежитии.</p>",

    "— Как распределяют студентов по общежитиям?":
        "<p>В личном кабинете у каждого абитуриента после выхода приказа о зачислении открывается возможность "
        "онлайн-бронирования, где можно увидеть фотографии комнат и выбрать ее по собственному желанию, "
        "из имеющихся в наличии.</p>",

    "— Можно ли переселиться из комнаты, выбранной первоначально, в другую комнату?":
        "<p>Этот вопрос может быть рассмотрен при наличии свободных мест, после основного поселения всех студентов, "
        "поступивших на первый курс.</p>",

    "— Какова стоимость проживания в общежитиях университета?":
        "<p>Стоимость проживания зависит от выбранного общежития и комфортности комнаты в пределах "
        "<b>от 3500 до 7200 руб./мес.</b></p>",

    "— Какие льготы предусмотрены для студентов при заселении?":
        "<p><b>В первую очередь заселяются:</b></p>"
        "<ul>"
        "<li>Дети-сироты</li>"
        "<li>Дети-инвалиды/ЧАЭС</li>"
        "<li>Студенты, получающие государственную социальную стипендию</li>"
        "</ul>"
        "<p><b>Во вторую очередь:</b></p>"
        "<ul><li>Дети участников СВО</li></ul>",

    "— Что взять с собой в общежитие?":
        "<p><b>Предоставляется общежитием:</b></p>"
        "<ul>"
        "<li>Постельное белье</li>"
        "<li>Стол, стул, кровать</li>"
        "<li>Тумба и шкаф</li>"
        "</ul>"
        "<p><b>Можно взять с собой:</b></p>"
        "<ul>"
        "<li>Кухонные принадлежности (кастрюлька, тарелка, чашка, ложка, вилка)</li>"
        "<li>Предметы личной гигиены</li>"
        "<li>Личные вещи</li>"
        "</ul>"
        "<p><b>Оборудование в общежитиях:</b></p>"
        "<ul>"
        "<li>Стиральные и сушильные машины</li>"
        "<li>Электро и газовые плиты</li>"
        "<li>Микроволновые печи на общих кухнях</li>"
        "</ul>",

    "— Когда начнется заселение в общежития?":
        "<p><b>С 21 августа</b> начнется заселение. Приезжать необходимо в то общежитие, которое вы забронировали "
        "через личный кабинет с полным пакетом документов.</p>"
        "<p><b>Часы заселения:</b> с 10.00 до 16.00.</p>"
        "<p><b>Важно:</b> По прибытии в Санкт-Петербург не гулять по городу до вечера, "
        "а сразу ехать в общежитие. Приезжайте в первой половине дня.</p>"
}
for question, answer in faq.items():
    with st.expander(question):
        st.markdown(answer, unsafe_allow_html=True)
st.divider()

col9, col10 = st.columns([1, 1])
with col9:
    st.subheader("🔗 Полезные ресурсы")
    st.markdown("""
    <div>
        <ul>
            <li><a href="https://unecon.ru">Официальный сайт СПбГЭУ</a></li>
            <li><a href="https://student.unecon.ru">Портал для студентов</a></li>
            <li><a href="https://vk.com/unecon">Группа ВКонтакте</a></li>
        </ul>
    </div>
""", unsafe_allow_html=True)
with col10:
    st.subheader("Контакты для связи")
    st.markdown("""
    <div>
        <p><strong>Жилищно-бытовое управление:</strong></p>
        <p>📍 Адрес: наб. канала Грибоедова, д. 30-32, лестница № 4</p>
        <p>📞 Справки по телефону: <a href="tel:+78124589730,4291,4294">+7 (812) 458-97-30, доб. 4291, 4294</a></p>
        <p>📩 <a href="mailto:dom@unecon.ru">dom@unecon.ru</a></p>
        <p><strong>Часы приема:</strong></p>
        <p>ПН: 14:00 — 16:30
        <br>
        ВТ: 14:00 — 16:30
        <br>
        СР: приема нет
        <br>
        ЧТ: 14:00 — 16:30
        <br>
        ПТ: 13:00 — 15:00</p>
    </div>
""", unsafe_allow_html=True)
# убрать    st.markdown(create_button("https://appointmentzhbuforstudents.streamlit.app/", "Записаться на прием"), unsafe_allow_html=True)
    





