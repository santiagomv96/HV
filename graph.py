import json
import streamlit as st
from streamlit_echarts import st_echarts

# Datos del grafo
graph = {
    "nodes": [
        {"id": "1", "name": "Jean Valjean", "category": 0},
        {"id": "2", "name": "Javert", "category": 1},
        {"id": "3", "name": "Fantine", "category": 0},
        {"id": "4", "name": "Cosette", "category": 0},
        {"id": "5", "name": "Marius", "category": 1}
        # Más nodos...
    ],
    "links": [
        {"source": "1", "target": "2"},
        {"source": "1", "target": "3"},
        {"source": "3", "target": "4"},
        {"source": "4", "target": "5"}
        # Más enlaces...
    ],
    "categories": [
        {"name": "Protagonistas"},
        {"name": "Antagonistas"}
        # Más categorías...
    ]
}

# Ajustar el tamaño de los nodos
for idx, _ in enumerate(graph["nodes"]):
    graph["nodes"][idx]["symbolSize"] = 5

# Configuración de la visualización
option = {
    "title": {
        "text": "Les Miserables",
        "subtext": "Default layout",
        "top": "bottom",
        "left": "right",
    },
    "tooltip": {},
    "legend": [{"data": [a["name"] for a in graph["categories"]]}],
    "series": [
        {
            "name": "Les Miserables",
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
