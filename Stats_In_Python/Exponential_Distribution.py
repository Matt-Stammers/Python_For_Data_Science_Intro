# This is based on the time intervals between events in a a poisson process. If we draw samples using random.exponential()

def successive_poisson(tau1, tau2, size=1):
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size=size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size=size)

    # Then add them together
    return t1 + t2

# we can then plot them

# Draw samples of waiting times
waiting_times = successive_poisson(764, 715, size=100000)

# Make the histogram
_ = plt.hist(waiting_times, bins=100, histtype='step',
             normed=True)

# Label axes
_ = plt.xlabel('total waiting time (between patient long stays)')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()

# voila!
