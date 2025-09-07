# 🚀 AI-Based Internship Recommendation Engine for PM Internship Scheme

### 📌 Smart India Hackathon (SIH) 2025

**Team NOVAS**
👨‍💻 **Members:**

* Asif Qamar
* Fatima Aslam
* Aryan Jha
* Souvik Majee
* Avik Ghosh
* Prerna Priya

---

## 📖 Problem Statement

**ID:** 25034
**Title:** *AI-Based Internship Recommendation Engine for PM Internship Scheme*

The **PM Internship Scheme** receives thousands of applications from youth across India, including rural areas, tribal districts, urban slums, and remote colleges. Many candidates are first-generation learners with limited digital exposure and no prior internship experience.

With hundreds of internships listed on the portal, it becomes challenging for such candidates to identify opportunities that match their **skills, interests, or aspirations**. This leads to misaligned applications and missed opportunities.

---

## 🎯 Objective

To build a **simple, lightweight AI-based recommendation engine** that suggests the **top 3–5 most relevant internships** to each candidate based on their **profile, education, skills, interests, and location preferences**.

The solution must be:

* ✅ User-friendly & mobile-first
* ✅ Accessible even for users with low digital literacy
* ✅ Lightweight and easy to integrate with the **existing PM Internship Portal**
* ✅ Multi-language adaptable (support for regional languages)

---

## ⚙️ Proposed Solution

A **functional prototype** with the following features:

* 📥 **Input Capture:** Candidate’s basic details (Education, Skills, Sector Preferences, Location).
* 🤖 **Recommendation Engine:** A lightweight ML/Rule-based model that suggests **3–5 top internships**.
* 📱 **User-Friendly UI:** Minimal text, intuitive icons, card/swipe-based design.
* 🌍 **Mobile Access:** Built with **React & React Native** for accessibility on web and mobile.
* 🔗 **Integration Ready:** Exposed as **REST API**, so it can easily be plugged into the **PM Internship Portal**.

---

## 🛠️ Tech Stack

### 🔹 Frontend (UI/UX)

* **React.js** → Web interface
* **React Native** → Mobile app interface
* **Card-based UI** (Swipe-style interaction, similar to shorts) for internship suggestions

### 🔹 Backend (API & Logic)

* **FastAPI / Flask / Node.js** → REST API to connect frontend with ML model
* Lightweight, scalable backend for integration with **PM Internship Portal**

### 🔹 Machine Learning / Recommendation Engine

* **Rule-based Scoring System (Phase 1):**

  * +10 → for each matching skill
  * +5 → for matching sector of interest
  * +5 → for location preference match
  * Rank internships → Show Top 3–5

* **Collaborative Filtering (Phase 2 - Enhancement):**

  * Uses user application history & successful placements to refine recommendations
  * Hybrid approach (Rule-based + Collaborative Filtering)

### 🔹 Data

* **Internship Data** → Collected via scraping/dummy dataset (CSV/JSON)
* **Candidate Data** → Captured from form input

---

## 🔄 Workflow (High-Level Flowchart)

1. **User Input** → Education, Skills, Interests, Location
2. **Internship Database** → Title, Skills Required, Sector, Location, Stipend
3. **Preprocessing** → Clean and structure candidate & internship data
4. **Scoring System** → Rule-based matching with weighted scores
5. **Recommendation Engine** → Rank & return Top 3–5 internships
6. **Frontend Display** → Mobile-first UI with swipeable internship cards

---

## 📌 Features

* 📝 Resume upload + preference form (location, remote/on-site, skills, etc.)
* 🔍 Gap Analysis → Show missing skills vs. required skills
* 📊 Score-based ranking (0–1 similarity or out of 10)
* 🌐 Multi-language support with icons & minimal text for accessibility
* 📱 Mobile-first design → Suitable for low digital literacy candidates

---

## 🚧 Challenges & How We Overcame

| Challenge                              | Solution                                                      |
| -------------------------------------- | ------------------------------------------------------------- |
| Limited digital literacy of candidates | Designed **icon-driven UI** with minimal text                 |
| Low-resource deployment requirement    | Used **rule-based lightweight ML** instead of heavy models    |
| Lack of direct API for internships     | Created structured dataset (CSV/JSON) via scraping/dummy data |
| Diverse backgrounds of candidates      | Included **broad sector options + "Other"** for flexibility   |
| Integration with existing portal       | Built **REST API** for seamless integration                   |

---

## 🌍 Impact & Benefits

* 🎯 **Personalized guidance** → Ensures candidates don’t get overwhelmed by hundreds of listings
* 📈 **Higher success rate** → Better alignment between candidate skills & internships
* 🏫 **Inclusive system** → Rural, tribal, and first-gen learners can access equal opportunities
* 💡 **Scalable model** → Can evolve with data into advanced recommendation system
* 🤝 **Government integration** → Strengthens PM Internship Scheme by improving placement efficiency

---

## 📷 Prototype Preview

*(Insert UI mockups, flowchart, or prototype screenshots here)*

---

## 📚 References

1. Corné de Ruijt, Sandjai Bhulai (2021) - [Job Recommender Systems: A Review](https://arxiv.org/abs/2111.13576)
2. ITM Conferences (2022) - [Job Recommendation Approaches](https://www.itm-conferences.org/articles/itmconf/abs/2022/04/itmconf_icacc2022_02002/itmconf_icacc2022_02002.htm)
3. G. Deepak - [Applying Data Mining Techniques in Job Recommender System](https://gdeepak.com/pubs/Applying_Data_Mining_Anika.pdf)



