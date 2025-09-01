# TTS Finetuning

This project finetunes the **VITS-based Bangla TTS model** (`bangla-speech-processing/bangla_tts_female`)  
to generate authentic **Bangladeshi-accent Bengali speech**.  
It integrates open datasets (OpenSLR 53, Mozilla Common Voice, Bengali.AI) with preprocessing pipelines  
for accent-specific filtering, normalization, and phonemization.  
A **custom loss function** is introduced, combining mel-spectrogram loss, phoneme accuracy,  
and accent-discriminator loss to enforce Bangladeshi pronunciation.  
Training leverages Hugging Face Transformers, PyTorch, and WandB for monitoring.  
The repository includes dataset preparation, model adaptation, training, and a Gradio demo for inference.  

---
