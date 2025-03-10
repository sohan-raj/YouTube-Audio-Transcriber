import yt_dlp
from pathlib import Path
import whisper
import torch

def download_audio_fast(url, output_template=None):
    clean_url = url.split('?')[0]  # Remove tracking parameters
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',  
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                #'del_old': True,  # Delete original file after conversion
            }
        ],
        'outtmpl': output_template,    #audio-output/'%(title)s.%(ext)s',   Keeping original extension
        'prefer_ffmpeg': True,  # Using FFmpeg for handling formats
        'noplaylist': True,  
        'nocheckcertificate': True,  #bypassing ssl pass
        'cookiefile': 'cookies.txt',  # Load cookies from file
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([clean_url])
        # Extract the final file path from metadata
        if result == 0:  # Success
            info = ydl.extract_info(clean_url, download=False)
            file_path = ydl.prepare_filename(info)
            base, _ = file_path.rsplit('.', 1)
            return f"{base}.mp3"  # Return path to converted MP3
        else:
            raise Exception("Download failed")
     
    except Exception as e:
        print(f"Error: {str(e)}")



def audio_directory():
    output_dir = Path('audio-output')
    output_dir.mkdir(exist_ok=True)  # Creating the directory if it doesn't exist
    output_template = str(output_dir / '%(title)s.%(ext)s')
    return output_template


def get_model(model_size: str):
    model_path = Path(f'model/{model_size}/model.pt')
    # Initialize model
    model = whisper.load_model(model_size)
    #choosing device
    device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')
    
    if model_path.exists():
        try:
            # Load model
            model.load_state_dict(torch.load(model_path, map_location=device,weights_only=True))
            #Change device to current model
            model.to(device)
            return model
            
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            return None
    else:
        #saving model locally
        try:
            model_path.parent.mkdir(parents=True, exist_ok=True)
            torch.save(model.state_dict(), model_path)
            return model
        except Exception as e:
            print(f"Error saving model: {str(e)}")


def transcribe_audio(audio_path):
    model = get_model('base')
    if model:
        try:
            # Test FFmpeg availability
            import librosa
            y, sr = librosa.load(audio_path, sr=None)  # Test audio loading
            print("Audio loaded successfully with librosa")
            
            # Proceed with transcription
            result = model.transcribe(audio_path)
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return 'Error loading model'

if __name__ == "__main__":
    video_url = input("Enter a Youtube video link:") #'https://youtu.be/kzDnA_EVhTU?si=nydklEZo9lXOTiuJ'
    audio_path = download_audio_fast(video_url, audio_directory())
    
    if audio_path and Path(audio_path).exists():  # <-- ADD CHECK
        result = transcribe_audio(str(audio_path))
        output_path = Path(audio_path).with_suffix('.txt')
        output_path.write_text(result['text'])
        print(f"Transcription saved to {output_path}")
        
    else:
        print("Download failed or file not found")
