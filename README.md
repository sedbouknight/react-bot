# ReactBot

ReactBot is a chatbot project developed using React and FastAPI, integrating OpenAI's Whisper API using GPT-4o backend and Eleven Labs' Text-to-Speech (TTS) API. It functions as a digital research assistant, particularly in the field of organic chemistry. However, it can be modified for any task.

## Demo

## Features
- Organic Chemistry Help
- Scientific experiment suggestions
- Voice-enabled interactions

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/slbouknight/react-bot.git
    cd react-bot
    ```

2. **Activate the Provided Virtual Environment**:
    - On Windows:
      ```bash
      cd backend
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      cd backend
      source venv/bin/activate
      ```

3. **Verify the Virtual Environment**:
    ```bash
    pip list
    ```

4. **Set Up Environment Variables**:
    Modify `.env` file in the `backend` directory and add your API keys. Requires free or possibly paid subscription to OpenAI and Eleven Labs APIs.
    ```plaintext
    OPEN_AI_ORG=your_openai_org_id
    OPEN_AI_KEY=your_openai_api_key
    ELEVEN_LABS_API_KEY=your_elevenlabs_api_key
    ```

5. **Run the Application**:
    ```bash
    uvicorn main:app --reload
    ```

## Usage
