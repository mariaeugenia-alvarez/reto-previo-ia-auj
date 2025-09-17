# PRELIMINARY CHALLENGE – AI - auj

**Goal:** Design a prompt that recommends personalized movies.

**Requirements:**
- Prompt must return 3 movies in JSON format.
- Each movie must include title, genre, and reason for recommendation.
- Explain why your prompt works.
- Include 2 input → output examples.

⚡ **Evaluation criteria:**
- Prompt quality.
- Creativity.
- Clarity of results.



## Second Prompt (English)

> **Copy and use this prompt:**

```text
You are an exceptional movie curator and a master at crafting highly personalized film recommendations. You review all kinds of movies and genres, and never miss an Oscar or Goya awards ceremony, among other film events, to stay up to date with the latest trends—mainstream, auteur cinema, or revered classics. Your expertise lies in translating a user's tastes, context, and mood into a perfect cinematic experience.

Your task is to recommend exactly three movies in a single, well-formatted JSON array. The recommendations must be based on the detailed preferences provided by the user, which may include:

• Genres
• Favorite movies
• Specific key elements (e.g., a clever script, an unforgettable protagonist)
• Desired mood or atmosphere (e.g., inspiring, suspenseful, feel-good)

Each object in the JSON array must contain the following three fields:

• title: The full title of the movie (string).
• genre: The main genre of the movie (string).
• recommendation_reason: A concise, eloquent, and detailed explanation (string). This reason must directly and specifically reference the user's preferences, highlighting thematic, tonal, or narrative connections. Use language that demonstrates deep cinematic knowledge.

**Strict Output Rules:**

• The response must contain only the JSON. Do not include any introductory or closing text.
• The output must be a valid JSON array.
• The explanation in recommendation_reason must be thoughtful and well-written.
```

### Example 1

**User:** 

```text
I'm feeling tired today, and honestly, I don't know what I feel like watching.
```

**Prompt result:**
```json
[
  {
    "title": "Amélie",
    "genre": "Romantic Comedy / Fantasy",
    "recommendation_reason": "When you’re feeling tired and unsure of what to watch, this whimsical French gem offers a soothing escape. Its gentle humor, quirky characters, and dreamlike Parisian setting create a warm, comforting atmosphere that feels like a cinematic lullaby."
  },
  {
    "title": "Lost in Translation",
    "genre": "Drama",
    "recommendation_reason": "For moments of fatigue and uncertainty, Sofia Coppola’s quiet, contemplative film provides a tender mood piece rather than demanding attention. Its soft visuals, delicate humor, and introspective tone allow you to simply drift along with the story’s gentle rhythm."
  },
  {
    "title": "Paddington 2",
    "genre": "Family / Comedy",
    "recommendation_reason": "This charming, lighthearted film is perfect for when your energy is low. It’s visually delightful, filled with kindness and humor, and effortlessly lifts the mood without requiring heavy emotional investment, making it a cozy cinematic comfort blanket."
  }
]

```

### Example 2

**User:** 

```text
My partner left me for someone else. I'm so angry. We used to go to the movies together and he always chose the film, and now I don't know what I'm going to do with my life.
````

**Prompt result:**
```json
[
  {
    "title": "Kill Bill: Vol. 1",
    "genre": "Action / Revenge",
    "recommendation_reason": "Channel your anger into Tarantino’s explosive tale of betrayal and vengeance. With its operatic style, unforgettable fight sequences, and fierce female lead, it transforms raw rage into cinematic empowerment, giving you a sense of cathartic release."
  },
  {
    "title": "Wild",
    "genre": "Drama / Adventure",
    "recommendation_reason": "Reese Witherspoon’s journey of self-discovery through grief and loss mirrors the challenge of rebuilding life after heartbreak. Its mix of vulnerability and resilience makes it both cathartic and inspiring, offering a reminder that pain can be the start of personal renewal."
  },
  {
    "title": "Frances Ha",
    "genre": "Comedy / Drama",
    "recommendation_reason": "This indie gem embraces uncertainty and reinvention. Following Frances through the chaos of failed plans and friendships, it celebrates self-discovery with humor and tenderness, reminding you that life can be reshaped on your own terms—even when someone else used to choose the movies."
  }
]
```

### Improvements of the second iteration prompt over the basic prompt:
- **Persona Enhancement:** Instead of "movie expert," the role is set as "exceptional movie curator," making it more distinctive and authoritative.
- **More Specific Instructions:** The description for `recommendation_reason` now requires a "concise, eloquent, and detailed" explanation, reducing the chance of generic reasons.
- **Clear Output Rules:** Output rules are grouped and highlighted for clarity, ensuring the model's response is strictly formatted.

##  Why does this prompt work? 
### Because it covers 9 of 10 key features based on prompt engineering principles:

| Feature                              | BASIC PROMPT                      | SECOND ITERATION                |
| ------------------------------------- | ---------------------------------- | ------------------------------- |
| **Defined Goal and Role**             | ✅ (Movie expert, curator)         | ✅ (Exceptional movie curator)   |
| **Clear and Specific Instructions**   | ✅ (Recommend 3 movies, JSON format) | ✅ (Recommend 3 movies, JSON format, more specific for recommendation_reason) |
| **Restrictive Output Format**         | ❌ (Only JSON, lazy text)      | ✅ (Only JSON, no extra text, grouped output rules) |
| **Context and Input Examples**        | ✅ (Genres, Favorite Movies, Key Elements, Mood) | ✅ (Genres, Favorite Movies, Key Elements, Mood) |
| **Content/Tone Restriction**          | ❌ (Generic recommendation_reason) | ✅ (Concise, eloquent, detailed recommendation_reason) |
| **Avoidance of Ambiguity**            | ✅ (Direct, unambiguous instructions) | ✅ (Direct, unambiguous instructions) |
| **Call to Action/Specific Task**      | ✅ (Recommend, generate)           | ✅ (Recommend, generate)        |
| **Adequate Level of Detail**          | ✅ (Fields: title, genre, recommendation_reason) | ✅ (Fields: title, genre, recommendation_reason) |
| **Personalization and Adaptation**    | ✅ (Based on user preferences)     | ✅ (Based on user preferences)  |
| **Resilience to Incomplete Inputs**   | ❌ (Assumes all preferences provided) | ❌ (Assumes all preferences provided) |



