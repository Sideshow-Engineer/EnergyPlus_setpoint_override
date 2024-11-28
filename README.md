## Overview
This is a demo using an EnergyPlus plugin to override the setpoint schedule of the EnergyPlus model

## Files
1. ThermostatSchedule.py - this code which defines a class named ThermostatSetpoint_Override, works as the plugin overrides the setpoint schedule
2. test.idf - the EnergyPlus model. At the end of the idf file, a PythonPlugin:Instance object is added, which register the plugin ThermostatSchedule.py, so it can be identifed by the EnergyPlus simulation.
