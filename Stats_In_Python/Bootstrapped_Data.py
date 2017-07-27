# Bootstrapped data is simply data that has been resampled in order to simulate new data. It's a great way to statistically validate
# and test your data ;)

# so for say the admissions data from earlier:

for _ in range(50):
    # Generate bootstrap sample: bs_sample
    bs_sample = np.random.choice(admissions, size=len(admissions))

    # Compute and plot ECDF from bootstrap sample
    x, y = ecdf(bs_sample)
    _ = plt.plot(x, y, marker='.', linestyle='none',
                 color='gray', alpha=0.1)

# Compute and plot ECDF from original data
x, y = ecdf(admissions)
_ = plt.plot(x, y, marker='.')

# Make margins and label axes
plt.margins(0.02)
_ = plt.xlabel('yearly admissions (total)')
_ = plt.ylabel('ECDF')

# Show the plot
plt.show()

# the bootstrap samples give one an idea of how admissions are spread

# To generate the bootstrap samples it is much easier to write some functions out:

def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))

def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicates."""

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates

# one can then use the bootstrap replicates to calculate the standard error of the mean

# Take 10,000 bootstrap replicates of the mean: bs_replicates
bs_replicates = draw_bs_reps(admissions, np.mean, size=10000)

# Compute and print SEM
sem = np.std(admissions) / np.sqrt(len(admissions))
print(sem)

# Compute and print standard deviation of bootstrap replicates
bs_std = np.std(bs_replicates)
print(bs_std)

# Make a histogram of the results
_ = plt.hist(bs_replicates, bins=50, normed=True)
_ = plt.xlabel('mean annual admissions (number')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()

# Calculate the confidence intervals:
np.percentile(bs_replicates, [2.5, 97.5])

# This shows how powerful bootstrapped data can be in validating results and computing confidence intervals.

# You can also use it to plot the variance:

# Generate 10,000 bootstrap replicates of the variance: bs_replicates
bs_replicates = draw_bs_reps(admissions, np.var, size = 10000)

# Put the variance in units of single patients rather than hundreds as it was in the initial data
bs_replicates /= 100

# Make a histogram of the results
_ = plt.hist(bs_replicates, normed = True, bins = 50)
_ = plt.xlabel('variance of admissions (numbers)')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()

# You can also bootstrap data in pairs to use it for regression problems by using np.polyfit as well.

def draw_bs_pairs_linreg(x, y, size=1):
    """Perform pairs bootstrap for linear regression."""

    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))

    # Initialize replicates: bs_slope_reps, bs_intercept_reps
    bs_slope_reps = np.empty(size)
    bs_intercept_reps = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, size=len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_slope_reps[i], bs_intercept_reps[i] = np.polyfit(bs_x, bs_y, 1)

    return bs_slope_reps, bs_intercept_reps

# for the histogram:

# Generate replicates of slope and intercept using pairs bootstrap
bs_slope_reps, bs_intercept_reps = draw_bs_pairs_linreg(
                    admission_rate, death, size=1000)

# Compute and print 95% CI for slope
print(np.percentile(bs_slope_reps, [2.5, 97.5]))

# Plot the histogram
_ = plt.hist(bs_slope_reps, bins=50, normed=True)
_ = plt.xlabel('slope')
_ = plt.ylabel('PDF')
plt.show()

# for linear regression:

# Generate array of x-values for bootstrap lines: x
x = np.array([0, 100])

# Plot the bootstrap lines
for i in range(100):
    _ = plt.plot(x, bs_slope_reps[i] * x + bs_intercept_reps[i],
                 linewidth=0.5, alpha=0.2, color='red')

# Plot the data
_ = plt.plot(admission_rate, death, marker='.', linestyle='none')

# Label axes, set the margins, and show the plot
_ = plt.xlabel('admission rate')
_ = plt.ylabel('death %')
plt.margins(0.02)
plt.show()
