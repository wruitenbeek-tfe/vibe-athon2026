from app.schemas.matching import (
    CandidateProfile,
    ChatIntakeRequest,
    CVUploadRequest,
    MatchMode,
)


class IntakeService:
    def from_cv_upload(self, payload: CVUploadRequest) -> CandidateProfile:
        chunks = [
            f"source: cv file {payload.filename.strip()}",
            payload.content.strip(),
            payload.notes.strip(),
        ]
        return CandidateProfile(mode=MatchMode.cv_upload, text=self._join_chunks(chunks))

    def from_chat_intake(self, payload: ChatIntakeRequest) -> CandidateProfile:
        chunks: list[str] = [payload.summary.strip()]
        for item in payload.answers:
            chunks.append(f"{item.question.strip()}: {item.answer.strip()}")
        return CandidateProfile(mode=MatchMode.chat_intake, text=self._join_chunks(chunks))

    @staticmethod
    def _join_chunks(chunks: list[str]) -> str:
        return "\n".join(chunk for chunk in chunks if chunk).strip()
