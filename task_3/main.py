def calculate_coin_probabilities():
    # Probabilities of getting 'H' for each of the 5 coins
    p_heads = [0.8, 0.9, 0.1, 0.2, 0.3]
    
    # Initial probabilities (we pick 1 coin out of 5 at random)
    prior_probs = [0.2, 0.2, 0.2, 0.2, 0.2]
    
    # The sequence of actual flips we observed
    flips = ['H', 'T', 'H', 'H', 'H', 'T', 'T', 'H', 'H']
    
    # Here we'll store the probability of getting 'H' on the *next* flip
    predicted_probs = []

    for flip in flips:
        new_probs = []
        
        for i in range(len(p_heads)):
            if flip == 'H':
                # If it's heads, multiply by the probability of heads
                new_probs.append(prior_probs[i] * p_heads[i])
            else:
                # If it's tails, multiply by the probability of tails (1 - P(H))
                new_probs.append(prior_probs[i] * (1.0 - p_heads[i]))
        
        # Normalize the probabilities so they sum to 1
        total_prob = sum(new_probs)
        prior_probs = [p / total_prob for p in new_probs]
        
        # Now, calculate the probability of getting 'H' on the next flip
        next_h_prob = sum(prior_probs[i] * p_heads[i] for i in range(len(p_heads)))
        
        # Round to 2 decimal places and save it
        predicted_probs.append(round(next_h_prob, 2))

    return predicted_probs

result = calculate_coin_probabilities()
print(f"Predicted probabilities: {result}")