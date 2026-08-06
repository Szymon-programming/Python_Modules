from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
	allowed = dark_spell_allowed_ingredients()
	ing_list = [ing.strip().lower() for ing in ingredients.split(",")]
	is_valid = any(ing in allowed for ing in ing_list)
	if is_valid:
		status = "VALID"
	else:
		status = "INVALID"
	return f"{ingredients} ({status})"