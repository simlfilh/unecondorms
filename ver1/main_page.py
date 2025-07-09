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

st.markdown("""
    Добро пожаловать на портал общежитий Санкт-Петербургского государственного экономического университета.  
    Здесь вы найдете актуальную информацию о каждом общежитии, правила проживания и контакты администрации.
""")
st.divider()

# Глобальный CSS для точного контроля отступов
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
    st.markdown(create_button("https://chkalovski27.streamlit.app/", "Общежитие №2 | Чкаловский 27"), unsafe_allow_html=True)
    st.image("здание_общежития_ч27.jpg", use_container_width=True)

with col2:
    st.markdown(create_button("https://kosigina19k2.streamlit.app/", "Общежитие №3 | Косыгина 19к2"), unsafe_allow_html=True)
    st.image("здание общежития.jpg", use_container_width=True)

with col3:
    st.markdown(create_button("https://voronezhskaya69.streamlit.app/", "Общежитие №4 | Воронежская 69"), unsafe_allow_html=True)
    st.image("здание_общежития_в69.jpg", use_container_width=True)

with col4:
    st.markdown(create_button("https://voronezhskaya38.streamlit.app/", "Общежитие №7 | Воронежская 38"), unsafe_allow_html=True)
    st.image("здание_общежития_в38.jpg", use_container_width=True)
st.divider()

st.subheader("❓ Часто задаваемые вопросы: заселение в общежитие")
st.markdown("""
    Заселение в общежитие всегда вызывает много вопросов. Страшно, сложно и непонятно, знаем. 
    Поэтому мы подготовили для тебя FAQ по общежитиям — ответы начальника Жилищно-бытового управления Рябова Сергея Павловича.
    """)
faq = {
    "— Какие условия нужны, чтобы заселиться в общежитие?":
        st.markdown("""
            **Общежитие предоставляется:**  
            • Иногородним студентам (в приоритете — очная форма обучения)  
            • На основе онлайн-бронирования через личный кабинет  
            • С учетом баллов ЕГЭ  

            **Не предоставляется:**  
            • Студентам, проживающим в ближайших пригородах Санкт-Петербурга  

            Все документы размещены на сайте Университета в разделе «общежития».
            """),
    "— Какие из общежитий блочного, а какие коридорного типа?":
        st.markdown("""
            **Коридорный тип:**  
            • Общежитие №2 (пр. Чкаловский, 27)  
            • Общежитие №7 (ул. Воронежская, 38)  

            **Блочный тип:**  
            • Общежитие №3 (пр. Косыгина, 19/2)  
            • Общежитие №4 (ул. Воронежская, 69)
            """),
    "— Что запрещено в общежитии?":
        st.markdown("""
            Строго запрещено:  
            • Употребление алкоголя и курение  
            • Нахождение в нетрезвом виде  
            • Использование пожароопасных приборов  
            • Содержание животных  
            • Открытый огонь
            """),
    "— Есть ли вероятность того, что я поступлю в вуз, но не получу общежитие?":
        st.markdown("""
            Практика показывает:  
            • Все иногородние студенты-очники получают место  
            • Приоритет — по баллам ЕГЭ и дате подачи заявления
            """),
    "— Как распределяют студентов по общежитиям?":
        st.markdown("""
            Процесс распределения:  
            1. После зачисления открывается онлайн-бронирование  
            2. В личном кабинете доступны:  
               - Фотографии комнат  
               - Выбор из доступных вариантов  
            3. Система автоматически учитывает ваш рейтинг
            """)
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)
st.divider()

col9, col10 = st.columns([1, 1])
with col9:
    st.subheader("🔗 Полезные ресурсы")
    st.markdown("""
        - [Официальный сайт СПбГЭУ](https://unecon.ru)  
        - [Портал для студентов](https://my.unecon.ru)  
        - [Группа ВКонтакте](https://vk.com/unecon)  
    """)
with col10:
    st.subheader("Контакты для связи")
    st.markdown("""
    **Отдел по работе с общежитиями:**  
    📍 Адрес: наб. канала Грибоедова, д. 30-32, лестница № 4  
    📞 Справки по телефону: [+7 (812) 458-97-30, доб. 4291, 4294](tel:+78124589730,4291,4294)  
    📩 [dom@unecon.ru](mailto:dom@unecon.ru)  
    
    **Часы приема:**  
    ПН: 14:00 — 16:30  
    ВТ: 14:00 — 16:30  
    СР: приема нет  
    ЧТ: 14:00 — 16:30  
    ПТ: 13:00 — 15:00  
    """, unsafe_allow_html=True)
