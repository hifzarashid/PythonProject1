import speech_recognition as sr
import sounddevice as sd
import scipy.io.wavfile as wav
import tkinter as tk
from tkinter import messagebox
from google import genai

AI_CLIENT = genai.Client(api_key="AQ.Ab8RN6KC_cJi1KHaQn2aK_G-Em7JfD_K6lNHYh1_81wzD34ECw")

def ask_ai(question_text):
    try:
        response = AI_CLIENT.models.generate_content(
            model='gemini-1.5-flash',
            contents=question_text,
        )
        return response.text
    except Exception as e:
        return f"AI Error: Jawab nahi mil saka. {str(e)}"
def start_listening():
    fs = 44100
    seconds = 5

    status_label.config(text="Listening... Ask your question! ", fg="#E63946")
    root.update()

    try:
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()

        status_label.config(text="Thinking... ", fg="#457B9D")
        root.update()

        wav.write('temp_audio.wav', fs, myrecording)

        recognizer = sr.Recognizer()
        with sr.AudioFile('temp_audio.wav') as source:
            audio = recognizer.record(source)

        user_question = recognizer.recognize_google(audio)

        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, f" You asked: {user_question}\n\n")
        root.update()
        ai_response = ask_ai(user_question)
        text_box.insert(tk.END, f"AI Answer:\n{ai_response}")
        status_label.config(text="Done! Response received.", fg="#2A9D8F")

    except sr.UnknownValueError:
        status_label.config(text="Error: Could not understand audio.", fg="#E63946")
        messagebox.showwarning("Oops!", "Mujhe aapki awaz samajh nahi aayi, please dubara boliye.")
    except Exception as e:
        status_label.config(text="Something went wrong.", fg="#E63946")
        messagebox.showerror("Error", f"Kuch masla hua hai: {str(e)}")


def copy_to_clipboard():
    text_to_copy = text_box.get("1.0", tk.END).strip()
    if text_to_copy:
        root.clipboard_clear()
        root.clipboard_append(text_to_copy)
        messagebox.showinfo("Success", "Text copy ho gaya hai! ")
    else:
        messagebox.showwarning("Empty", "Copy karne ke liye koi text nahi hai!")


def show_about_info():
    about_text = (
        " Voice AI Chatbot v2.0\n\n"
        "About this App:\n"
        "This is a voice-activated AI Assistant. Speak any question, "
        "and it will use advanced Google AI to give you real-time answers!\n\n"
        "Developed by: Hifza "
    )
    messagebox.showinfo("About This Application", about_text)
root = tk.Tk()
root.title("My Voice AI Chatbot")
root.geometry("500x500")
root.configure(bg="#F1FAEE")

title_label = tk.Label(root, text="Voice AI Chatbot", font=("Helvetica", 16, "bold"), bg="#F1FAEE", fg="#1D3557")
title_label.pack(pady=15)

mic_button = tk.Button(root, text=" Ask AI Anything", font=("Helvetica", 12, "bold"), bg="#457B9D", fg="white",
                       activebackground="#1D3557", activeforeground="white", padx=10, pady=5, command=start_listening)
mic_button.pack(pady=10)

status_label = tk.Label(root, text="Click the button above and ask a question", font=("Helvetica", 10, "italic"),
                        bg="#F1FAEE", fg="#6C757D")
status_label.pack(pady=5)

text_box = tk.Text(root, font=("Helvetica", 11), width=52, height=10, wrap=tk.WORD, bd=2, relief=tk.GROOVE)
text_box.pack(pady=15)

copy_button = tk.Button(root, text="Copy Full Chat", font=("Helvetica", 11, "bold"), bg="#2A9D8F", fg="white",
                        activebackground="#264653", activeforeground="white", padx=15, pady=5,
                        command=copy_to_clipboard)
copy_button.pack(pady=5)

about_button = tk.Button(root, text="ℹ About App", font=("Helvetica", 9, "bold"), bg="#E63946", fg="white",
                         activebackground="#1D3557", activeforeground="white", padx=10, command=show_about_info)
about_button.pack(pady=10)

root.mainloop()
