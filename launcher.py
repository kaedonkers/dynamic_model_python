from dynamic_model.simulator import Simulator


def launch_simulation(simulation_name, plot=True):
    # Create and initialize simulator object
    sim = Simulator()
    sim.initialize(simulation_name)

    # Launch the simulation itself
    sim.run_simulation()

    # And plot the results, if requested
    if plot: 
        sim.plot_results()

if __name__=="__main__":
    # Launch simulation
    launch_simulation("simulation_1")
