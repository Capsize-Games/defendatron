# Defendatron

Defendatron is a simple coordinator for `Protectbots`, Python modules that provide security features for your applications.

---

![img_1.png](img.png)

[![Upload Python Package](https://github.com/Capsize-Games/defendatron/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Capsize-Games/defendatron/actions/workflows/python-publish.yml)

---

## Installation

```bash
pip install defendatron
```

## Usage

```python
import defendatron

# Activate defendatron (all protectbots)
defendatron.activate()

# Deactivate defendatron (all protectbots)
defendatron.deactivate()

# Activate specific protectbots
defendatron.nullscream.activate()
defendatron.shadowlogger.activate()
defendatron.darklock.activate()

# Deactivate specific protectbots
defendatron.nullscream.deactivate()
defendatron.shadowlogger.deactivate()
defendatron.darklock.deactivate()
```

See `src/defendatron/__init__.py` for more advanced usage.

## When Protecbots assemble, they create DEFENDATRON
![img_2.png](img_1.png)

---

Defendatron is built with `Protectbots`, Python modules that provide security features for your applications. 
Each `Protectbot` is designed to defend against specific threats and vulnerabilities, 
helping to provide another layer of protection for your code. 

- [NULLSCREAM](https://github.com/Capsize-Games/nullscream) Responsible for masquerading as other libraries in order to cancel out their operations. Useful when you are unable to modify the code of a library that you are using, but you want to prevent it from performing certain operations.
- [DARKLOCK](https://github.com/Capsize-Games/darklock) Responsible for locking down your application and preventing it from performing certain operations.
- [SHADOWLOGGER](https://github.com/Capsize-Games/shadowlogger) Intercepts all logs and shadows them, preventing sensitive information from being leaked.
