# Parameter optimisation for the patient death data

# Seed random number generator
np.random.seed(42)

# Compute mean no-death time: tau
tau = np.mean(no_death_times)

# Draw out of an exponential distribution with parameter tau: inter_no_death_time
inter_no_death_time = np.random.exponential(tau, 100000)

# Plot the PDF and label axes
_ = plt.hist(inter_no_death_time,
             bins = 50, normed = True, histtype='step')
_ = plt.xlabel('Admissions between no-deaths')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()

# plotting the actual ecdf against the theoretical one

# Create a CDF from theoretical samples: x_theor, y_theor
x_theor, y_theor = ecdf(inter_no_death_time)

# Overlay the plots
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')

# Margins and axis labels
plt.margins(0.02)
plt.xlabel('Admissions between no-deaths')
plt.ylabel('CDF')
plt.show()

# To show how the best parameters are calculated directly from the mean of the data see what happens when you double or halve tau:

# Plot the theoretical CDFs
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('Deaths between admissions')
plt.ylabel('CDF')

# Take samples with half tau: samples_half
samples_half = np.random.exponential(tau/2, size = 10000)

# Take samples with double tau: samples_double
samples_double = np.random.exponential(tau*2, size = 10000)

# Generate CDFs from these samples
x_half, y_half = ecdf(samples_half)
x_double, y_double = ecdf(samples_double)

# Plot these CDFs as lines
_ = plt.plot(x_half, y_half)
_ = plt.plot(x_double, y_double)

# Show the plot
plt.show()
