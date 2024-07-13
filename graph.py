import json
import streamlit as st
from streamlit_echarts import st_echarts

def mostrar_quien_soy():
    opcion_seleccionada = st.selectbox(
        "Qué enfoque ver:",
        ("Desde lo humano", "Desde lo técnico", "Integralmente")
    )

    def Grafico_tecnico():
        st.write('Ingeniero industrial, especialista en datos, apasionado por la analítica, el desarrollo y la programación')
        # Datos del grafo
        graph = {
            "nodes": [
                {"id": "1", "name": "SQL", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5470c6"}},  # Azul
                {"id": "2", "name": "Python", "category": 0, "symbol": "rect", "itemStyle": {"color": "#91cc75"}},  # Verde
                {"id": "3", "name": "AWS", "category": 0, "symbol": "rect", "itemStyle": {"color": "#fac858"}},  # Amarillo
                {"id": "4", "name": "Machine Learning", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ca8622"}},  # Naranja
                {"id": "5", "name": "Programación Orientada a Objetos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ee6666"}},  # Rojo
                {"id": "6", "name": "Automatizaciones", "category": 0, "symbol": "rect", "itemStyle": {"color": "#c4ccd3"}},  # Gris
                {"id": "7", "name": "Power BI", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5978bb"}},  # Azul oscuro
                {"id": "8", "name": "Office", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5ab1ef"}},  # Azul claro
                {"id": "9", "name": "Escenarios What-If", "category": 0, "symbol": "rect", "itemStyle": {"color": "#d87a80"}},  # Rojo claro
                {"id": "10", "name": "Computación en la Nube", "category": 0, "symbol": "rect", "itemStyle": {"color": "#919191"}},  # Gris oscuro
                
                # Nodos hijos para SQL
                {"id": "11", "name": "Consultas Avanzadas", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5470c6"}},
                {"id": "12", "name": "Procedimientos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5470c6"}},
                {"id": "13", "name": "Vistas", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5470c6"}},
                {"id": "14", "name": "Diseño Relacional", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5470c6"}},
                
                # Nodos hijos para Python
                {"id": "15", "name": "Pandas", "category": 0, "symbol": "rect", "itemStyle": {"color": "#91cc75"}},
                {"id": "16", "name": "NumPy", "category": 0, "symbol": "rect", "itemStyle": {"color": "#91cc75"}},
                # {"id": "17", "name": "Decoradores", "category": 1, "symbol": "rect", "itemStyle": {"color": "#91cc75"}},
                # {"id": "18", "name": "Iteradores y Generadores", "category": 1, "symbol": "rect", "itemStyle": {"color": "#91cc75"}},
                
                # Nodos hijos para AWS
                {"id": "19", "name": "EC2", "category": 0, "symbol": "rect", "itemStyle": {"color": "#fac858"}},
                {"id": "20", "name": "S3", "category": 0, "symbol": "rect", "itemStyle": {"color": "#fac858"}},
                {"id": "21", "name": "Lambda", "category": 0, "symbol": "rect", "itemStyle": {"color": "#fac858"}},
                {"id": "22", "name": "RDS", "category": 0, "symbol": "rect", "itemStyle": {"color": "#fac858"}},
                
                # Nodos hijos para Machine Learning
                {"id": "23", "name": "Modelos Supervisados", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ca8622"}},
                {"id": "24", "name": "Modelos No Supervisados", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ca8622"}},
                {"id": "25", "name": "Validación Cruzada", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ca8622"}},
                {"id": "26", "name": "Overfitting y Underfitting", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ca8622"}},
                
                # Nodos hijos para Programación Orientada a Objetos (OOP)
                {"id": "27", "name": "Clases y Objetos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ee6666"}},
                {"id": "28", "name": "Herencia y Polimorfismo", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ee6666"}},
                {"id": "29", "name": "Encapsulamiento", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ee6666"}},
                # {"id": "30", "name": "Abstracción", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ee6666"}},
                
                # Nodos hijos para Automatizaciones en la Cadena de Suministro
                {"id": "31", "name": "SAP", "category": 0, "symbol": "rect", "itemStyle": {"color": "#c4ccd3"}},
                {"id": "32", "name": "Gestion de datos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#c4ccd3"}},
                {"id": "33", "name": "Documentación", "category": 0, "symbol": "rect", "itemStyle": {"color": "#c4ccd3"}},
                {"id": "34", "name": "Repositorios compartidos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#c4ccd3"}},
                
                # Nodos hijos para Power BI
                {"id": "35", "name": "Transformación de Datos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5978bb"}},
                {"id": "36", "name": "Gateways de Datos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5978bb"}},
                {"id": "37", "name": "DAX (Data Analysis Expressions)", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5978bb"}},
                {"id": "38", "name": "Paneles y Reportes", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5978bb"}},
                
                # Nodos hijos para Office
                {"id": "39", "name": "Excel Avanzado", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5ab1ef"}},
                {"id": "40", "name": "Power Query", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5ab1ef"}},
                {"id": "41", "name": "VBA", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5ab1ef"}},
                {"id": "42", "name": "Documentaciones", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5ab1ef"}},
                
                # Nodos hijos para Escenarios What-If en Power BI
                {"id": "43", "name": "Simulaciones de Escenarios", "category": 0, "symbol": "rect", "itemStyle": {"color": "#d87a80"}},
                {"id": "44", "name": "Análisis de Sensibilidad", "category": 0, "symbol": "rect", "itemStyle": {"color": "#d87a80"}},
                {"id": "45", "name": "Parámetros en Power BI", "category": 0, "symbol": "rect", "itemStyle": {"color": "#d87a80"}},
                {"id": "46", "name": "Escenarios Alternativos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#d87a80"}},
                
                # Nodos hijos para Computación en la Nube
                {"id": "47", "name": "Escalabilidad", "category": 0, "symbol": "rect", "itemStyle": {"color": "#919191"}},
                {"id": "48", "name": "Seguridad en la Nube", "category": 0, "symbol": "rect", "itemStyle": {"color": "#919191"}},
                {"id": "49", "name": "Servicios Web en la Nube", "category": 0, "symbol": "rect", "itemStyle": {"color": "#919191"}},
                {"id": "50", "name": "Big Data", "category": 0, "symbol": "rect", "itemStyle": {"color": "#919191"}},
            ],
            "links": [
                # Relaciones para SQL
                {"source": "1", "target": "11"},
                {"source": "1", "target": "12"},
                {"source": "1", "target": "13"},
                {"source": "1", "target": "14"},
                {"source": "1", "target": "22"},
                {"source": "1", "target": "35"},
                
                # Relaciones para Python
                {"source": "2", "target": "15"},
                {"source": "2", "target": "16"},
                {"source": "2", "target": "17"},
                {"source": "2", "target": "18"},
                {"source": "2", "target": "5"},
                {"source": "2", "target": "6"},
                {"source": "2", "target": "4"},
                
                # Relaciones para AWS
                {"source": "3", "target": "19"},
                {"source": "3", "target": "20"},
                {"source": "3", "target": "21"},
                {"source": "3", "target": "22"},
                {"source": "3", "target": "47"},
                {"source": "3", "target": "4"},
                
                # Relaciones para Machine Learning
                {"source": "4", "target": "23"},
                {"source": "4", "target": "24"},
                {"source": "4", "target": "25"},
                {"source": "4", "target": "26"},
                
                # Relaciones para Programación Orientada a Objetos (OOP)
                {"source": "5", "target": "27"},
                {"source": "5", "target": "28"},
                {"source": "5", "target": "29"},
                {"source": "5", "target": "30"},
                
                # Relaciones para Automatizaciones en la Cadena de Suministro
                {"source": "6", "target": "31"},
                {"source": "6", "target": "32"},
                {"source": "6", "target": "33"},
                {"source": "6", "target": "34"},
                {"source": "6", "target": "41"},
                {"source": "6", "target": "36"},
                
                # Relaciones para Power BI
                {"source": "7", "target": "35"},
                {"source": "7", "target": "36"},
                {"source": "7", "target": "37"},
                {"source": "7", "target": "38"},
                
                # Relaciones para Office
                {"source": "8", "target": "39"},
                {"source": "8", "target": "40"},
                {"source": "8", "target": "41"},
                {"source": "8", "target": "42"},
                
                # Relaciones para Escenarios What-If en Power BI
                {"source": "9", "target": "43"},
                {"source": "9", "target": "44"},
                {"source": "9", "target": "45"},
                {"source": "9", "target": "46"},
                
                # Relaciones para Computación en la Nube
                {"source": "10", "target": "47"},
                {"source": "10", "target": "48"},
                {"source": "10", "target": "49"},
                {"source": "10", "target": "50"},
                
                # Relaciones cruzadas si aplican
                {"source": "1", "target": "32"},
                {"source": "6", "target": "34"},
                {"source": "7", "target": "45"},
                {"source": "9", "target": "49"}
            ],
            "categories": [
                {"name": "Conocimientos Técnicos"},
                {"name": "Habilidades"}
            ]
        }



        # Ajustar el tamaño de los nodos
        for idx, _ in enumerate(graph["nodes"]):
            graph["nodes"][idx]["symbolSize"] = 10  # Aumentar el tamaño para mayor visibilidad

        # Configuración de la visualización
        option = {
            "title": {
                "text": 'Quien soy',
                "subtext": "Default layout",
                "top": "bottom",
                "left": "right",
            },
            "tooltip": {},
            "legend": {
                "data": [
                    # {"name": "Habilidades", "icon": "circle"},
                    {"name": "Conocimientos Técnicos", "icon": "rect"}
                ]
            },
            "series": [
                {
                    "type": "graph",
                    "layout": "force",
                    "data": graph["nodes"],
                    "links": graph["links"],
                    "categories": graph["categories"],
                    "roam": True,
                    "label": {"position": "right"},
                    "draggable": True,
                    "force": {"repulsion": 100},
                }
            ],
        }

        # Mostrar la visualización en Streamlit
        st_echarts(option, height="500px")

    def Grafico_blando():
        # Datos del grafo
        st.write('Hermano, hijo, novio, enfocado en vivir tranquilo y ayudar, con una responsabilidad social clara y en constante aprendizaje')
        
        graph = {
            "nodes": [
                {"id": "51", "name": "Liderazgo", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff7f50"}},  # Coral
                {"id": "52", "name": "Storytelling", "category": 1, "symbol": "circle", "itemStyle": {"color": "#87cefa"}},  # Azul cielo
                {"id": "53", "name": "Innovación", "category": 1, "symbol": "circle", "itemStyle": {"color": "#da70d6"}},  # Orquídea
                {"id": "54", "name": "Conversaciones Difíciles", "category": 1, "symbol": "circle", "itemStyle": {"color": "#32cd32"}},  # Verde lima
                {"id": "55", "name": "Empatía", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ffa500"}},  # Naranja
                {"id": "56", "name": "Confianza", "category": 1, "symbol": "circle", "itemStyle": {"color": "#9370db"}},  # Púrpura medio
                {"id": "57", "name": "Delegar", "category": 1, "symbol": "circle", "itemStyle": {"color": "#3cb371"}},  # Verde mar
                {"id": "58", "name": "Reconocer", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff6347"}},  # Tomate
                
                # Nodos hijos para Liderazgo
                {"id": "59", "name": "Visión Estratégica", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff7f50"}},
                {"id": "60", "name": "Toma de Decisiones", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff7f50"}},
                {"id": "61", "name": "Motivación de Equipos", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff7f50"}},
                {"id": "62", "name": "Gestión del Cambio", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff7f50"}},
                
                # Nodos hijos para Storytelling
                {"id": "63", "name": "Narración Estructurada", "category": 1, "symbol": "circle", "itemStyle": {"color": "#87cefa"}},
                {"id": "64", "name": "Engagement del Auditorio", "category": 1, "symbol": "circle", "itemStyle": {"color": "#87cefa"}},
                {"id": "65", "name": "Uso de Metáforas", "category": 1, "symbol": "circle", "itemStyle": {"color": "#87cefa"}},
                {"id": "66", "name": "Comunicación Emocional", "category": 1, "symbol": "circle", "itemStyle": {"color": "#87cefa"}},
                
                # Nodos hijos para Innovación
                {"id": "67", "name": "Pensamiento Creativo", "category": 1, "symbol": "circle", "itemStyle": {"color": "#da70d6"}},
                {"id": "68", "name": "Resolución de Problemas", "category": 1, "symbol": "circle", "itemStyle": {"color": "#da70d6"}},
                {"id": "69", "name": "Fomento de la Innovación", "category": 1, "symbol": "circle", "itemStyle": {"color": "#da70d6"}},
                {"id": "70", "name": "Adopción de Nuevas Ideas", "category": 1, "symbol": "circle", "itemStyle": {"color": "#da70d6"}},
                
                # Nodos hijos para Conversaciones Difíciles
                {"id": "71", "name": "Escucha Activa", "category": 1, "symbol": "circle", "itemStyle": {"color": "#32cd32"}},
                {"id": "72", "name": "Gestión de Conflictos", "category": 1, "symbol": "circle", "itemStyle": {"color": "#32cd32"}},
                {"id": "73", "name": "Comunicación Clara", "category": 1, "symbol": "circle", "itemStyle": {"color": "#32cd32"}},
                {"id": "74", "name": "Empatía en la Comunicación", "category": 1, "symbol": "circle", "itemStyle": {"color": "#32cd32"}},
                
                # Nodos hijos para Empatía
                {"id": "75", "name": "Comprensión Emocional", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ffa500"}},
                {"id": "76", "name": "Conexión Humana", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ffa500"}},
                {"id": "77", "name": "Perspectiva de los Demás", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ffa500"}},
                {"id": "78", "name": "Asertividad Empática", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ffa500"}},
                
                # Nodos hijos para Confianza
                {"id": "79", "name": "Construcción de Relaciones", "category": 1, "symbol": "circle", "itemStyle": {"color": "#9370db"}},
                {"id": "80", "name": "Integridad Personal", "category": 1, "symbol": "circle", "itemStyle": {"color": "#9370db"}},
                {"id": "81", "name": "Transparencia", "category": 1, "symbol": "circle", "itemStyle": {"color": "#9370db"}},
                {"id": "82", "name": "Consistencia", "category": 1, "symbol": "circle", "itemStyle": {"color": "#9370db"}},
                
                # Nodos hijos para Delegar
                {"id": "83", "name": "Definición de Roles", "category": 1, "symbol": "circle", "itemStyle": {"color": "#3cb371"}},
                {"id": "84", "name": "Delegación Efectiva", "category": 1, "symbol": "circle", "itemStyle": {"color": "#3cb371"}},
                {"id": "85", "name": "Seguimiento y Supervisión", "category": 1, "symbol": "circle", "itemStyle": {"color": "#3cb371"}},
                {"id": "86", "name": "Responsabilidad Compartida", "category": 1, "symbol": "circle", "itemStyle": {"color": "#3cb371"}},
                
                # Nodos hijos para Reconocer
                {"id": "87", "name": "Apreciación del Trabajo", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff6347"}},
                {"id": "88", "name": "Reconocimiento Público", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff6347"}},
                {"id": "89", "name": "Feedback Constructivo", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff6347"}},
                {"id": "90", "name": "Recompensas y Beneficios", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff6347"}},
            ],
            "links": [
                # Relaciones para Liderazgo
                {"source": "51", "target": "59"},
                {"source": "51", "target": "60"},
                {"source": "51", "target": "61"},
                {"source": "51", "target": "62"},
                {"source": "51", "target": "56"},
                {"source": "51", "target": "58"},
                {"source": "51", "target": "54"},
                {"source": "51", "target": "55"},
                
                # Relaciones para Storytelling
                {"source": "52", "target": "63"},
                {"source": "52", "target": "64"},
                {"source": "52", "target": "65"},
                {"source": "52", "target": "66"},
                
                # Relaciones para Innovación
                {"source": "53", "target": "67"},
                {"source": "53", "target": "68"},
                {"source": "53", "target": "69"},
                {"source": "53", "target": "70"},
                
                # Relaciones para Conversaciones Difíciles
                {"source": "54", "target": "71"},
                {"source": "54", "target": "72"},
                {"source": "54", "target": "73"},
                {"source": "54", "target": "74"},
                
                # Relaciones para Empatía
                {"source": "55", "target": "75"},
                {"source": "55", "target": "76"},
                {"source": "55", "target": "77"},
                {"source": "55", "target": "78"},
                
                # Relaciones para Confianza
                {"source": "56", "target": "79"},
                {"source": "56", "target": "80"},
                {"source": "56", "target": "81"},
                {"source": "56", "target": "82"},
                {"source": "56", "target": "57"},
                
                # Relaciones para Delegar
                {"source": "57", "target": "83"},
                {"source": "57", "target": "84"},
                {"source": "57", "target": "85"},
                {"source": "57", "target": "86"},
                
                # Relaciones para Reconocer
                {"source": "58", "target": "87"},
                {"source": "58", "target": "88"},
                {"source": "58", "target": "89"},
                {"source": "58", "target": "90"},

                {"source": "74", "target": "68"},
                {"source": "71", "target": "66"},
            ],
            "categories": [
                {"name": "Habilidades "},
                {"name": "Habilidades Blandas"}
            ]
        }



        # Ajustar el tamaño de los nodos
        for idx, _ in enumerate(graph["nodes"]):
            graph["nodes"][idx]["symbolSize"] = 10  # Aumentar el tamaño para mayor visibilidad

        # Configuración de la visualización
        option = {
            "title": {
                "text": 'Quien soy',
                "subtext": "Default layout",
                "top": "bottom",
                "left": "right",
            },
            "tooltip": {},
            "legend": {
                "data": [
                    # {"name": "Habilidades", "icon": "circle"},
                    {"name": "Habilidades Blandas", "icon": "circle"}
                ]
            },
            "series": [
                {
                    "type": "graph",
                    "layout": "force",
                    "data": graph["nodes"],
                    "links": graph["links"],
                    "categories": graph["categories"],
                    "roam": True,
                    "label": {"position": "right"},
                    "draggable": True,
                    "force": {"repulsion": 100},
                }
            ],
        }

        # Mostrar la visualización en Streamlit
        st_echarts(option, height="500px")

    def Grafico_completo():
        # Datos del grafo
        st.write('Una persona sensata, analítica e innovadora, compasivo y enfocado en los logros, dispuesto a entregar todo de sí y ayudar a construir ')
        
        graph = {
            "nodes": [
                {"id": "1", "name": "SQL", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5470c6"}},  # Azul
                {"id": "2", "name": "Python", "category": 0, "symbol": "rect", "itemStyle": {"color": "#91cc75"}},  # Verde
                {"id": "3", "name": "AWS", "category": 0, "symbol": "rect", "itemStyle": {"color": "#fac858"}},  # Amarillo
                {"id": "4", "name": "Machine Learning", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ca8622"}},  # Naranja
                {"id": "5", "name": "Programación Orientada a Objetos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ee6666"}},  # Rojo
                {"id": "6", "name": "Automatizaciones", "category": 0, "symbol": "rect", "itemStyle": {"color": "#c4ccd3"}},  # Gris
                {"id": "7", "name": "Power BI", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5978bb"}},  # Azul oscuro
                {"id": "8", "name": "Office", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5ab1ef"}},  # Azul claro
                {"id": "9", "name": "Escenarios What-If", "category": 0, "symbol": "rect", "itemStyle": {"color": "#d87a80"}},  # Rojo claro
                {"id": "10", "name": "Computación en la Nube", "category": 0, "symbol": "rect", "itemStyle": {"color": "#919191"}},  # Gris oscuro
                
                # Nodos hijos para SQL
                {"id": "11", "name": "Consultas Avanzadas", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5470c6"}},
                {"id": "12", "name": "Procedimientos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5470c6"}},
                {"id": "13", "name": "Vistas", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5470c6"}},
                {"id": "14", "name": "Diseño Relacional", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5470c6"}},
                
                # Nodos hijos para Python
                {"id": "15", "name": "Pandas", "category": 0, "symbol": "rect", "itemStyle": {"color": "#91cc75"}},
                {"id": "16", "name": "NumPy", "category": 0, "symbol": "rect", "itemStyle": {"color": "#91cc75"}},
                # {"id": "17", "name": "Decoradores", "category": 1, "symbol": "rect", "itemStyle": {"color": "#91cc75"}},
                # {"id": "18", "name": "Iteradores y Generadores", "category": 1, "symbol": "rect", "itemStyle": {"color": "#91cc75"}},
                
                # Nodos hijos para AWS
                {"id": "19", "name": "EC2", "category": 0, "symbol": "rect", "itemStyle": {"color": "#fac858"}},
                {"id": "20", "name": "S3", "category": 0, "symbol": "rect", "itemStyle": {"color": "#fac858"}},
                {"id": "21", "name": "Lambda", "category": 0, "symbol": "rect", "itemStyle": {"color": "#fac858"}},
                {"id": "22", "name": "RDS", "category": 0, "symbol": "rect", "itemStyle": {"color": "#fac858"}},
                
                # Nodos hijos para Machine Learning
                {"id": "23", "name": "Modelos Supervisados", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ca8622"}},
                {"id": "24", "name": "Modelos No Supervisados", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ca8622"}},
                {"id": "25", "name": "Validación Cruzada", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ca8622"}},
                {"id": "26", "name": "Overfitting y Underfitting", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ca8622"}},
                
                # Nodos hijos para Programación Orientada a Objetos (OOP)
                {"id": "27", "name": "Clases y Objetos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ee6666"}},
                {"id": "28", "name": "Herencia y Polimorfismo", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ee6666"}},
                {"id": "29", "name": "Encapsulamiento", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ee6666"}},
                # {"id": "30", "name": "Abstracción", "category": 0, "symbol": "rect", "itemStyle": {"color": "#ee6666"}},
                
                # Nodos hijos para Automatizaciones en la Cadena de Suministro
                {"id": "31", "name": "SAP", "category": 0, "symbol": "rect", "itemStyle": {"color": "#c4ccd3"}},
                {"id": "32", "name": "Gestion de datos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#c4ccd3"}},
                {"id": "33", "name": "Documentación", "category": 0, "symbol": "rect", "itemStyle": {"color": "#c4ccd3"}},
                {"id": "34", "name": "Repositorios compartidos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#c4ccd3"}},
                
                # Nodos hijos para Power BI
                {"id": "35", "name": "Transformación de Datos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5978bb"}},
                {"id": "36", "name": "Gateways de Datos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5978bb"}},
                {"id": "37", "name": "DAX (Data Analysis Expressions)", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5978bb"}},
                {"id": "38", "name": "Paneles y Reportes", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5978bb"}},
                
                # Nodos hijos para Office
                {"id": "39", "name": "Excel Avanzado", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5ab1ef"}},
                {"id": "40", "name": "Power Query", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5ab1ef"}},
                {"id": "41", "name": "VBA", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5ab1ef"}},
                {"id": "42", "name": "Documentaciones", "category": 0, "symbol": "rect", "itemStyle": {"color": "#5ab1ef"}},
                
                # Nodos hijos para Escenarios What-If en Power BI
                {"id": "43", "name": "Simulaciones de Escenarios", "category": 0, "symbol": "rect", "itemStyle": {"color": "#d87a80"}},
                {"id": "44", "name": "Análisis de Sensibilidad", "category": 0, "symbol": "rect", "itemStyle": {"color": "#d87a80"}},
                {"id": "45", "name": "Parámetros en Power BI", "category": 0, "symbol": "rect", "itemStyle": {"color": "#d87a80"}},
                {"id": "46", "name": "Escenarios Alternativos", "category": 0, "symbol": "rect", "itemStyle": {"color": "#d87a80"}},
                
                # Nodos hijos para Computación en la Nube
                {"id": "47", "name": "Escalabilidad", "category": 0, "symbol": "rect", "itemStyle": {"color": "#919191"}},
                {"id": "48", "name": "Seguridad en la Nube", "category": 0, "symbol": "rect", "itemStyle": {"color": "#919191"}},
                {"id": "49", "name": "Servicios Web en la Nube", "category": 0, "symbol": "rect", "itemStyle": {"color": "#919191"}},
                {"id": "50", "name": "Big Data", "category": 0, "symbol": "rect", "itemStyle": {"color": "#919191"}},
                
                {"id": "51", "name": "Liderazgo", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff7f50"}},  # Coral
                {"id": "52", "name": "Storytelling", "category": 1, "symbol": "circle", "itemStyle": {"color": "#87cefa"}},  # Azul cielo
                {"id": "53", "name": "Innovación", "category": 1, "symbol": "circle", "itemStyle": {"color": "#da70d6"}},  # Orquídea
                {"id": "54", "name": "Conversaciones Difíciles", "category": 1, "symbol": "circle", "itemStyle": {"color": "#32cd32"}},  # Verde lima
                {"id": "55", "name": "Empatía", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ffa500"}},  # Naranja
                {"id": "56", "name": "Confianza", "category": 1, "symbol": "circle", "itemStyle": {"color": "#9370db"}},  # Púrpura medio
                {"id": "57", "name": "Delegar", "category": 1, "symbol": "circle", "itemStyle": {"color": "#3cb371"}},  # Verde mar
                {"id": "58", "name": "Reconocer", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff6347"}},  # Tomate
                
                # Nodos hijos para Liderazgo
                {"id": "59", "name": "Visión Estratégica", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff7f50"}},
                {"id": "60", "name": "Toma de Decisiones", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff7f50"}},
                {"id": "61", "name": "Motivación de Equipos", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff7f50"}},
                {"id": "62", "name": "Gestión del Cambio", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff7f50"}},
                
                # Nodos hijos para Storytelling
                {"id": "63", "name": "Narración Estructurada", "category": 1, "symbol": "circle", "itemStyle": {"color": "#87cefa"}},
                {"id": "64", "name": "Engagement del Auditorio", "category": 1, "symbol": "circle", "itemStyle": {"color": "#87cefa"}},
                {"id": "65", "name": "Uso de Metáforas", "category": 1, "symbol": "circle", "itemStyle": {"color": "#87cefa"}},
                {"id": "66", "name": "Comunicación Emocional", "category": 1, "symbol": "circle", "itemStyle": {"color": "#87cefa"}},
                
                # Nodos hijos para Innovación
                {"id": "67", "name": "Pensamiento Creativo", "category": 1, "symbol": "circle", "itemStyle": {"color": "#da70d6"}},
                {"id": "68", "name": "Resolución de Problemas", "category": 1, "symbol": "circle", "itemStyle": {"color": "#da70d6"}},
                {"id": "69", "name": "Fomento de la Innovación", "category": 1, "symbol": "circle", "itemStyle": {"color": "#da70d6"}},
                {"id": "70", "name": "Adopción de Nuevas Ideas", "category": 1, "symbol": "circle", "itemStyle": {"color": "#da70d6"}},
                
                # Nodos hijos para Conversaciones Difíciles
                {"id": "71", "name": "Escucha Activa", "category": 1, "symbol": "circle", "itemStyle": {"color": "#32cd32"}},
                {"id": "72", "name": "Gestión de Conflictos", "category": 1, "symbol": "circle", "itemStyle": {"color": "#32cd32"}},
                {"id": "73", "name": "Comunicación Clara", "category": 1, "symbol": "circle", "itemStyle": {"color": "#32cd32"}},
                {"id": "74", "name": "Empatía en la Comunicación", "category": 1, "symbol": "circle", "itemStyle": {"color": "#32cd32"}},
                
                # Nodos hijos para Empatía
                {"id": "75", "name": "Comprensión Emocional", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ffa500"}},
                {"id": "76", "name": "Conexión Humana", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ffa500"}},
                {"id": "77", "name": "Perspectiva de los Demás", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ffa500"}},
                {"id": "78", "name": "Asertividad Empática", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ffa500"}},
                
                # Nodos hijos para Confianza
                {"id": "79", "name": "Construcción de Relaciones", "category": 1, "symbol": "circle", "itemStyle": {"color": "#9370db"}},
                {"id": "80", "name": "Integridad Personal", "category": 1, "symbol": "circle", "itemStyle": {"color": "#9370db"}},
                {"id": "81", "name": "Transparencia", "category": 1, "symbol": "circle", "itemStyle": {"color": "#9370db"}},
                {"id": "82", "name": "Consistencia", "category": 1, "symbol": "circle", "itemStyle": {"color": "#9370db"}},
                
                # Nodos hijos para Delegar
                {"id": "83", "name": "Definición de Roles", "category": 1, "symbol": "circle", "itemStyle": {"color": "#3cb371"}},
                {"id": "84", "name": "Delegación Efectiva", "category": 1, "symbol": "circle", "itemStyle": {"color": "#3cb371"}},
                {"id": "85", "name": "Seguimiento y Supervisión", "category": 1, "symbol": "circle", "itemStyle": {"color": "#3cb371"}},
                {"id": "86", "name": "Responsabilidad Compartida", "category": 1, "symbol": "circle", "itemStyle": {"color": "#3cb371"}},
                
                # Nodos hijos para Reconocer
                {"id": "87", "name": "Apreciación del Trabajo", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff6347"}},
                {"id": "88", "name": "Reconocimiento Público", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff6347"}},
                {"id": "89", "name": "Feedback Constructivo", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff6347"}},
                {"id": "90", "name": "Recompensas y Beneficios", "category": 1, "symbol": "circle", "itemStyle": {"color": "#ff6347"}},
            
            
            ],
            "links": [
                # Relaciones para SQL
                {"source": "1", "target": "11"},
                {"source": "1", "target": "12"},
                {"source": "1", "target": "13"},
                {"source": "1", "target": "14"},
                {"source": "1", "target": "22"},
                {"source": "1", "target": "35"},
                
                # Relaciones para Python
                {"source": "2", "target": "15"},
                {"source": "2", "target": "16"},
                {"source": "2", "target": "17"},
                {"source": "2", "target": "18"},
                {"source": "2", "target": "5"},
                {"source": "2", "target": "6"},
                {"source": "2", "target": "4"},
                
                # Relaciones para AWS
                {"source": "3", "target": "19"},
                {"source": "3", "target": "20"},
                {"source": "3", "target": "21"},
                {"source": "3", "target": "22"},
                {"source": "3", "target": "47"},
                {"source": "3", "target": "4"},
                
                # Relaciones para Machine Learning
                {"source": "4", "target": "23"},
                {"source": "4", "target": "24"},
                {"source": "4", "target": "25"},
                {"source": "4", "target": "26"},
                
                # Relaciones para Programación Orientada a Objetos (OOP)
                {"source": "5", "target": "27"},
                {"source": "5", "target": "28"},
                {"source": "5", "target": "29"},
                {"source": "5", "target": "30"},
                
                # Relaciones para Automatizaciones en la Cadena de Suministro
                {"source": "6", "target": "31"},
                {"source": "6", "target": "32"},
                {"source": "6", "target": "33"},
                {"source": "6", "target": "34"},
                {"source": "6", "target": "41"},
                {"source": "6", "target": "36"},
                
                # Relaciones para Power BI
                {"source": "7", "target": "35"},
                {"source": "7", "target": "36"},
                {"source": "7", "target": "37"},
                {"source": "7", "target": "38"},
                
                # Relaciones para Office
                {"source": "8", "target": "39"},
                {"source": "8", "target": "40"},
                {"source": "8", "target": "41"},
                {"source": "8", "target": "42"},
                
                # Relaciones para Escenarios What-If en Power BI
                {"source": "9", "target": "43"},
                {"source": "9", "target": "44"},
                {"source": "9", "target": "45"},
                {"source": "9", "target": "46"},
                
                # Relaciones para Computación en la Nube
                {"source": "10", "target": "47"},
                {"source": "10", "target": "48"},
                {"source": "10", "target": "49"},
                {"source": "10", "target": "50"},
                
                # Relaciones cruzadas si aplican
                {"source": "1", "target": "32"},
                {"source": "6", "target": "34"},
                {"source": "7", "target": "45"},
                {"source": "9", "target": "49"},

            # Relaciones para Liderazgo
                {"source": "51", "target": "59"},
                {"source": "51", "target": "60"},
                {"source": "51", "target": "61"},
                {"source": "51", "target": "62"},
                {"source": "51", "target": "56"},
                {"source": "51", "target": "58"},
                {"source": "51", "target": "54"},
                {"source": "51", "target": "55"},
                
                # Relaciones para Storytelling
                {"source": "52", "target": "63"},
                {"source": "52", "target": "64"},
                {"source": "52", "target": "65"},
                {"source": "52", "target": "66"},
                
                # Relaciones para Innovación
                {"source": "53", "target": "67"},
                {"source": "53", "target": "68"},
                {"source": "53", "target": "69"},
                {"source": "53", "target": "70"},
                
                # Relaciones para Conversaciones Difíciles
                {"source": "54", "target": "71"},
                {"source": "54", "target": "72"},
                {"source": "54", "target": "73"},
                {"source": "54", "target": "74"},
                
                # Relaciones para Empatía
                {"source": "55", "target": "75"},
                {"source": "55", "target": "76"},
                {"source": "55", "target": "77"},
                {"source": "55", "target": "78"},
                
                # Relaciones para Confianza
                {"source": "56", "target": "79"},
                {"source": "56", "target": "80"},
                {"source": "56", "target": "81"},
                {"source": "56", "target": "82"},
                {"source": "56", "target": "57"},
                
                # Relaciones para Delegar
                {"source": "57", "target": "83"},
                {"source": "57", "target": "84"},
                {"source": "57", "target": "85"},
                {"source": "57", "target": "86"},
                
                # Relaciones para Reconocer
                {"source": "58", "target": "87"},
                {"source": "58", "target": "88"},
                {"source": "58", "target": "89"},
                {"source": "58", "target": "90"},

                {"source": "74", "target": "68"},
                {"source": "71", "target": "66"}, 
                
                {"source": "52", "target": "9"}, 
                {"source": "2", "target": "53"}, 
                {"source": "57", "target": "6"}, 
            ],
            "categories": [
                {"name": "Conocimientos Técnicos"},
                {"name": "Habilidades Blandas"}
            ]
        }



        # Ajustar el tamaño de los nodos
        for idx, _ in enumerate(graph["nodes"]):
            graph["nodes"][idx]["symbolSize"] = 10  # Aumentar el tamaño para mayor visibilidad

        # Configuración de la visualización
        option = {
            "title": {
                "text": 'Quien soy',
                "subtext": "Default layout",
                "top": "bottom",
                "left": "right",
            },
            "tooltip": {},
            "legend": {
                "data": [
                    {"name": "Habilidades Blandas", "icon": "circle"},
                    {"name": "Conocimientos Técnicos", "icon": "rect"}
                ]
            },
            "series": [
                {
                    "type": "graph",
                    "layout": "force",
                    "data": graph["nodes"],
                    "links": graph["links"],
                    "categories": graph["categories"],
                    "roam": True,
                    "label": {"position": "right"},
                    "draggable": True,
                    "force": {"repulsion": 100},
                }
            ],
        }

        # Mostrar la visualización en Streamlit
        st_echarts(option, height="800px")


    if opcion_seleccionada == "Desde lo humano":
        Grafico_blando()
    elif opcion_seleccionada == "Desde lo técnico":
        Grafico_tecnico()
    elif opcion_seleccionada == "Integralmente":
        Grafico_completo()

def mostrar_logros():
    import pandas as pd
    opcion_seleccionada = st.selectbox(
    "Qué enfoque ver:",
    ("Desde lo técnico", "Desde lo humano"))

    if opcion_seleccionada == "Desde lo humano":
        st.markdown(f"**Vivir tranquilo**")
        st.markdown(f'Aprender a vivir valorando mis defectos y fortalezas, agradeciendo por lo que tengo y trabajando por lo que quiero')
        st.markdown(f"**Vivir solo**")
        st.markdown(f'Uno de los procesos mas duros e inesperados pero de las mejore experiencias para mi crecimiento')
        st.markdown(f"**Disfrutar mi trabajo**")
        st.markdown(f'Tras una construcción y deconstrución aprendí que hay momentos duros, que son estos los que mas aportan')
        st.markdown(f"**Tener una vida en equilibrio**")
        st.markdown(f'Aprender a separar espacios, tiempos, querer en cierta medida la rutina y valorar mi salud')
        st.markdown(f"**Poder tener mis gustos y ayudar a las personas**")
        st.markdown(f'Disfrutar del fruto del trabajo y la satisfacción del deber cumplido')
        st.markdown(f"**Hacer sentir orgulloso a mis padres**")
        st.markdown(f'El día que escuché estas palabras entendí que había hecho lo que tanto quería')
    elif opcion_seleccionada == "Desde lo técnico":
        # Definir los datos de ejemplo
        data = {
            "Logro": [
                "HUB Medellin", 
                "Nearshoring", 
                "Automatizador", 
                "Iniciativa de capacitación", 
                "Liderazgo celulas de trabajo"
            ],
            "Contexto": [
                "Analisis de prefactibilidad para modificar modelo de transporte primario en secos para todo grupo"
                ,"Evaluar Flujos de bastecimiento"
                ,"Integración de varias herramientas en una ejecución automatica de informes"
                ,"Creación de capacitaciones en el negocio para el negocio"
                ,"El equipo se divide en celulas de trabajo, cada uno con diferentes objetivos"],

            "Aprendizaje": [
                "Gestión de conocimiento y seguimiento a desarrollo ejecutado por un proveedor externo",
                "Mejorar la comunicación, validando expectativas e información para desarrollo de lógicas y proyectos"
                ,"Liderazgo, confianza, seguimiento, gestión de iniciativas e industrialización de desarrollos"
                ,"Identificación de necesidades de conocimiento y generación de espacios para transmitir conocimiento  "
                ,"Confianza en los demás, seguimiento a iniciativas, comunicación y reuniones efectivas, tener empatia y ayudar a seleccionar practiacntes, gestión por OKR"]
        }
        df = pd.DataFrame(data)

        # Crear el DataFrame
        for index, row in df.iterrows():
            st.markdown(f"### {row['Logro']}")
            st.markdown(f"**Contexto:** {row['Contexto']}")
            st.markdown(f"**Aprendizaje:** {row['Aprendizaje']}\n")


st.sidebar.header("Navegación")
page = st.sidebar.radio("Ir a:", ["Quien soy", "Principales Logros"])
if page == "Quien soy":
    mostrar_quien_soy()
elif page == "Principales Logros":
    mostrar_logros()

