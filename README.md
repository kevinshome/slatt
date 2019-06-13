# The Slatt Esoteric Programming Language
#### (devel branch - used for non-binary/development releases)

[![codebeat badge](https://codebeat.co/badges/f5365231-19d4-4825-aeb9-bfe72f30a543)](https://codebeat.co/projects/github-com-kevinshome-slatt-master)

* Slatt is an esoteric programming language based on the way rapper, "Playboi Carti", writes tweets.

* Examples:

    * https://twitter.com/playboicarti/status/994731849690869761

    * https://twitter.com/playboicarti/status/991715100854714368

    * https://twitter.com/playboicarti/status/1006241861579804672

* The latest release of Slatt is Development Release 004:

(In order to use the Slatt Development Releases, you must have >= Python 3.5 installed)

* Features in this release:

    - if/else statements!

    - user input!

    - examples of these can be found in "examples/if_else.slatt"

    - (i also did a bit of a rewrite because this code was a fucking mess, still is, but now less)


* How to use the latest Slatt Development Release:

    - Clone this git repository.

    ```
      git clone https://github.com/kevinshome/slatt.git
    ```

    - Run Slatt module through Python.

    ```
      python3 -m slatt {SLATT_FILE}.slatt
    ```

    - Program will then be built and run by the Slatt compiler.


* "Hello, world!" example:

```
    1 **slatt!** # this is reqired at the top of every slatt file
    2
    3 +yo pierre("Hello, world!") # outputs "Hello, world!" in console
    4
    5 ok! # this is required at the bottom of every slatt file
```

    (This example can be run with "python3 -m slatt slatt/examples/hello.slatt")
