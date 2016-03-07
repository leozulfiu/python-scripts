# useful python scripts

I have these python scripts in my PATH variable which I use on a daily basis.

**syn** gives you synonyms to a given word

**kw** gives you the current calendar week

**stp** gives you your timetable for the zhaw (only school of engineering)

## Installation

You can just download/clone and use it.
Some scripts need additional dependencies. See list below.

* syn: lxml, requests
* kw: datetime
* stp: datetime, prettytable, requests, json

## Usage

### syn
For the syn script I parse the output of http://synonyme.woxikon.de/

		syn word
		
Example

		syn gehen
Output
```
	fortgehen
	abgehen
	kündigen
	zurücktreten
	abdanken
	sterben
	abfahren
	aufgeben
	...
```
### kw

use without any arguments

Output

		current calendar week: 9

### stp

Usage: stp [days adding to current date]

Output

```
+-------+-------+---------+--------+
| Start |  End  |  Course |  Room  |
+-------+-------+---------+--------+
| 08:00 | 09:35 | t.MC2-V | TE 407 |
| 12:00 | 13:35 | t.MPC-P | TH 553 |
| 14:00 | 15:35 | t.MPC-V | TH 553 |
+-------+-------+---------+--------+

```

## License

Copyright (C) 2016 Leo Zulfiu

There python scripts are free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

These python scripts are distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

