import streamlit as st
import subprocess

if __name__ == "__main__":
    # This launches the UI script when main.py runs
    subprocess.run(["streamlit", "run", "UI.py"])

