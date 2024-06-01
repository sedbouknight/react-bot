# ReactBot

ReactBot is a chatbot project developed using React and FastAPI, integrating OpenAI's Whisper API using Chat GPT-4o backend and Eleven Labs' Text-to-Speech (TTS) API. It functions as a digital research assistant, particularly in the field of organic chemistry. However, it can be modified for any task.

## Demo
<video width="600" controls>
  <source src="https://github.com/slbouknight/react-bot/blob/main/assets/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

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

2. **Backend Setup**:
    - On Windows:
      ```bash
      cd backend
      python -m venv venv
      .\venv\Scripts\activate
      pip install openai==0.27.0 python-decouple==3.8 python-multipart==0.0.6 requests==2.28.2 fastapi==0.92.0 "uvicorn[standard]"
      ```

3. **Frontend Setup**:
    - On Windows:
      ```bash
      cd frontend
      yarn create vite .
      Select React and TypeScript when prompted
      yarn --exact
      ```

4. **Set Up Environment Variables**:
    Modify `.env` file in the `backend` directory and add your API keys. Requires free or possibly paid subscription to OpenAI and Eleven Labs APIs.
    ```plaintext
    OPEN_AI_ORG=your_openai_org_id
    OPEN_AI_KEY=your_openai_api_key
    ELEVEN_LABS_API_KEY=your_elevenlabs_api_key
    ```

5. **Run the Application Locally**:
   Activate backend in terminal
    ```bash
    cd backend
    uvicorn main:app
    ```
    Activate frontend in separate terminal
   ```bash
   cd frontend
   yarn build
   yarn start
    ```
   Go to the localhost link displayed after yarn start and app will be running

## Usage
Press the record button and start speaking your prompt into the microphone. Once you're done click the button again to stop recording, and ReactBot will respond.
Audio playback is also available for you and ReactBot's messages between each other.
Refresh button at the top right will clear conversation history.


