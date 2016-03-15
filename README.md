# useful python scripts

I have these python scripts in my PATH variable which I use on a daily basis.

**syn** gives you synonyms to a given word

**kw** gives you the current calendar week

**stp** gives you your timetable for the zhaw (only school of engineering)

**de** translates a german word to english

**en** translates an english word to german

## Installation

You can just download/clone and use it.
Some scripts need additional dependencies. See list below.

* syn: lxml, requests
* kw: datetime
* stp: datetime, prettytable, requests, json
* ed/de: requests

## Usage

### syn
The syn script parses the output from [woxikon.de](http://synonyme.woxikon.de/)

`syn word`
		
Example

`syn gehen`

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

`current calendar week: 9`

### stp

Usage: `stp [days adding to current date]`

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

### ed/de

It uses the API from [Yandex.Translate](https://translate.yandex.com/)

Usage: `ed ENGLISH-WORD`
or
`de GERMAN-WORD`

## License

MIT
