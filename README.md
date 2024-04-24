# When Protecbots assemble, they create DEFENDRON

---

![img_1.png](img.png)

---

## Installation

```bash
pip install defendron
```

## Usage

```python
import defendron

# Activate defendron (all protectbots)
defendron.activate()

# Deactivate defendron (all protectbots)
defendron.deactivate()

# Activate specific protectbots
defendron.nullscream.activate()
defendron.shadowlogger.activate()
defendron.lockdown.activate()

# Deactivate specific protectbots
defendron.nullscream.deactivate()
defendron.shadowlogger.deactivate()
defendron.lockdown.deactivate()
```

## When Protecbots assemble, they create DEFENDRON
![img_2.png](img_1.png)

---

Defendron is built with `Protectbots`, Python modules that provide security features for your applications. 
Each `Protectbot` is designed to defend against specific threats and vulnerabilities, 
helping to provide another layer of protection for your code. 

- [NULLSCREAM](https://github.com/Capsize-Games/nullscream) Responsible for masquerading as other libraries in order to cancel out their operations. Useful when you are unable to modify the code of a library that you are using, but you want to prevent it from performing certain operations.
- [LOCKDOWN](https://github.com/Capsize-Games/lockdown) Responsible for locking down your application and preventing it from performing certain operations.
- [SHADOWLOGGER](https://github.com/Capsize-Games/shadowlogger) Intercepts all logs and shadows them, preventing sensitive information from being leaked.
