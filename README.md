# Open BOBJ

Simple Python Package to open `.obj` files in Blender
from the command line.
It clears the whole scene from any default objects and
you are left with the `.obj` files you specified.

## Prerequisites

The script expects the command `blender` to point at
your blender executable. You can test if this is the case
by running

```
blender
```

and if everything goes right, then Blender will open and you
can continue with the installation process.

In case you get an error saying something like

```
blender: command not found
```

then you either haven't installed Blender, or your don't
have a shortcut to your blender executable. If the latter is
the case, then you can export the blender PATH

```
export PATH="/path/to/your/blender/blender-3.3.0:$PATH"
```

If this still doesn't fix your problem, then you could also
create a [`bash_alias`](https://linuxize.com/post/how-to-create-bash-aliases/).

## Install

You can simply install it using

```
pip install open-bobj
```

or if you have `pipx` use

```
pipx install open-bobj
```

## Usage

To open any number of `.obj` files in the terminal, run

```
open-bobj /path/to/file.obj
```

You can also open multiple at ones. This is going to open all
of the `.obj` objects in the same blender instance.

```
open-bobj /path/to/file.obj /another/file.obj /and/another/one.obj
```

There is also a short handle

```
bobj /path/to/file.obj
```
