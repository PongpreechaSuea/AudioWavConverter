import ffmpeg
from typing import Optional

def convert_to_wav(input_file: str, output_file: str, sample_rate: int = 44100) -> Optional[str]:
    """
        Convert an audio file to WAV format using ffmpeg.

        This function converts the input audio file to WAV format with specified parameters.
        It uses ffmpeg for the conversion process and handles potential errors.

        Input:
            input_file (str): Path to the input audio file.
            output_file (str): Path where the output WAV file will be saved.
            sample_rate (int, optional): The desired sample rate for the output WAV file. Default is 44100 Hz.

        Output:
            Optional[str]: The path to the output WAV file if conversion is successful, None otherwise.

        Raises:
            ffmpeg.Error: If there's an error during the conversion process.

        Example usage:
            converted_file = convert_to_wav("input.mp3", "output.wav", sample_rate=48000)
    """
    try:
        stream = ffmpeg.input(input_file)
        stream = ffmpeg.output(stream, output_file, 
                               acodec='pcm_s16le',  # Linear PCM 16-bit little-endian
                               ac=2,                # 2 audio channels (stereo)
                               ar=str(sample_rate)) # Sample rate
        ffmpeg.run(stream, overwrite_output=True)
        return output_file
    except ffmpeg.Error as e:
        raise
    except Exception as e:
        return None