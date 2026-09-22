def confidence_label(score, candidate_count=0):
    if candidate_count <= 1:
        return "Low"
    if score >= 0.80:
        return "High"
    if score >= 0.55:
        return "Medium"
    return "Low"

def candidate_confidence(candidates):
    if not candidates:
        return {"label":"Low", "score":0.0}
    scores = [float(c.get("ngram_score", c.get("score", 0.0))) for c in candidates]
    best = scores[0]
    second = scores[1] if len(scores) > 1 else best
    gap = max(0.0, best-second)
    normalized = min(1.0, gap / max(abs(best), 1.0) + (0.15 if best > 0 else 0.0))
    return {"label": confidence_label(normalized, len(candidates)), "score": round(normalized, 3)}
