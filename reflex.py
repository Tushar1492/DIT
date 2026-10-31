class SimpleReflexVacuumAgent:
    def __init__(self):
        self.location = "A"
        self.percept_sequence = []
        self.actions = []

    def add_percept(self, location, is_dirty):
        self.percept_sequence.append((location, is_dirty))

    def add_action(self, action):
        self.actions.append(action)

    def execute_actions(self):
        for action in self.actions:
            print(f"Percept: {self.percept_sequence.pop(0)} - Action: {action}")
            if action == "Suck":
                print("Vacuuming dirt.")
            elif action == "MoveLeft":
                self.location = "A"
                print("Moving left to location A.")
            elif action == "MoveRight":
                self.location = "B"
                print("Moving right to location B.")
            elif action == "DoNothing":
                print("Doing nothing.")

def simple_reflex_vacuum_agent(percept_sequence):
    agent = SimpleReflexVacuumAgent()

    for percept in percept_sequence:
        location, is_dirty = percept
        agent.add_percept(location, is_dirty)

        if is_dirty:
            agent.add_action("Suck")
        else:
            if location == "A":
                agent.add_action("MoveRight")
            elif location == "B":
                agent.add_action("MoveLeft")

    return agent

# Example percept sequence
percept_sequence = [("A", True), ("A", False), ("B", True), ("B", False)]

# Create and run the agent
agent = simple_reflex_vacuum_agent(percept_sequence)
agent.execute_actions()




# Design and Implement a Simple Reflex Agent for the Vacuum Cleaner World and
# Analyze Its Rational Behavior in a Given Environment
# Aim
# To design and implement a Simple Reflex Agent for the Vacuum Cleaner World and
# analyze its rational behavior based on the current percept of the environment.
# Objectives
# 1. To understand the concept of an intelligent agent.
# 2. To understand the working of a Simple Reflex Agent.
# 3. To implement a Vacuum Cleaner Agent using Python.
# 4. To analyze the agent&#39;s actions for different environmental conditions.
# 5. To understand the concept of rational behavior of an AI agent.

# Theory:
# What is an Intelligent Agent?
# An intelligent agent is a system that perceives its environment through sensors and
# performs actions through actuators to achieve a goal.
# Basic structure:
# Environment → Sensors → Agent → Actuators → Environment
# For a vacuum cleaner:
#  Sensors: Detect the current location and whether the floor is clean or dirty.
#  Agent: Decides what action to perform.

#  Actuators: Move the vacuum cleaner or perform cleaning.
#  Environment: Rooms/floor locations containing clean or dirty surfaces.

# Vacuum Cleaner World
# Consider a simple environment containing two locations:
#  Location A
#  Location B
# Each location can have one of two states:
#  Clean
#  Dirty
# The vacuum cleaner can perform the following actions:
# Condition Action
# Current location is Dirty
# - Suck
# Current location is Clean and agent is at
# A

# - Move
# Right
# Current location is Clean and agent is at
# B

# - Move
# Left

# Example
# Suppose the initial environment is:
# Locatio
# n

# Statu
# s
# A Dirty
# B Dirty
# Agent starts at A.

# The agent performs:
# A Dirty → Suck → A Clean → Move Right → B Dirty → Suck → B Clean
# Thus, the agent cleans both locations.

# Simple Reflex Agent
# A Simple Reflex Agent selects an action based only on the current percept.
# It uses condition-action rules:
# IF condition THEN action
# For example:
#  IF current location is dirty → Suck
#  IF current location is clean and agent is at A → Move Right
#  IF current location is clean and agent is at B → Move Left
# The agent does not maintain a detailed history of previous states.

# PEAS Description
# PEAS stands for:
# P – Performance Measure
# E – Environment
# A – Actuators
# S – Sensors
# Component Vacuum Cleaner Agent
# Performance
# Measure

# Maximum cleanliness, minimum unnecessary movement,
# minimum time/energy

# Environment Two-room environment: A and B
# Actuators Suck, Move Left, Move Right
# Sensors Current location and cleanliness status

# Algorithm
# Algorithm: Simple Reflex Vacuum Cleaner Agent
# Step 1: Start.
# Step 2: Define the environment with two locations A and B.
# Step 3: Set the initial position of the vacuum cleaner.
# Step 4: Read the current location and its cleanliness status.
# Step 5: If the current location is dirty, perform Suck.
# Step 6: If the current location is clean:
#  If the agent is at A, move to B.
#  If the agent is at B, move to A.
# Step 7: Update the environment after every action.
# Step 8: Repeat the process for a specified number of steps.

# Step 9: Display the actions performed and final environment.
# Step 10: Stop.