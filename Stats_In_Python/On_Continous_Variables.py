# Generating Probability Distribution and Cumulative Distribution Functions for the Normal Distribution

# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
samples_std1 = np.random.normal(20, 1, size=100000)
samples_std3 = np.random.normal(20, 3, size=100000)
samples_std10 = np.random.normal(20, 10, size=100000)

# Make histograms
_ = plt.hist(samples_std1, bins=100, normed=True, histtype='step')
_ = plt.hist(samples_std3, bins=100, normed=True, histtype='step')
_ = plt.hist(samples_std10, bins=100, normed=True, histtype='step')

# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()

# Generate CDFs
x_std1, y_std1 = ecdf(samples_std1)
x_std3, y_std3 = ecdf(samples_std3)
x_std10, y_std10 = ecdf(samples_std10)

# Plot CDFs
_ = plt.plot(x_std1, y_std1, marker='.', linestyle='none')
_ = plt.plot(x_std3, y_std3, marker='.', linestyle='none')
_ = plt.plot(x_std10, y_std10, marker='.', linestyle='none')

# Make 2% margin
plt.margins(0.02)

# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()

# Say we wanted to plot the normal distribution of patient's stay in hospital to see if it follows a normal distribution

# Compute mean and standard deviation: mu, sigma to get the shape of the curve
mu = np.mean(patient_stay)
sigma = np.std(patient_stay)

# Sample out of a normal distribution with this mu and sigma: samples
samples = np.random.normal(mu, sigma, size = 10000)

# Get the CDF of the samples and of the data - we can then get an idea of how long patient's stayed compared to the perfect normal distribution
x_theor, y_theor = ecdf(samples)
x, y = ecdf(patient_stay)

# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)

# say we had a patient who stayed over 1000 days. Could we work out the probability of this event happening again?

# Take a million samples out of the Normal distribution: samples (as per prev with the mu and sigma already calculated.
samples = np.random.normal(mu, sigma, size = 1000000)

# Compute the fraction that stayed over 1000 days: prob
a = samples >= 1000
b = sum(a)
print(b)
prob = b / len(samples)

# Print the result
print('Probability of patient staying over 1,000 days:', prob)
