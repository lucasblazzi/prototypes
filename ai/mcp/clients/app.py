import streamlit as st

# Set page title and layout
st.set_page_config(page_title="ChatGPT-powered Chat", layout="centered")

st.title("ChatGPT-powered Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input box and submit button
user_input = st.text_input("Your message:", key="user_input")
if st.button("Send"):
    if user_input:
        # Display user message in chat
        with st.chat_message("user"):
            st.markdown(user_input)
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Generate assistant response (replace this with actual GPT model call)
        with st.spinner("Thinking..."):
            # Example: replace the following line with your GPT backend call, e.g.:
            # response = chatbot.process_query(user_input)
            response = f"Echo: {user_input}"

        # Display assistant response in chat
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Clear input box for next message
        st.session_state.user_input = ""
