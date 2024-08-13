from django.db import models

SIZES = [
    ('tiny', 'Tiny'),
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
    ('gargantuan', 'Garagantuan')

]

ATTRIBUTE_CHOICES = [
    ('strength', 'Strength'),
    ('dexterity', 'Dexterity'),
    ('constitution', 'Constitution'),
    ('intelligence', 'Intelligence'),
    ('wisdom', 'Wisdom'),
    ('charisma', 'Charisma')
]

EFFECT_CHOICES = [
    ('strength', 'Strength'),
    ('dexterity', 'Dexterity'),
    ('constitution', 'Constitution'),
    ('intelligence', 'Intelligence'),
    ('wisdom', 'Wisdom'),
    ('charisma', 'Charisma'),
    ('attack', 'Attack'),
    ('cmd', 'CMD'),
    ('cmb', 'CMB'),
    ('size', 'Size'),
    ('spell_res', 'Spell Resistance'),
    ('damage_res', 'Damage Resistance'),
    ('ac', 'Armor Class'),
    ('move_speed', 'Movement Speed'),
    ('init_misc', 'Initiative')

]


class Attributes(models.Model):
    attr_name = models.CharField(max_length=50, null=True)
    attr_base = models.PositiveSmallIntegerField(default=10)
    attr_adj = models.SmallIntegerField(default=0)


class SavingThrows(models.Model):
    save_name = models.CharField(max_length=50, null=True)
    save_magic = models.SmallIntegerField(default=0)
    save_temp = models.SmallIntegerField(default=0)
    save_misc = models.SmallIntegerField(default=0)


class Skills(models.Model):
    skill_name = models.CharField(max_length=50, null=True)
    skill_ranks = models.PositiveSmallIntegerField(default=0)
    skill_mod = models.SmallIntegerField(default=0)


class CharacterClass(models.Model):
    class_name = models.CharField(max_length=100, null=True)
    class_bab = models.SmallIntegerField(default=0)
    class_will_mod = models.PositiveSmallIntegerField(default=0)
    class_fort_mod = models.PositiveSmallIntegerField(default=0)
    class_level = models.PositiveSmallIntegerField(default=1)


class DamageResistance(models.Model):
    dmg_res_name = models.CharField(max_length=50, null=True)
    dmg_res_type = models.CharField(max_length=20, null=True)
    dmg_res_value = models.PositiveSmallIntegerField(default=0)


class Effect(models.Model):
    """
    TODO: handle effects that need specification like skill affection: Which Skill?
    """
    affected_trait = models.CharField(choices=EFFECT_CHOICES, max_length=50, null=True)
    effect_value = models.SmallIntegerField(default=0)
    effect_condition = models.CharField(max_length=50, null=True)


class Traits(models.Model):
    trait_name = models.CharField(max_length=50, null=True)
    trait_description = models.TextField(default="")
    trait_effect = models.ManyToManyField(Effect)


class Weapons(models.Model):
    weapon_name = models.CharField(max_length=50, null=True)
    weapon_description = models.TextField(default="")
    weapon_attack_bonus = models.PositiveSmallIntegerField(default=0)
    weapon_crit_range = models.PositiveSmallIntegerField(default=20)
    weapon_crit_damage = models.PositiveSmallIntegerField(default=2)
    weapon_range = models.PositiveSmallIntegerField(default=5)
    weapon_ammunition = models.PositiveSmallIntegerField(null=True)
    weapon_damage_dice = models.CharField(max_length=50, null=True)


class Armors(models.Model):
    armor_name = models.CharField(max_length=50, null=True)
    armor_description = models.TextField(default="")
    armor_bonus = models.SmallIntegerField(default=0)
    armor_type = models.CharField(max_length=50, null=True)
    armor_check_penalty = models.SmallIntegerField(default=0)
    armor_spell_fail = models.SmallIntegerField(default=0)
    armor_weight = models.PositiveSmallIntegerField(default=0)
    armor_properties = models.CharField(max_length=500, null=True)


class Items(models.Model):
    item_name = models.CharField(max_length=50, null=True)
    item_description = models.TextField(default="")
    item_weight = models.PositiveSmallIntegerField(default=0)
    item_amount = models.PositiveSmallIntegerField(default=1)


class Feats(models.Model):
    feat_name = models.CharField(max_length=50, null=True)
    feat_description = models.TextField(default="")
    feat_source = models.CharField(max_length=50, null=True)
    feat_effect = models.ManyToManyField(Effect)


class SpecialAbilities(models.Model):
    ability_name = models.CharField(max_length=50, null=True)
    ability_description = models.TextField(default="")
    ability_source = models.CharField(max_length=50, null=True)
    ability_effect = models.ManyToManyField(Effect)


class Spells(models.Model):
    spell_name = models.CharField(max_length=50, null=True)
    spell_description = models.TextField(default="")
    spell_level = models.PositiveSmallIntegerField(null=True)
    spell_school = models.CharField(max_length=50, null=True)
    spell_components = models.CharField(max_length=100, null=True)
    spell_range = models.CharField(max_length=50, null=True)
    spell_target = models.CharField(max_length=100, null=True)
    spell_duration = models.CharField(max_length=50, null=True)
    spell_saving_throw = models.CharField(max_length=50, null=True)
    spell_resistance = models.CharField(max_length=50, null=True)


class SpellCasting(models.Model):
    casting_level = models.PositiveSmallIntegerField(null=True)
    spell_save_dc = models.PositiveSmallIntegerField(null=True)
    spells_known = models.PositiveSmallIntegerField(null=True)
    spells_per_day = models.PositiveSmallIntegerField(null=True)
    bonus_spells = models.PositiveSmallIntegerField(null=True)


class Character(models.Model):
    # general semi constants
    name = models.CharField(max_length=100, null=True)
    player = models.CharField(max_length=100, default="Player")
    race = models.CharField(max_length=50, null=True)
    alignment = models.CharField(max_length=20, null=True)
    deity = models.CharField(max_length=100, null=True)
    homeland = models.CharField(max_length=100, null=True)
    weight = models.FloatField(null=True)
    hair = models.CharField(max_length=100, null=True)
    eyes = models.CharField(max_length=100, null=True)

    size = models.CharField(max_length=20, default="medium")
    age = models.PositiveSmallIntegerField(null=True)

    char_classes = models.ManyToManyField(CharacterClass)
    char_attributes = models.ManyToManyField(Attributes)
    char_skills = models.ManyToManyField(Skills)

    char_saving_throws = models.ManyToManyField(SavingThrows)
    char_save_mod_general = models.SmallIntegerField(default=0)

    # resistances
    spell_resistance = models.SmallIntegerField(default=0)
    dmg_resistance = models.ManyToManyField(DamageResistance)
    dmg_res_general = models.PositiveSmallIntegerField(default=0)

    # hp
    total_hit_points = models.PositiveSmallIntegerField(null=True)
    current_hit_points = models.SmallIntegerField(null=True)
    temporary_hit_points = models.SmallIntegerField(default=0)
    non_lethal_dmg = models.PositiveSmallIntegerField(null=True)

    # armor
    base_armor = models.PositiveSmallIntegerField(default=10)
    size_armor = models.SmallIntegerField(default=0)
    natural_armor = models.SmallIntegerField(default=0)
    deflection_armor = models.SmallIntegerField(default=0)

    # initiative
    initiative_misc = models.SmallIntegerField(default=0)

    # attack actions
    cmb_modifier = models.SmallIntegerField(null=True)
    cmd_modifier = models.SmallIntegerField(null=True)
    bab_general_modifiers = models.SmallIntegerField(default=0)

    # equipment
    weapon = models.ManyToManyField(Weapons)
    armor = models.ManyToManyField(Armors)
    inventory = models.ManyToManyField(Items)

    # powers
    traits = models.ManyToManyField(Traits)
    special_abilities = models.ManyToManyField(SpecialAbilities)
    feats = models.ManyToManyField(Feats)
    spells = models.ManyToManyField(Spells)

    spell_casting = models.ManyToManyField(SpellCasting)

    # currency
    copper = models.PositiveSmallIntegerField(default=0)
    silver = models.PositiveSmallIntegerField(default=0)
    gold = models.PositiveSmallIntegerField(default=0)
    platinum = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
