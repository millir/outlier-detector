# outlier-detector

This application detects outlier data points, informs the user of the outliers found, and then writes a clean version of the data with the outlier points removed to file.

Because the algorithm should not have access to any future data during the analysis of any given point, I have decided to go for a single pass approach to create this outlier detector. I have created a streamer class that updates its internal state with a new mean and variance for each new data point. By reading the input exactly once, our algorithm requires O(n) time, and since we eliminate the need for storing all of the historical data, it has O(1) storage. This should theoretically make the application extensible to much larger data streaming inputs.

I have used  [Welford's algorithm](https://www.wikiwand.com/en/Algorithms_for_calculating_variance#/) to calculate a rolling mean and variance with high numerical stability. We start with mean and variance of zero, and then update these as we iterate through the datastream, using the sum of squares of differences from the current mean(denoted as M2 in the code).

Finally, the outlier is determined as lying a configurable number of standard deviations away from the sample mean.
