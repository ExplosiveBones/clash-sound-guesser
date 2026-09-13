import os
import random
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sound_library = {
    "Archer Queen": {
        "filenames": [
            "Cards_Archer Queen_aq_dep_sfx_02.ogg",
            "Cards_Archer Queen_aq_fire_01.ogg",
            "Cards_Archer Queen_archer_queen_die_01.ogg",
            "Cards_Archer Queen_archer_queen_invis_01.ogg",
        ],
        "accepted_guesses": ["archer queen", "aq"],
    },
    "Archers": {
        "filenames": [
            "Cards_Archers_clash_archer_deploy_01.ogg",
            "Cards_Archers_evo_archer_crit_fire_01.ogg",
            "Cards_Archers_evo_archer_deploy_01.ogg",
        ],
        "accepted_guesses": ["archers", "evo archers"],
    },
    "Arrows": {
        "filenames": ["Cards_Arrows_archer_queen_attack_02.ogg"],
        "accepted_guesses": ["arrows", "arrow"],
    },
    "Baby Dragon": {
        "filenames": [
            "Cards_Baby Dragon_baby_dragon_deploy_end_11.ogg",
            "Cards_Baby Dragon_card_evolution_baby_dragon_deploy_vo_01.ogg",
            "Cards_Baby Dragon_card_evolution_baby_dragon_skill_loop.ogg",
            "Cards_Baby Dragon_tinymite_attack_04.ogg",
        ],
        "accepted_guesses": [
            "baby dragon",
            "baby dragon evolution",
            "evo baby dragon",
            "bd",
        ],
    },
    "Balloon": {
        "filenames": [
            "Cards_Balloon_deploy_balloon_06.ogg",
            "Cards_Balloon_card_hero_balloon_atk_cast.ogg",
            "Cards_Balloon_card_hero_balloon_death_bomb_burning.ogg",
            "Cards_Balloon_card_hero_balloon_death_bomb_explosion.ogg",
            "Cards_Balloon_card_hero_balloon_deploy.ogg",
            "Cards_Balloon_card_hero_balloon_skill_atk_cast.ogg",
            "Cards_Balloon_card_hero_balloon_skill_skeleton_fly.ogg",
        ],
        "accepted_guesses": ["balloon", "loon", "hero balloon"],
    },
    "Bandit": {
        "filenames": [
            "Cards_Bandit_bandit_atk_vo_01.ogg",
            "Cards_Bandit_bandit_dash_03.ogg",
            "Cards_Bandit_bandit_deploy_01.ogg",
            "Cards_Bandit_bandit_sneaky_laugh_05.ogg",
        ],
        "accepted_guesses": ["bandit"],
    },
    "Barbarian Barrel": {
        "filenames": [
            "Cards_Barbarian Barrel_barbarrel_01.ogg",
            "Cards_Barbarian Barrel_card_hero_barbarian_barrel_ability_activated.ogg",
            "Cards_Barbarian Barrel_card_hero_barbarian_barrel_deploy.ogg",
        ],
        "accepted_guesses": [
            "barbarian barrel",
            "barb barrel",
            "barbbarrel",
            "hero barb barrel",
            "hero barbarian barrel",
            "hero barbbarrel",
        ],
    },
    "Barbarians": {
        "filenames": [
            "Cards_Barbarians_barbarian_attack_02.ogg",
            "Cards_Barbarians_barbarian_attack_03.ogg",
            "Cards_Barbarians_barbarian_attack_04.ogg",
            "Cards_Barbarians_barbarian_attack_06.ogg",
            "Cards_Barbarians_deploy_barbarians_01.ogg",
            "Cards_Barbarians_evo_barb_dep_sfx_02.ogg",
        ],
        "accepted_guesses": [
            "barbarians",
            "barbs",
            "barbarian",
            "evo barbarians",
            "barbarian evolution",
            "evo barbs",
        ],
    },
    "Bats": {
        "filenames": [
            "Cards_Bats_bat_atk_01.ogg",
            "Cards_Bats_bat_deploy_01.ogg",
            "Cards_Bats_evo_bat_atk_01.ogg",
            "Cards_Bats_evo_bat_deploy_01.ogg",
        ],
        "accepted_guesses": ["bats", "bat", "evo bats", "bats evolution"],
    },
    "Battle Healer": {
        "filenames": [
            "Cards_Battle Healer_bh_atk_01_dl.ogg",
            "Cards_Battle Healer_bh_deploy_01_dl.ogg",
            "Cards_Battle Healer_bh_die_01_dl.ogg",
            "Cards_Battle Healer_bh_heal_01_dl.ogg",
        ],
        "accepted_guesses": ["battle healer", "healer", "bh"],
    },
    "Battle Ram": {
        "filenames": [
            "Cards_Battle Ram_battleram_charge_01.ogg",
            "Cards_Battle Ram_battleram_deploy_01.ogg",
            "Cards_Battle Ram_evo_battleram_dep_01.ogg",
        ],
        "accepted_guesses": [
            "battle ram",
            "ram",
            "evo battle ram",
            "evo ram",
            "battle ram evolution",
        ],
    },
    "Berserker": {
        "filenames": [
            "Cards_Berserker_card_common_berserker_atk_vo_01.ogg",
            "Cards_Berserker_card_common_berserker_atk_vo_02.ogg",
            "Cards_Berserker_card_common_berserker_atk_vo_03.ogg",
            "Cards_Berserker_card_common_berserker_atk_vo_06.ogg",
            "Cards_Berserker_card_common_berserker_deploy_vo_01.ogg",
            "Cards_Berserker_card_common_berserker_deploy_vo_02.ogg",
            "Cards_Berserker_card_common_berserker_deploy_vo_03.ogg",
            "Cards_Berserker_card_common_berserker_die_vo.ogg",
        ],
        "accepted_guesses": ["berserker"],
    },
    "Bomb Tower": {
        "filenames": ["Cards_Bomb Tower_building_explode_01.ogg"],
        "accepted_guesses": ["bomb tower", "bt"],
    },
    "Bomber": {
        "filenames": [
            "Cards_Bomber_deploy_skeleton_01.ogg",
            "Cards_Bomber_evo_bomber_dep_sfx_01.ogg",
        ],
        "accepted_guesses": ["bomber", "evo bomber", "bomber evolution", "barry"],
    },
    "Boss Bandit": {
        "filenames": [
            "Cards_Boss Bandit_card_champion_boss_bandit_attack_vo_a.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_attack_vo_b.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_attack_vo_e.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_bond_vo_01.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_bond_vo_02.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_bond_vo_03.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_bond_vo_04.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_bond_vo_05_a.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_bond_vo_05_b.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_bond_vo_06.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_bond_vo_07.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_born_vo_02.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_born_vo_03.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_born_vo_04.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_born_vo_05.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_dash_vo_01_a.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_dash_vo_02.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_dash_vo_03.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_dash_vo_04.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_deploy_sfx.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_die_vo_b.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_idle_vo.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_skill2_cast.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_skill_cast_02_a.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_skill_cast_02_b.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_skill_vo_01.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_skill_vo_02.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_skill_vo_03.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_skill_vo_05.ogg",
            "Cards_Boss Bandit_card_champion_boss_bandit_skill_vo_06.ogg",
        ],
        "accepted_guesses": ["boss bandit", "bossbandit"],
    },
    "Bowler": {
        "filenames": [
            "Cards_Bowler_bowl_atk_03.ogg",
            "Cards_Bowler_bowl_atk_04.ogg",
            "Cards_Bowler_bowl_atk_05.ogg",
            "Cards_Bowler_bowler_deploy_vo_01.ogg",
            "Cards_Bowler_card_hero_bowler_deploy.ogg",
            "Cards_Bowler_card_hero_bowler_inrange.ogg",
            "Cards_Bowler_card_hero_bowler_skill_ball_hit.ogg",
            "Cards_Bowler_card_hero_bowler_skill_bgm.ogg",
            "Cards_Bowler_card_hero_bowler_skill_cast_sfx.ogg",
            "Cards_Bowler_card_hero_bowler_skill_cast_vo.ogg",
            "Cards_Bowler_card_hero_bowler_skill_light.ogg",
            "Cards_Bowler_card_hero_bowler_skill_vo_03.ogg",
        ],
        "accepted_guesses": ["bowler", "hero bowler"],
    },
    "Cannon Cart": {
        "filenames": ["Cards_Cannon Cart_rolling_cannon_deploy_01.ogg"],
        "accepted_guesses": ["cannon cart", "cart"],
    },
    "Cannon": {
        "filenames": [
            "Cards_Cannon_cannon_deploy_01.ogg",
            "Cards_Cannon_cannon_fire_03.ogg",
            "Cards_Cannon_evo_cannon_deploy_sfx_01.ogg",
        ],
        "accepted_guesses": ["cannon", "evo cannon"],
    },
    "Clone": {
        "filenames": ["Cards_Clone_clone_spell_01.ogg"],
        "accepted_guesses": ["clone"],
    },
    "Dark Prince": {
        "filenames": [
            "Cards_Dark Prince_b_knight_atk_02.ogg",
            "Cards_Dark Prince_b_knight_atk_03.ogg",
            "Cards_Dark Prince_b_knight_atk_charge_01.ogg",
            "Cards_Dark Prince_b_knight_atk_charge_02.ogg",
            "Cards_Dark Prince_card_hero_dark_prince_ability_activated.ogg",
            "Cards_Dark Prince_card_hero_dark_prince_ability_jump.ogg",
            "Cards_Dark Prince_card_hero_dark_prince_charge_cast.ogg",
            "Cards_Dark Prince_card_hero_dark_prince_charge_hit.ogg",
            "Cards_Dark Prince_card_hero_dark_prince_deploy_sfx.ogg",
            "Cards_Dark Prince_dark_prince_atk_hit_01.ogg",
            "Cards_Dark Prince_dark_prince_charge_jing_02.ogg",
            "Cards_Dark Prince_dark_prince_deploy_01.ogg",
        ],
        "accepted_guesses": ["dark prince", "hero dark prince", "dp", "hero dp"],
    },
    "Dart Goblin": {
        "filenames": [
            "Cards_Dart Goblin_blowdart_deploy_01.ogg",
            "Cards_Dart Goblin_blowdart_goblin_atk_02.ogg",
            "Cards_Dart Goblin_evo_gob_dart_atk_01.ogg",
            "Cards_Dart Goblin_evo_gob_dart_deploy_01.ogg",
        ],
        "accepted_guesses": [
            "dart goblin",
            "goggin",
            "evo dart goblin",
            "evo dart",
        ],
    },
    "Earthquake": {
        "filenames": ["Cards_Earthquake_scrollearthquake01.ogg"],
        "accepted_guesses": ["earthquake", "eq", "quake"],
    },
    "Electro Dragon": {
        "filenames": [
            "Cards_Electro Dragon_be_charge_01.ogg",
            "Cards_Electro Dragon_be_deploy_01.ogg",
            "Cards_Electro Dragon_be_deploy__end_01.ogg",
            "Cards_Electro Dragon_evo_dragon_atk_sfx_01.ogg",
            "Cards_Electro Dragon_evo_dragon_dep_sfx_01.ogg",
        ],
        "accepted_guesses": [
            "electro dragon",
            "edrag",
            "e dragon",
            "e drag",
            "evo electro dragon",
            "evo e drag",
            "evo e dragon",
            "evo edrag",
        ],
    },
    "Electro Giant": {
        "filenames": ["Cards_Electro Giant_elec_giant_dep_01.ogg"],
        "accepted_guesses": ["electro giant", "egiant", "e giant"],
    },
    "Electro Spirit": {
        "filenames": ["Cards_Electro Spirit_electro_spirit_dep_01.ogg"],
        "accepted_guesses": ["electro spirit", "espirit", "e spirit"],
    },
    "Electro Wizard": {
        "filenames": [
            "Cards_Electro Wizard_electro_wiz_atk_01.ogg",
            "Cards_Electro Wizard_electro_wiz_atk_02.ogg",
            "Cards_Electro Wizard_electro_wiz_atk_03.ogg",
            "Cards_Electro Wizard_electro_wiz_atk_04.ogg",
            "Cards_Electro Wizard_electro_wiz_atk_05.ogg",
            "Cards_Electro Wizard_electro_wiz_deploy_01.ogg",
        ],
        "accepted_guesses": ["electro wizard", "ewiz", "e wiz"],
    },
    "Elite Barbarians": {
        "filenames": ["Cards_Elite Barbarians_elite_barbs_deploy_01.ogg"],
        "accepted_guesses": ["elite barbarians", "ebarbs", "e barbs"],
    },
    "Elixir Collector": {
        "filenames": ["Cards_Elixir Collector_get_elixir_02.ogg"],
        "accepted_guesses": [
            "elixir collector",
            "pump",
            "e pump",
            "elixir pump",
        ],
    },
    "Elixir Golem": {
        "filenames": [
            "Cards_Elixir Golem_bigslime_atk_01.ogg",
            "Cards_Elixir Golem_bigslime_dep_end_01.ogg",
        ],
        "accepted_guesses": ["elixir golem", "egolem", "e golem"],
    },
    "Executioner": {
        "filenames": [
            "Cards_Executioner_card_evolution_executioner_attack_sfx_cast.ogg",
            "Cards_Executioner_card_evolution_executioner_attack_vo_02_a.ogg",
            "Cards_Executioner_card_evolution_executioner_attack_vo_02_b.ogg",
            "Cards_Executioner_card_evolution_executioner_attack_vo_02_c.ogg",
            "Cards_Executioner_card_evolution_executioner_born_vo_01.ogg",
            "Cards_Executioner_card_evolution_executioner_born_vo_02.ogg",
            "Cards_Executioner_card_evolution_executioner_born_vo_03.ogg",
            "Cards_Executioner_deploy_executioner_01.ogg",
            "Cards_Executioner_executioner_atk_01.ogg",
        ],
        "accepted_guesses": ["executioner", "exe", "evo executioner", "evo exe"],
    },
    "Fire Spirit": {
        "filenames": ["Cards_Fire Spirit_fire_spirit_deploy_01.ogg"],
        "accepted_guesses": [
            "fire spirit",
            "fire spirits",
            "fspirit",
            "f spirit",
        ],
    },
    "Fireball": {
        "filenames": [
            "Cards_Fireball_fire_ball_02.ogg",
            "Cards_Fireball_fire_ball_explo_02.ogg",
        ],
        "accepted_guesses": ["fireball", "fire ball"],
    },
    "Firecracker": {
        "filenames": [
            "Cards_Firecracker_evo_firecracker_dep_sfx_02.ogg",
            "Cards_Firecracker_firecracker_atk_01.ogg",
            "Cards_Firecracker_firecracker_dep_01.ogg",
            "Cards_Firecracker_firecracker_dep_vo_01.ogg",
            "Cards_Firecracker_firecracker_fireworks_01.ogg",
        ],
        "accepted_guesses": ["firecracker", "fc", "evo firecracker"],
    },
    "Fisherman": {
        "filenames": [
            "Cards_Fisherman_fm_atk_02.ogg",
            "Cards_Fisherman_fm_atk_hit_01.ogg",
            "Cards_Fisherman_fm_dep_01.ogg",
            "Cards_Fisherman_fm_dep_end_01.ogg",
        ],
        "accepted_guesses": ["fisherman", "fishman"],
    },
    "Flying Machine": {
        "filenames": ["Cards_Flying Machine_flying_machine_loop_01.ogg"],
        "accepted_guesses": ["flying machine", "flyingmachine", "fm"],
    },
    "Freeze": {
        "filenames": ["Cards_Freeze_freeze_04.ogg"],
        "accepted_guesses": ["freeze"],
    },
    "Furnace": {
        "filenames": [
            "Cards_Furnace_card_evo_furnace_atk_cast_01.ogg",
            "Cards_Furnace_card_evo_furnace_deploy.ogg",
            "Cards_Furnace_card_evo_furnace_fire_spirit_spawn_01.ogg",
            "Cards_Furnace_card_rare_furnace_atk_cast_01.ogg",
            "Cards_Furnace_card_rare_furnace_deploy.ogg",
        ],
        "accepted_guesses": ["furnace"],
    },
    "Giant Skeleton": {
        "filenames": [
            "Cards_Giant Skeleton_big_skeleton_summon_01.ogg",
            "Cards_Giant Skeleton_giant_skelly_dep_vo_01.ogg",
        ],
        "accepted_guesses": ["giant skeleton", "giant skelly", "gs"],
    },
    "Giant Snowball": {
        "filenames": [
            "Cards_Giant Snowball_evo_snowball_deploy_01.ogg",
            "Cards_Giant Snowball_evo_snowball_land_01.ogg",
            "Cards_Giant Snowball_snowball_impact_01.ogg"
        ],
        "accepted_guesses": ["giant snowball", "snowball", "evo snow", "evo giant snowball", "evo snowball", "snow"],
    },
    "Giant": {
        "filenames": [
            "Cards_Giant_giant_deploy_01.ogg",
            "Cards_Giant_giant_attack_swing_01.ogg",
            "Cards_Giant_card_hero_giant_skill.ogg",
            "Cards_Giant_card_hero_giant_deploy_vo.ogg",
            "Cards_Giant_card_hero_giant_deploy_jingle_stereo.ogg",
            "Cards_Giant_card_hero_giant_atk_vo_b.ogg",
            "Cards_Giant_card_hero_giant_atk_hit_a.ogg"
        ],
        "accepted_guesses": ["giant", "hero giant"],
    },
    "Goblin Barrel": {
        "filenames": [
            "Cards_Goblin Barrel_barrel_drawback_14.ogg",
            "Cards_Goblin Barrel_barrel_explosion_02.ogg",
            "Cards_Goblin Barrel_evo_gob_barrel_dep_01.ogg"
        ],
        "accepted_guesses": ["goblin barrel", "gb", "barrel", "evo goblin barrel"],
    },
    "Goblin Cage": {
        "filenames": [
            "Cards_Goblin Brawler_cage_gob_dep_01.ogg",
            "Cards_Goblin Brawler_cage_gob_hit_01.ogg",
            "Cards_Goblin Brawler_prison_cage_gob_drop_02.ogg",
            "Cards_Goblin Cage_evo_gob_cage_break_01.ogg",
            "Cards_Goblin Cage_evo_gob_cage_dep_01.ogg",
            "Cards_Goblin Cage_goblin_cage_fight_loop_01.ogg"
        ],
        "accepted_guesses": ["goblin cage", "cage", "evo goblin cage", "evo cage", "diddy cage", "evo diddy cage"],
    },
    "Goblin Curse": {
        "filenames": [
            "Cards_Goblin Curse_gob_spell_transformation_01.ogg",
            "Cards_Goblin Curse_goblin_curse_spell_02.ogg"
        ],
        "accepted_guesses": ["goblin curse", "curse"],
    },
    "Goblin Demolisher": {
        "filenames": [
            "Cards_Goblin Demolisher_gob_demo_atk_01.ogg",
            "Cards_Goblin Demolisher_gob_demo_charge_01.ogg",
            "Cards_Goblin Demolisher_gob_demo_dep_vo_01.ogg",
            "Cards_Goblin Demolisher_gob_demo_explo_01.ogg"
        ],
        "accepted_guesses": ["goblin demolisher", "demolisher"],
    },
    "Goblin Drill": {
        "filenames": [
            "Cards_Goblin Drill_gob_drill_up_02.ogg",
            "Cards_Goblin Drill_evo_gob_drill_deploy_01.ogg",
            "Cards_Goblin Drill_evo_gob_drill_up_01.ogg",
            "Cards_Goblin Drill_evo_goib_drill_dis_01.ogg",
            "Cards_Goblin Drill_gob_drill_down_01.ogg",
            "Cards_Goblin Drill_gob_drill_loop_01.ogg"
        ],
        "accepted_guesses": ["goblin drill", "drill", "evo goblin drill", "evo drill"],
    },
}


def pick_random_card():
    card_name = random.choice(list(sound_library.keys()))
    sound_file = random.choice(sound_library[card_name]["filenames"])
    return card_name, sound_file


if "current_card" not in st.session_state:
    card, sound = pick_random_card()
    st.session_state.current_card = card
    st.session_state.sound_file = sound
    st.session_state.feedback = ""
    st.session_state.user_guess = ""

def next_sound_callback():
    card, sound = pick_random_card()
    st.session_state.current_card = card
    st.session_state.sound_file = sound
    st.session_state.feedback = ""
    st.session_state.user_guess = ""

st.title("Clash Royale Sound Guessing game")

current_card = st.session_state.current_card
sound_path = os.path.join(BASE_DIR, st.session_state.sound_file)

st.write("Made by ExplosiveBones &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (v.7.8)")
st.write("")
st.write("Listen to the sound effect below:")
if os.path.exists(sound_path):
    st.audio(sound_path, format="audio/ogg")
else:
    st.warning(
        f"Audio file not found at path: `{sound_path}`. Make sure all `.ogg` files are uploaded."
    )

with st.form(key="guess_form"):
    user_guess = (
        st.text_input("Guess the Clash Royale card:", key="user_guess")
        .strip()
        .lower()
    )

    submitted = st.form_submit_button("Submit Guess")

    if submitted:
        accepted = sound_library[current_card]["accepted_guesses"]
        if user_guess in accepted:
            st.session_state.feedback = "correct"
        else:
            st.session_state.feedback = "incorrect"

st.button("Next Sound", on_click=next_sound_callback)

if st.session_state.feedback == "correct":
    st.success("Correct!")
elif st.session_state.feedback == "incorrect":
    st.error(f"Incorrect! The answer was **{current_card}**.")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("Made and coded by ExplosiveBones, sound effects belong to Supercell, sound effects that come from multiple cards have been omitted as well as sounds that are near impossible to determine the source of, the first number of the version in the top right corner correlates to the latest letter of the alphabet that a card's name may start with, and the second number is the amount of cards that have been added starting with that letter (ex. v7.5 meand 5 cards that start with the letter 'g' have been added as well as everything before that).")
