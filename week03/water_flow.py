import math
def water_column_height(tower_height, tank_height):
    """Return the height of a column of water, using a tower height
    and a tank wall height. 
    Ecuation: h = t + 3w/4
    where
        h is height of the water column
        t is the height of the tower
        w is the height of the walls of the tank
          that is on top of the tower

    Parameters
        tower_height: float number from tower height
        tank_height: float number from tank wall height
    Return: float number of height of a column of water.
    """
    column_height = tower_height + ((3 * tank_height) / 4)
    return column_height

def pressure_gain_from_water_height(height):
     """Return the pressure caused by Earth’s
        gravity pulling on the water stored in an
        elevated tank
    Ecuation: P = (ρgh)/1000
    where
        P is the pressure in kilopascals
        ρ is the density of water 
          998.2 ( kilogram / meter3) *Just use 
          #in your calculations
        g is the acceleration from 
          Earths gravity 9.80665 (meter / second2) * Just use
            #in your calculations
        h is the height of the water column in meters

    Parameters
        height: float value from height of the water column in meters.
    Return: float value of pressure."""
     
     pressure = (998.2  * 9.80665 * height) / 1000
     return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
     """calculates and returns the water pressure lost
       because of the friction between the water and 
       the walls of a pipe that it flows through
       Ecuation: P = (− f* L *8 ρ * v2)/ 2000 * d

       where:
        P is the lost pressure in kilopascals
        f is the pipe’s friction factor
        L is the length of the pipe in meters
        ρ is the density of water 998.2 (kilogram / meter3) 
            *Just use # in your calculations
        v is the velocity of the water flowing through 
            the pipe in meters / second
        d is the diameter of the pipe in meters
    Parameters
        pipe_diameter: float value diameter of the pipe in meters
        pipe_length: float value length of the pipe in meters
        friction_factor: float value of friction factor
        fluid_velocity: float value of velocity of the water flowing through 
            the pipe in meters / second

    Return: float value of lost pressure in kilopascals.
       """
     lost_pressure = (-friction_factor * pipe_length * 998.2 * math.pow(fluid_velocity, 2)) / (2000 * pipe_diameter)

     return lost_pressure

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
     """calculates the water pressure lost because
       of fittings such as 45° and 90° bends that are 
       in a pipeline.
       Ecuation: P = (−0.04 * ρ *v2 *n )/ 2000

       where:
        P is the lost pressure in kilopascals
        ρ is the density of water (998.2 kilogram / meter3)
        v is the velocity of the water flowing through the pipe in meters / second
        n is the quantity of fittings
    Parameters
        fluid_velocity: float value water's velocity
        quantity_fittings: int value fittings quantity
        
    Return: float value of loss pressure in kilopascals.
       """
     loss_pressure = (-0.04 * 998.2 * math.pow(fluid_velocity, 2) * quantity_fittings) / 2000
     return loss_pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
     """calculates and returns the Reynolds number for
       a pipe with water flowing through it. The Reynolds 
       number is a unitless ratio of the inertial and viscous
        forces in a fluid that is useful for predicting fluid 
        flow in different situations

       Ecuation: R = (ρ * d * v)/ μ

       where:
        R is the Reynolds number
        ρ is the density of water (998.2 kilogram / meter3)
        d is the hydraulic diameter of a pipe in meters. For a round pipe, 
            the hydraulic diameter is the same as the pipe’s inner diameter.
        v is the velocity of the water flowing through the pipe in meters / second
        μ is the dynamic viscosity of water (0.0010016 Pascal seconds)
    Parameters
        hydraulic_diameter: float value the hydraulic diameter of a pipe in meters
        fluid_velocity: float value water's velocity
        
    Return: float value of Reynolds number for a pipe with water flowing through it.
       """
     reynolds_number = (998.2 * fluid_velocity * hydraulic_diameter) / 0.0010016
     return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
     """calculates the water pressure lost because of
       water moving from a pipe with a large diameter 
       into a pipe with a smaller diameter

       Ecuations: k = (0.1 + 50/R) * ((D/d)^4 − 1)
       P = −k ρ v2 / 2000

       where:
        k is a constant computed by the first formula and used in the second formula
        R is the Reynolds number that corresponds to the pipe with the larger diameter
        D is the diameter of the larger pipe in meters
        d is the diameter of the smaller pipe in meters
        P is the lost pressure kilopascals
        ρ is the density of water (998.2 kilogram / meter3)
        v is the velocity of the water flowing through the larger diameter pipe in meters / second
        Parameters
            larger_diameter: float value the diameter of the larger pipe in meters
            fluid_velocity: float value water's velocity
            reynolds_number: float value of Reynolds number for a pipe with water flowing through it.
            smaller_diameter: the diameter of the smaller pipe in meters
        
    Return: float value of pressure lost because of water 
            moving from a pipe with a large diameter into a     
            pipe with a smaller diameter
       """
     k = (0.1 + (50/reynolds_number)) * (math.pow((larger_diameter/smaller_diameter), 4) -1)
     pressure_loss = (-k * 998.2 *math.pow(fluid_velocity, 2)) / 2000

     return pressure_loss
     
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()


