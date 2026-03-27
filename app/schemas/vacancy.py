from pydantic import BaseModel, Field


class Vacancy(BaseModel):
    job_title: str = Field(alias="jobTitle")
    job_description: str = Field(alias="jobDescription")
    location: str
    employment_type: str = Field(alias="employmentType")
    experience_level: str = Field(alias="experienceLevel")
    required_skills: list[str] = Field(alias="requiredSkills")
    education_level: str = Field(alias="educationLevel")
    languages_required: list[str] = Field(alias="languagesRequired")

    model_config = {"populate_by_name": True}


class VacancyMatch(BaseModel):
    vacancy: Vacancy
    score: int
    reasons: list[str]
