# Bangladeshi Bengali TTS Finetuning

This project finetunes the **VITS-based Bangla TTS model**  
(`bangla-speech-processing/bangla_tts_female`)  
to generate authentic **Bangladeshi-accent Bengali speech**.

It integrates open datasets:  
- OpenSLR 53  
- Mozilla Common Voice  
- Bengali.AI  

Preprocessing includes **accent-specific filtering, normalization, and phonemization**.

A **custom loss function** is used, combining:  
- Mel-spectrogram loss  
- Phoneme accuracy  
- Accent-discriminator loss  

Training uses **Hugging Face Transformers, PyTorch, and WandB** for monitoring.

The repository provides:  
- Dataset preparation scripts  
- Model adaptation & training pipeline  
- Gradio demo for inference
