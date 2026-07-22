from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/transcript", methods=["GET"])
def get_transcript():
    video_id = request.args.get("videoId")
    if not video_id:
        return jsonify({"error": "Missing videoId parameter"}), 400

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([item["text"] for item in transcript_list])
        return jsonify({"videoId": video_id, "transcript": full_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Transcript service is running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
