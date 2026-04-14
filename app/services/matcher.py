from app.schemas.matching import CandidateProfile, MatchResponse


class VacancyMatcherService:
    def match(self, profile: CandidateProfile) -> MatchResponse:
        return MatchResponse(
            mode=profile.mode,
            reply=(
                "Starter intake completed. No vacancy ranking is implemented yet. "
                "Build your own extraction and matching logic in "
                "`app/services/matcher.py`."
            ),
            profile_preview=self._profile_preview(profile.text),
            matches=[],
        )

    @staticmethod
    def _profile_preview(profile_text: str) -> str:
        compact = " ".join(profile_text.split())
        return compact[:160] + ("..." if len(compact) > 160 else "")
