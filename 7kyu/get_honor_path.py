def get_honor_path(honor_score, target_honor_score):
    if honor_score >= target_honor_score:
        return {}
    return {"1kyus": int((target_honor_score - honor_score)/2),
            "2kyus": (target_honor_score - honor_score) % 2}
