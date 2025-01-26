#!/usr/bin/env python
# coding: utf-8

# # app

# In[1]:


import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

# Beispiel-Daten
diff_data_midi = pd.read_csv("diff_data_midi.csv")
midi_data_df = pd.read_csv("midi_data_df.csv")
rt_data_df = pd.read_csv("rt_data_df.csv")
means_df = pd.read_csv("mean_rt_by_sound.csv")

conditions = [
    "faces_left_faces_right",
    "words_left_words_right",
    "faces_left_words_left",
    "faces_right_words_right",
    "faces_right_words_left",
    "faces_left_words_right"
]
sound_conditions = ["normal", "aesth"]

# Farben und Stile für Mittelwertlinien
sound_type_colors = {'normal': '#0072B2', 'aesth': '#D55E00'}
linestyles = {"normal": "dash", "aesth": "dot"}

# App erstellen
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Sonification of EEG Data", className="text-center mb-4"), width=12)
    ]),

    # Hinweiskasten a
    dbc.Row([
        dbc.Col(
            dbc.Alert(
                "Wählen Sie in den Dropdown-Menüs eine Bedingungskombination und einen Klangtyp aus. "
                "Spielen Sie den Sound ausgewählten Sound ab. "
                "Der linke Graph zeigt die absolute Differenz zwischen den MIDI-Noten der ausgewählten Bedingungskombination über die Zeit. "
                "Der rechte Graph zeigt die beiden MIDI-Noten-Verläufe, die in dem Sound kombiniert wurden, den Sie ausgewählt haben. "
                "Nutzen Sie die Optionen, um die Reaktionszeitpunkte der Versuchspersonen als Histogramme und Mittelwerte einzublenden.",
                color="info"
            ), width=12
        )
    ]),
    
    # Dropdowns
    dbc.Row([
        dbc.Col([
            html.Label("Bedingung auswählen"),
            dcc.Dropdown(
                id="condition-dropdown",
                options=[{"label": condition, "value": condition} for condition in conditions],
                value=conditions[0],
                clearable=False
            )
        ], width=6),
        dbc.Col([
            html.Label("Sound-Bedingung auswählen"),
            dcc.Dropdown(
                id="sound-condition-dropdown",
                options=[{"label": sc, "value": sc} for sc in sound_conditions],
                value=sound_conditions[0],
                clearable=False
            )
        ], width=6)
    ], className="mb-4"),
    
    # Audio Player
    dbc.Row([
        dbc.Col(html.Audio(id="audio-player", controls=True, style={"width": "100%"}), width=12)
    ], className="mb-4"),

    # Histogram- und Mittelwert-Schalter
    dbc.Row([
        dbc.Col(
            dbc.Checkbox(
                id="toggle-histogram",
                label="Histogram einblenden",
                value=False,
                className="mb-2"
            ), width=6
        ),
        dbc.Col(
            dbc.Checkbox(
                id="toggle-means",
                label="Mittelwerte einblenden",
                value=False,
                className="mb-2"
            ), width=6
        ),
    ]),

    # Graphen
    dbc.Row([
        dbc.Col(dcc.Graph(id="diff-graph", style={"height": "400px"}), width=6),
        dbc.Col(dcc.Graph(id="midi-graph", style={"height": "400px"}), width=6)
    ], className="mb-4"),

# Hinweiskasten b
    dbc.Row([
        dbc.Col(
            dbc.Alert(
                "Hier können Sie sich die statistischen Kennwerte der Reaktionszeitpunkt-Daten anschauen. "
                "Die Boxplots zeigen die Verteilung der Reaktipnszeitpunkte pro Sound. "
                "Fahren Sie mit dem Mauszeiger über die Grafik, um Median, Minimum, Maximum, Quartile und Extremwerte einzusehen. "
                "Die Tabellen enthalten deskriptive Statistiken für die beiden abhängigen Variablen. ",
                color="info"
            ), width=12
        )
    ]),

# Boxplot
    dbc.Row([
        dbc.Col(
            html.Div([
                html.H2("Boxplots Reaktionszeiten pro Sound", className="text-center mb-4"),
                html.Iframe(
                    src="/assets/boxplot_interactive.html",
                    style={"width": "100%", "height": "700px", "border": "none"}
                )
            ]), width=12
        )
    ]),
    
    # Hinweiskasten c
    dbc.Row([
        dbc.Col(
            dbc.Alert(
                "Die Flowchart visualisiert unsere Hypothesen und unseren methodischen Ansatz. "
                "Die Tabellen enthalten deskriptive Statistiken für die beiden abhängigen Variablen. ",
                color="info"
            ), width=12
        )
    ]),
    
# Bild Hypothesen
    dbc.Row([
        dbc.Col(html.Img(src="/assets/flowchart_avn_hypothesen.png", style={"width": "100%"}), width=12)
    ]),

# Bilder Tabellen Deskriptivstatistik
    dbc.Row([
        dbc.Col(html.Img(src="/assets/tabelle_abs_diff.png", style={"width": "100%"}), width=6),
        dbc.Col(html.Img(src="/assets/tabelle_in_interval_ratio.png", style={"width": "100%"}), width=6)
    ]),

# Hinweiskasten d
    dbc.Row([
        dbc.Col(
            dbc.Alert(
                "Die Interaktion der Faktoren Stimulus und Klangtyp auf die beiden abhängigen Variablen abs_diff und in_interval_ratio können Sie diesen Grafiken entnehmen. "
                "// Kleine Interpretationshilfe: Höhere Werte in in_interval_ratio entsprechen einem höheren Anteil an Reaktionszeitpunkten innerhalb der Intervalle, in denen sich die Differenz der Sound-Kurven deutlich verändert. "
                "Im Kontrast dazu entsprechen höhere Werte in abs_diff einer späteren, also langsameren Reaktion. Je größer der Wert von abs_diff, desto größer ist der mittlere Abstand der Reaktionszeitpunkte zu dem ersten Zeitpunkt deutlicher Differenzveränderungen zwischen den Sound-Kurven. "
                "Tiefergehende Informationen zum methodischen Vorgehen und der statistischen Analyse finden Sie auf unserem Poster. Sprechen Sie uns bei Fragen gerne auch jederzeit an! ",
                color="info"
            ), width=12
        )
    ]),

# Bilder Interaktionsdiagramme
    dbc.Row([
        dbc.Col(html.Img(src="/assets/interaction_in_interval_ratio.png", style={"width": "100%"}), width=6),
        dbc.Col(html.Img(src="/assets/interaction_abs_diff.png", style={"width": "100%"}), width=6)
    ]),

# Hinweiskasten e (PDF Anzeige und Download)
    dbc.Row([
        dbc.Col(
            dbc.Alert(
                "Hier können Sie unser Poster als PDF-Datei einsehen und herunterladen.",
                color="info"
            ), width=12
        )
    ]),
    dbc.Row([
        # PDF-Anzeige
        dbc.Col(
            html.Iframe(
                src="/assets/empra_poster.pdf",  # Link zur PDF
                style={"width": "100%", "height": "600px", "border": "none"}
            ), width=12
        )
    ]),
    dbc.Row([
    # Download-Link
        dbc.Col(
            html.A(
                "PDF herunterladen",
                href="/assets/empra_poster.pdf",  # Direktlink zur Datei
                download="empra_poster.pdf",  # Dateiname für den Download
                className="btn btn-primary mt-3"  # Bootstrap-Button
            ), width=12
        )
    ])], fluid=False)

# Callbacks für Graphen
@app.callback(
    [Output("audio-player", "src"),
     Output("diff-graph", "figure"),
     Output("midi-graph", "figure")],
    [Input("condition-dropdown", "value"),
     Input("sound-condition-dropdown", "value"),
     Input("toggle-histogram", "value"),
     Input("toggle-means", "value")]
)
def update_graphs(selected_condition, selected_sound_condition, show_histogram, show_means):
    audio_path = f"assets/sounds/{selected_condition}_{selected_sound_condition}.wav"
    # Maximalen y-Wert für diff_data_midi berechnen
    ymax_diff = diff_data_midi[conditions].max().max()

    # --- Absolute Differences Graph ---
    fig_diff = go.Figure()
    fig_diff.add_trace(go.Scatter(
        x=diff_data_midi["time"],
        y=diff_data_midi[selected_condition],
        mode="lines",
        name=f"diff {selected_condition}",
        line=dict(color='darkslateblue', width=1.5)
    ))

    # Histogram hinzufügen (eigene y-Achse)
    if show_histogram:
        hist_y = rt_data_df[f"{selected_condition}_{selected_sound_condition}"]
        fig_diff.add_trace(go.Histogram(
            x=hist_y,
            name="Reaktionszeitpunkte",
            marker=dict(color='skyblue', line=dict(color='darkblue', width=1)),
            opacity=0.6,
            xbins=dict(size=10),  # Breite der Balken
            yaxis="y2"
        ))

    # Mittelwertlinien
    if show_means:
        for sound_type, color in sound_type_colors.items():
            mean_value = means_df.loc[
                (means_df['condition'] == selected_condition) &
                (means_df['sound_type'] == sound_type), 'mean_RT'
            ].values
            if mean_value.size > 0:
                fig_diff.add_trace(go.Scatter(
                    x=[mean_value[0], mean_value[0]],
                    y=[0, ymax_diff],
                    mode="lines",
                    name=f"{sound_type} mean",
                    line=dict(color=color, dash=linestyles[sound_type], width=2)
                ))

    fig_diff.update_layout(
        title="Absolute Differences",
        xaxis_title="Time (ms)",
        yaxis=dict(title="Absolute Difference", range=[0, ymax_diff]),
        yaxis2=dict(
            title="Häufigkeit",
            overlaying="y",
            side="right",
            showgrid=False
        ),
        legend=dict(orientation="h", yanchor="top", y=-0.3),
        template="plotly_white"
    )

    # --- MIDI Graph ---
    condition_mapping = {
        "faces_left_faces_right": ["faces_left", "faces_right"],
        "words_left_words_right": ["words_left", "words_right"],
        "faces_left_words_left": ["faces_left", "words_left"],
        "faces_right_words_right": ["faces_right", "words_right"],
        "faces_right_words_left": ["faces_right", "words_left"],
        "faces_left_words_right": ["faces_left", "words_right"]
    }
    line_1, line_2 = condition_mapping[selected_condition]

    fig_midi = go.Figure()
    fig_midi.add_trace(go.Scatter(
        x=midi_data_df["time"],
        y=midi_data_df[line_1],
        mode="lines",
        name=line_1,
        line=dict(color="#1b9e77", width=1.5)
    ))
    fig_midi.add_trace(go.Scatter(
        x=midi_data_df["time"],
        y=midi_data_df[line_2],
        mode="lines",
        name=line_2,
        line=dict(color="#e7298a", width=1.5)
    ))

    # Histogram hinzufügen (eigene y-Achse)
    if show_histogram:
        hist_y = rt_data_df[f"{selected_condition}_{selected_sound_condition}"]
        fig_midi.add_trace(go.Histogram(
            x=hist_y,
            name="Reaktionszeitpunkte",
            marker=dict(color='skyblue', line=dict(color='darkblue', width=1)),
            opacity=0.6,
            xbins=dict(size=10),  # Breite der Balken
            yaxis="y2"
        ))

    # Mittelwertlinien
    if show_means:
        for sound_type, color in sound_type_colors.items():
            mean_value = means_df.loc[
                (means_df['condition'] == selected_condition) &
                (means_df['sound_type'] == sound_type), 'mean_RT'
            ].values
            if mean_value.size > 0:
                fig_midi.add_trace(go.Scatter(
                    x=[mean_value[0], mean_value[0]],
                    y=[min(midi_data_df[line_1].min(), midi_data_df[line_2].min()), max(midi_data_df[line_1].max(), midi_data_df[line_2].max())],
                    mode="lines",
                    name=f"{sound_type} mean",
                    line=dict(color=color, dash=linestyles[sound_type], width=2)
                ))

    fig_midi.update_layout(
        title="MIDI Note Number Curve",
        xaxis_title="Time (ms)",
        yaxis=dict(title="MIDI Note Number"),
        yaxis2=dict(
            title="Häufigkeit",
            overlaying="y",
            side="right",
            showgrid=False
        ),
        legend=dict(orientation="h", yanchor="top", y=-0.3),
        template="plotly_white"
    )

    return audio_path, fig_diff, fig_midi


if __name__ == "__main__":
    app.run_server(debug=True)

