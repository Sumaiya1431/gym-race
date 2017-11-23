from gym.envs.registration import register

register(
    id='Race-v0',
    entry_point='gym_race.envs:RaceEnv',
)
register(
    id='RaceExtrahand-v0',
    entry_point='gym_race.envs:RaceExtrahandEnv',
)

