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

# This shows how powerful bootstrapped data can be in validating results and computing confidence intervals.
