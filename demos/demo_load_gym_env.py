#!/usr/bin/env python3
"""Simple check if the available gym environments load without any error."""
import gym
import argparse


def main():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        "--env_name",
        default="push",
        choices=["reach", "push"],
        help="Specify which gym env to load, push or reach",
    )
    args = argparser.parse_args()

    if args.env_name == "push":
        env = gym.make(
            "pybullet_fingers.gym_wrapper:push-v0",
            control_rate_s=0.02,
            finger_type="single",
            enable_visualization=True,
        )

    elif args.env_name == "reach":

        smoothing_params = {
            "num_episodes": 700,
            "start_after": 3.0 / 7.0,
            "final_alpha": 0.975,
            "stop_after": 5.0 / 7.0,
        }
        env = gym.make(
            "pybullet_fingers.gym_wrapper:reach-v0",
            control_rate_s=0.02,
            finger_type="single",
            smoothing_params=smoothing_params,
            enable_visualization=True,
        )

    for episode in range(700):
        env.reset()
        for step in range(100):
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)


if __name__ == "__main__":
    main()