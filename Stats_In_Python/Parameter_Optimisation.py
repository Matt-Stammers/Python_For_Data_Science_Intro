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

# Regression Problems
===========================

# by first plotting the pearson co-efficient we can also get an idea about the shape of the data and whether it is correlated:

# Plot the admission rate versus death
_ = plt.plot(admission_rate, death, marker='.', linestyle='none')

# Set the margins and label axes
plt.margins(0.02)
_ = plt.xlabel('admission rate')
_ = plt.ylabel('death rate')

# Show the plot
plt.show()

# Show the Pearson correlation coefficient
print(pearson_r(admission_rate, death))

# In order to plot the regression parameters we can use np.polyfit to calculate the slope and intercept.

# Plot the admission rate versus death
_ = plt.plot(death_rate, death, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('admission_rate')
_ = plt.ylabel('death')

# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(admission_rate, death, 1)

# Print the results to the screen
print('slope =', a, 'admissions per day / deaths in %')
print('intercept =', b, 'admissions per day')

# Make theoretical line to plot
x = np.array([0,100])
y = a * x + b

# Add regression line to your plot
_ = plt.plot(x, y)

# Draw the plot
plt.show()

# computing the sum of the residuals squared or RDD can also be done manually:
# Specify slopes to consider: a_vals
a_vals = np.linspace(0, 0.1, 200)

# Initialize sum of square of residuals: rss
rss = np.empty_like(a_vals)

# Compute sum of square of residuals for each value of a_vals
for i, a in enumerate(a_vals):
    rss[i] = np.sum((admission_rate - a*death - b)**2)

# Plot the RSS
plt.plot(a_vals, rss, '-')
plt.xlabel('slope (admission rate / percent who died)')
plt.ylabel('sum of square of residuals')

plt.show()

# However, don't be blindly guided by these figures, all the numbers can look just dandy but as anscombe's quartet quite rightly points out
# Look before you leap - thus always start with graphical EDA.
=============
