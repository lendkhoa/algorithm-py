def getMinTime(n, requests, minGap):
    freq = collections.Counter(tasks)
        
        max_freq = max(freq.values())
        print(freq)
        print(max_freq)
        freq = list(freq.values())
        max_freq_ele_count = 0                 # total_elements_with_max_freq, last row elements
        i = 0
        while( i < len(freq)):
            print(f'{freq[i]} vs {max_freq}')
            if freq[i] == max_freq:
                max_freq_ele_count += 1
            i += 1
            
        ans = (max_freq - 1) * (n+1) + max_freq_ele_count
        
        return max(ans, len(tasks))
