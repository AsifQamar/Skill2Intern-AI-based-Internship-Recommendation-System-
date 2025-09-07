# AI-Based Internship Recommendation Engine for PM Internship Scheme

### Smart India Hackathon (SIH) 2025

**Team NOVAS**
**Members:**

* Asif Qamar
* Fatima Aslam
* Aryan Jha
* Souvik Majee
* Avik Ghosh
* Prerna Priya

---

## Problem Statement

**ID:** 25034
**Title:** *AI-Based Internship Recommendation Engine for PM Internship Scheme*

The PM Internship Scheme receives thousands of applications from youth across India, including those from rural areas, tribal districts, urban slums, and remote colleges. Many applicants are first-generation learners with limited digital exposure and no prior internship experience.

With hundreds of internships listed on the portal, it becomes difficult for such candidates to identify the opportunities that best match their skills, interests, and aspirations. This mismatch leads to misaligned applications, lower chances of success, and missed opportunities.

---

## Objective

The objective is to design and implement a **lightweight AI-based recommendation engine** that provides **3–5 personalized internship suggestions** to each candidate. Recommendations will be based on the candidate’s profile, including education, skills, interests, and location preferences.

The solution should be:

* User-friendly and accessible across devices.
* Designed for candidates with low digital literacy.
* Lightweight and easily integrable with the **PM Internship Scheme portal**.
* Adaptable to multiple Indian regional languages.

---

## Proposed Solution

The proposed system will provide a **functional prototype** with the following capabilities:

* **Input Capture**: Collect candidate information (education, skills, sector preferences, location).
* **Recommendation Engine**: Rule-based scoring with scope for lightweight machine learning, outputting the top 3–5 internships.
* **User Interface**: A simple, card-based interface that is intuitive and accessible on both web and mobile platforms.
* **Integration**: REST API that can be embedded within the PM Internship portal.

---

## System Architecture

### Frontend (UI/UX)

* Technology: **React.js** (Web), **React Native** (Mobile).
* Features:

  * Card-based design with swipe functionality for recommendations.
  * Icon-driven layout for candidates with low digital literacy.
  * Mobile-first design for maximum accessibility.

### Backend (API & Logic)

* Technology: **FastAPI / Flask / Node.js**.
* Features:

  * REST API providing internship recommendations in JSON format.
  * Integration-ready with the PM Internship Scheme portal.
  * Lightweight deployment to ensure low resource consumption.

### Recommendation Engine

**Phase 1 – Rule-Based Scoring System**

* +10 points for each matching skill.
* +5 points for matching sector of interest.
* +5 points for matching location preference.
* Internships are ranked and the top 3–5 are returned.

**Phase 2 – Enhancement with Collaborative Filtering**

* Utilizes historical user data and successful applications.
* Hybrid approach: Rule-based scores boosted with collaborative filtering insights.
* Example: “Candidates with your skills who applied to Internship A also successfully applied to Internship B.”

### Data Sources

* Internship Data: Scraped or simulated datasets (CSV/JSON) containing internship details (title, skills required, sector, location, stipend).
* Candidate Data: Form-based user input (education, skills, interests, location).

---

## Workflow

1. Candidate submits profile: education, skills, interests, and location.
2. Internship database is accessed, containing structured information on internships.
3. Data preprocessing ensures consistent format for candidate and internship data.
4. Rule-based scoring system evaluates candidate-to-internship matches.
5. Recommendation engine ranks internships and returns the top 3–5 results.
6. Frontend displays results in a mobile-first, card-based UI.

---

## Key Features

* Resume upload combined with preference form (location, remote/on-site, skills).
* Gap analysis showing missing skills compared to required internship skills.
* Score-based ranking for clarity in recommendations.
* Multi-language support for wider accessibility.
* Low complexity model ensuring lightweight deployment.

---

## Challenges and Solutions

| Challenge                                   | Solution                                                            |
| ------------------------------------------- | ------------------------------------------------------------------- |
| Limited digital literacy of candidates      | Icon-driven, minimal-text UI design.                                |
| Requirement for lightweight deployment      | Rule-based scoring system instead of resource-heavy models.         |
| Absence of direct internship APIs           | Created structured datasets (CSV/JSON) through scraping/simulation. |
| Diversity in candidate profiles             | Broad sector categories with an “Other” option for flexibility.     |
| Seamless integration with government portal | REST API for smooth interoperability.                               |

---

## Impact and Benefits

* Provides **personalized internship recommendations** to improve application quality.
* Reduces confusion and information overload among candidates.
* Enhances the success rate of internship placements.
* Bridges the opportunity gap for candidates from rural, tribal, and underserved regions.
* Scales with time, enabling integration of more advanced machine learning models.
* Strengthens the PM Internship Scheme’s efficiency and outreach.

---

## Prototype & Prototype Preview
<img width="500" height="500" alt="Frontend Sample" src="https://github.com/user-attachments/assets/8a4fc330-67e6-42d5-9772-8fd7b0d02e3d" />


<img width="500" height="500" alt="Untitled diagram _ Mermaid Chart-2025-09-07-085154" src="https://github.com/user-attachments/assets/0083c646-1f01-41d5-8ceb-18d9ddedad94" />



---

## References

1. Corné de Ruijt, Sandjai Bhulai (2021) - [Job Recommender Systems: A Review](https://arxiv.org/abs/2111.13576)
2. ITM Conferences (2022) - [Job Recommendation Approaches](https://www.itm-conferences.org/articles/itmconf/abs/2022/04/itmconf_icacc2022_02002/itmconf_icacc2022_02002.htm)
3. G. Deepak - [Applying Data Mining Techniques in Job Recommender System](https://gdeepak.com/pubs/Applying_Data_Mining_Anika.pdf)

---
