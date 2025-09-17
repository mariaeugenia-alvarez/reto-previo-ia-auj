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


## Basic Prompt (English)

You are a movie expert and a curator of personalized recommendations.
Your task is to recommend 3 movies in JSON format based on the detailed preferences I provide, like:
1. Genres
2. Favorite Movies
3. Key Elements
4. Mood

Based on the user's responses, generate an answer in **JSON format** containing an array of 3 objects, each representing a movie. Each object must have the following fields: 
`title` (string), `genre` (string), and `recommendation_reason` (string). 

The `recommendation_reason` should convincingly explain why the movie is a good choice for the user, directly connecting it to their previous answers. Do not include anything else in the response, only the JSON.


### Example 1

**User:** I like the science fiction genre, for example movies like Inception. My favorite actor is Keanu Reeves. Also, today I feel very energetic and active.

**Prompt result:**
```json
[
	{
		"title": "The Matrix",
		"genre": "Science Fiction, Action",
		"recommendation_reason": "Starring Keanu Reeves, 'The Matrix' offers a high-energy, action-packed experience with a complex science fiction plot, perfectly matching your love for the genre and your energetic mood."
	},
	{
		"title": "Edge of Tomorrow",
		"genre": "Science Fiction, Action",
		"recommendation_reason": "This movie combines intense action with a clever science fiction premise, ideal for someone who enjoys movies like 'Inception' and is feeling active."
	},
	{
		"title": "John Wick",
		"genre": "Action, Thriller",
		"recommendation_reason": "Keanu Reeves stars in this fast-paced thriller, which will keep you engaged and matches your energetic mood, even though it's not strictly science fiction."
	}
]
```


### Example 2

**User:** Today I’m feeling a bit nerdy. I like comedy, especially romantic ones. I don’t have a favorite actor as long as they make me laugh and the movie is about love.

**Prompt result:**
```json
[
  {
    "title": "The Big Sick",
    "genre": "Romantic Comedy",
    "recommendation_reason": "'The Big Sick' is a witty romantic comedy that blends nerdy humor with a heartfelt love story, perfect for your mood and taste."
  },
  {
    "title": "Crazy Rich Asians",
    "genre": "Romantic Comedy",
    "recommendation_reason": "This film is full of laughs and romance, with a charming cast and plenty of comedic moments centered around love, ideal for someone who enjoys romantic comedies."
  },
  {
    "title": "Notting Hill",
    "genre": "Romantic Comedy",
    "recommendation_reason": "A classic romantic comedy that will make you laugh and warm your heart, even if you don’t have a favorite actor, as the chemistry and humor are the highlights."
  }
]
```

##  Why does this prompt work? 
### Because it covers 9 of 10 key features based on prompt engineering principles:

| Feature                              | BASIC PROMPT |
| ------------------------------------- | ------------ |
| **Defined Goal and Role**             | ✅ (Movie expert, curator) |
| **Clear and Specific Instructions**   | ✅ (Recommend 3 movies, JSON format) |
| **Restrictive Output Format**         | ✅ (Only JSON, no extra text) |
| **Context and Input Examples**        | ✅ (Genres, Favorite Movies, Key Elements, Mood) |
| **Content/Tone Restriction**          | ✅ (Convincing recommendation_reason) |
| **Avoidance of Ambiguity**            | ✅ (Direct, unambiguous instructions) |
| **Call to Action/Specific Task**      | ✅ (Recommend, generate) |
| **Adequate Level of Detail**          | ✅ (Fields: title, genre, recommendation_reason) |
| **Personalization and Adaptation**    | ✅ (Based on user preferences) |
| **Resilience to Incomplete Inputs**   | ❌ (Assumes all preferences provided) |



