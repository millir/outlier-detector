# outlier-detector

This application detects outlier data points, informs the user of the outliers found, and then writes a clean version of the data with the outlier points removed to file.

Because the algorithm should not have access to any future data during the analysis of any given point, I have decided to go for a single pass approach to create this outlier detector. I have created a streamer class that updates its internal state with a new mean and variance for each new data point. By reading the input exactly once, our algorithm requires O(n) time, and since we eliminate the need for storing all of the historical data, it has O(1) storage. This should theoretically make the application extensible to much larger data streaming inputs.

The outlier is determined as lying a configurable number of standard deviations (z-scores - default 3) away from the sample mean.

I first implemented a cumulative approach, found it to not be flexible for longer timeseries data, and then created a moving sliding window with better results. These are on separate branches.


## Moving average
For this approach, I have created a sliding window of configurable length. This stores recent data from the stream, and pops values older than the window_size. The selection of the window_size affects the amount of smoothing: increasing the value of M improves the smoothing at the expense of accuracy. The sliding window allows us to pick up trends effectively.

## Cumulative average
I have used  [Welford's algorithm](https://www.wikiwand.com/en/Algorithms_for_calculating_variance#/) to calculate a rolling mean and variance with high numerical stability. We start with mean and variance of zero, and then update these as we iterate through the datastream, using the sum of squares of differences from the current mean (denoted as M2 in the code).

This approach is less useful for trends, as the value of the mean becomes stuck to the population mean. This approach raised lots of outliers for the latter half of the data, in which prices had gone up steadily.
