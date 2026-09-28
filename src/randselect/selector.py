import random

def random_selection(n_list, q_list, rng=random, exclude_names=(), exclude_questions=()):

  name_candidates = [n for n in n_list if n not in exclude_names]
  question_candidates = [q for q in q_list if q not in exclude_questions]

  chosen_name = rng.choice(name_candidates)
  chosen_question = rng.choice(question_candidates)

  return (chosen_name, chosen_question)