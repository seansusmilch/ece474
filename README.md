# 💻 ECE 474 Project

By Matthew Nelmark and Sean Susmilch

The goal of this project is to write a simulator for Tomasulo's algorithm.

## How To Run It

1. Have python3 installed
2. Clone repo `git clone https://github.com/seansusmilch/ece474`
3. Install requirements `pip install -r requirements.txt`
4. Run it `python processor.py`

---
## Project Stuff

Dividing it up into some major parts

### Add Unit

* can add and subtract
* each operation takes 2 cycles
* has 3 reservation stations (RS1-RS3)

### Multiply Unit

* can multiply and divide
* multiplication takes 10 cycles
* division takes 40 cycles
* has 2 reservation stations (RS4-RS5)

### Register

* has 8 registers (R0-R7)

### Restrictions

* cannot do same-cycle issue and dispatch
* cannot free and allocate a RS in the same cycle
* if the add unit and multiply unit try to brodcast in the same cycle, multiply unit will go first
* if multiple insts in the reservation station are ready to dispatch in the same cycle, dispatch in order (ex. RS1 then RS2 then RS3)
* instruction queue can hold up to 10 instructions
* Opcodes 0: add; 1: sub; 2: multiply; 3: divide

## Project Board

In the project board thing we can track work that needs to be done and the work that we're doing.

* Add stuff that needs to be done to **ToDo**
* Move stuff we're working on to **In progress**
  * We each have our own In progress column
* Move finished work to **Done**

