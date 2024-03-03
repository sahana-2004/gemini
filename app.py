from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    video_link = data.get('videoLink', '')

    # You should implement a function to fetch the YouTube video transcript.
    # For simplicity, let's assume you have a function get_transcript(video_link)
    # that returns the transcript as a string.

    transcript = get_transcript(video_link)

    if not transcript:
        return jsonify({'error': 'Failed to fetch transcript'})

    # Use OpenAI GPT-3 for more advanced summarization
    prompt = f"Summarize the following YouTube video transcript:\n{transcript}\n\nSummary:"
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the text-davinci-003 engine for GPT-3
            prompt=prompt,
            temperature=0.7,
            max_tokens=150
        )
        
        summarized_text = response.choices[0].text.strip()
    except Exception as e:
        return jsonify({'error': f'Error in GPT-3 API: {str(e)}'})

    return jsonify({'result': summarized_text})

if __name__ == '__main__':
    app.run(debug=True)
