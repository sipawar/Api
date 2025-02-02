import random
import pytest


def test_network_response_simulator():
    # Simulate network response time variations leading to occasional timeout scenarios.
    # In a real scenario, this could be due to varied server responsiveness or network issues.
    simulated_response_time = random.choice([0.01, 0.02, 0.5, 0.03, 0.5])  # 0.5 simulating a timeout threshold

    # Assert that the response time is below 0.1 seconds to simulate the test sometimes failing.
    assert simulated_response_time < 0.1, "Test failed due to simulated timeout"