import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

# Initialize app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Simple chatbot logic (replace with LLM later)
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hey there! 👋 How can I help you today?"
    elif "data" in user_input:
        return "I can help you visualize and analyze data 📊"
    elif "bye" in user_input:
        return "Goodbye! Have a great day 😊"
    else:
        return "I'm a simple bot 🤖 — try saying 'hello', 'data', or 'bye'!"

# Layout
app.layout = dbc.Container([

    dbc.Row([
        dbc.Col(html.H2("🤖 Smart Chatbot", className="text-center mb-4"), width=12)
    ]),

    # Chat display
    dbc.Row([
        dbc.Col(
            html.Div(id='chat-box', children=[], style={
                "height": "400px",
                "overflowY": "auto",
                "padding": "10px",
                "border": "1px solid #444",
                "borderRadius": "10px",
                "backgroundColor": "#1e1e1e"
            }),
            width=12
        )
    ], className="mb-3"),

    # Input + Button
    dbc.Row([
        dbc.Col(
            dcc.Input(
                id='user-input',
                type='text',
                placeholder='Type your message...',
                className="form-control"
            ),
            width=10
        ),
        dbc.Col(
            dbc.Button("Send", id='send-btn', color="primary", className="w-100"),
            width=2
        )
    ]),

    # Store chat history
    dcc.Store(id='chat-history', data=[])

], fluid=True, className="p-4")


# Callback
@app.callback(
    Output('chat-box', 'children'),
    Output('chat-history', 'data'),
    Input('send-btn', 'n_clicks'),
    State('user-input', 'value'),
    State('chat-history', 'data'),
    prevent_initial_call=True
)
def update_chat(n_clicks, user_input, history):

    if not user_input:
        return dash.no_update, history

    bot_reply = get_bot_response(user_input)

    # Append messages
    history.append({"user": user_input, "bot": bot_reply})

    chat_elements = []
    for chat in history:
        chat_elements.append(html.Div([
            html.Div(f"You: {chat['user']}", style={
                "textAlign": "right",
                "color": "#00d4ff",
                "margin": "5px"
            }),
            html.Div(f"Bot: {chat['bot']}", style={
                "textAlign": "left",
                "color": "#ffffff",
                "margin": "5px"
            })
        ]))

    return chat_elements, history


if __name__ == '__main__':
    app.run(debug=True)
