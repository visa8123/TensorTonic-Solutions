def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = recommended[:k]
    relevant = set(relevant)
    hits = sum(1 for items in top_k if items in relevant)
    
    precision = float(hits)/k if k > 0 else 0.0
    recall = float(hits)/len(relevant) if len(relevant) > 0 else 0.0

    return  [precision, recall]
    