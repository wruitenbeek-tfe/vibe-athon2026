from pydantic import BaseModel, Field


class Vacancy(BaseModel):
    job_title: str = Field(alias="jobTitle")
    job_description: str = Field(alias="jobDescription")
    location: str
    employment_type: str = Field(alias="employmentType")
    experience_level: str = Field(alias="experienceLevel")
    required_skills: list[str] = Field(alias="requiredSkills")
    must_have_skills: list[str] = Field(default_factory=list, alias="mustHaveSkills")
    nice_to_have_skills: list[str] = Field(default_factory=list, alias="niceToHaveSkills")
    education_level: str = Field(alias="educationLevel")
    languages_required: list[str] = Field(alias="languagesRequired")
    remote_policy: str | None = Field(default=None, alias="remotePolicy")
    salary_min: int | None = Field(default=None, alias="salaryMin")
    salary_max: int | None = Field(default=None, alias="salaryMax")
    industry: str | None = None
    company_stage: str | None = Field(default=None, alias="companyStage")
    visa_sponsorship: bool | None = Field(default=None, alias="visaSponsorship")
    language_level: str | None = Field(default=None, alias="languageLevel")
    posted_at: str | None = Field(default=None, alias="postedAt")

    model_config = {"populate_by_name": True}


class VacancyMatch(BaseModel):
    vacancy: Vacancy
    score: int
    reasons: list[str]
