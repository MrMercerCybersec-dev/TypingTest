# ⌨️ Type-Speed Engine

An interactive, raw console-based Typing Velocity Monitor built natively in Python using the `curses` library layout framework. It tracks user tactile accuracy and keystroke input bursts to compute real-time performance distributions.

## 🚀 Architectural Advantages
- **No Heavy Third-Party Dependencies:** Leverages Python standard modules (`curses`, `time`, `random`) for instantaneous workspace load-times.
- **Dynamic Color Feedback Pipeline:** Live screen buffers paint strings inline—printing standard green tracking for perfect entries or red highlighting for code execution typos.
- **WPM Evaluation Logic:** Computes raw speed utilizing standard metric constraints:  
  $$\text{WPM} = \frac{\text{Gross Keystrokes} / 5}{\text{Time In Minutes}}$$

## 🛠️ Launch & Verification Chain


## 🛠️ How to Run the Engine

Follow these steps to clone the repository and launch the typing test directly from your command line interface.

### 1. Download the Project
Open your terminal and clone your repository live from GitHub, then move directly into the project directory:

```bash
git clone https://github.com/MrMercerCybersec-dev/TypingTest.git
cd TypingTest
python3 typing_test.py

### 1. Requirements Prep
Since it uses standard console controls, it works natively out of the box on Linux/macOS environments.

*(If you are launching on a native Windows terminal framework, run this to install standard curses bindings first)*:
```bash
pip install windows-curses
