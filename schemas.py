# schemas.py - Public Interface Definitions
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, Dict, List
from enum import Enum

class ConversationMode(str, Enum):
    SPEAK_FOR_ME = "speak_for_me"
    TRANSLATE = "translate"
    EXPLAIN = "explain"

class VoiceRequest(BaseModel):
    """
    Schéma d'entrée pour l'endpoint multimodal.
    Démontre la gestion des entrées hybrides (texte/audio).
    """
    text_input: Optional[str] = Field(None, example="How much does this cost?")
    audio_base64: Optional[str] = Field(None, description="Audio raw data in base64 format")
    mode: ConversationMode = Field(..., example=ConversationMode.TRANSLATE)
    source_language: str = Field("en", pattern="^(en|ar|darija)$")

class VoiceResponse(BaseModel):
    """
    Schéma de sortie structuré.
    Démontre une conception orientée vers l'expérience utilisateur (UX).
    """
    detected_language: str
    transcription: str
    translation: str
    phonetic_transcription: Optional[str] = None
    audio_url: Optional[HttpUrl] = None
    confidence_score: float = Field(..., ge=0, le=1)
    
    # Métadonnées pour le suivi de la performance (Latency Tracking)
    metadata: Dict[str, float] = Field(
        default_factory=dict, 
        description="Timing breakdown for STT, LLM, and TTS steps"
    )

class ApiError(BaseModel):
    error_code: str
    message: str
