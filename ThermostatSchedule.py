import os
import sys
sys.path.append('C:\\EnergyPlusV9-3-0')
from pyenergyplus.plugin import EnergyPlusPlugin
import random

class ThermostatSetpoint_Override(EnergyPlusPlugin):
    def __init__(self):
        super().__init__()
        self.need_to_get_handles = True
        self.handle = None
        self.n = 0
        self.n_warmup = 0
    def on_end_of_zone_timestep_after_zone_reporting(self,state) -> int:
        self.current_environment_num = self.api.exchange.current_environment_num(state)
        self.warmup_flag = self.api.exchange.warmup_flag(state)
        if self.need_to_get_handles:
            self.heating_handles={}
            self.heating_handles[0] = self.api.exchange.get_actuator_handle(state,
                "Schedule:Compact", "Schedule Value", "HTGSETP_SCH_Core"
                )
            self.heating_handles[1] = self.api.exchange.get_actuator_handle(state,
                "Schedule:Compact", "Schedule Value", "HTGSETP_SCH_1"
                )
            self.heating_handles[2] = self.api.exchange.get_actuator_handle(state,
                "Schedule:Compact", "Schedule Value", "HTGSETP_SCH_2"
                )
            self.heating_handles[3] = self.api.exchange.get_actuator_handle(state,
                "Schedule:Compact", "Schedule Value", "HTGSETP_SCH_3"
                )
            self.heating_handles[4] = self.api.exchange.get_actuator_handle(state,
                "Schedule:Compact", "Schedule Value", "HTGSETP_SCH_4"
                )
            self.cooling_handles={}
            self.cooling_handles[0] = self.api.exchange.get_actuator_handle(state,
                "Schedule:Compact", "Schedule Value", "CLGSETP_SCH_Core"
                )
            self.cooling_handles[1] = self.api.exchange.get_actuator_handle(state,
                "Schedule:Compact", "Schedule Value", "CLGSETP_SCH_1"
                )
            self.cooling_handles[2] = self.api.exchange.get_actuator_handle(state,
                "Schedule:Compact", "Schedule Value", "CLGSETP_SCH_2"
                )
            self.cooling_handles[3] = self.api.exchange.get_actuator_handle(state,
                "Schedule:Compact", "Schedule Value", "CLGSETP_SCH_3"
                )
            self.cooling_handles[4] = self.api.exchange.get_actuator_handle(state,
                "Schedule:Compact", "Schedule Value", "CLGSETP_SCH_4"
                )
            
        if (self.current_environment_num == 3) & (self.warmup_flag==0):
            for i in range(5):
                if random.choice([0,1,1,1,1,1,1,1])==0:
                    SP = random.uniform(15, 32)
                    SP_range = random.uniform(0.1, 5)
                    self.api.exchange.set_actuator_value(state,self.heating_handles[i], SP)
                    self.api.exchange.set_actuator_value(state,self.cooling_handles[i], SP+SP_range)
            self.n+=1
        return 0