import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3

personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    username='03097181-e06d-4918-9e4a-d73394e7872d',
    password='vfvHHDqJqDGl')

with open(join(dirname(__file__), 'personality-v3.json')) as \
        profile_json:
    profile = personality_insights.profile(
        profile_json.read(), content_type='application/json',
        raw_scores=True, consumption_preferences=True)

    print(json.dumps(profile, indent=2))
