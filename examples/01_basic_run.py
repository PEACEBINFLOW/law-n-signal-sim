from law_n_signal_sim.simulator import SignalSimulator

sim = SignalSimulator()
for t, routes in sim.run(steps=3):
    print(f"t={t}")
    for row in routes:
        print(row)
