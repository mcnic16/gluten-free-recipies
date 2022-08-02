from food import db


class Dessert(db.Model):
    # schema for the Desserts Model
    id = db.Column(db.Integer, primary_key=True)
    dessert_name = db.Column(db.Text, unique=True, nullable=False)
    dessert_description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Dessert: {1} ".format(
        self.id, self.dessert_name, self.dessert_description
        )


class Recipe(db.Model):
    # schema for the Recipe Model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.Text, unique=True, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
         return "#{0} - Recipe: {1} ".format(
         self.id, self.recipe_name, self.recipe_description
        )
    