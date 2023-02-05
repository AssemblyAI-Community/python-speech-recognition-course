
## Dependencies

```console
$ pip install pyaudio
```
Incase you come across an error installing pyaudio on windows using pip, try this below:

```console
$ pip install pipwin
$ pipwin install pyaudio
```


M1 Mac:

```console
$ python -m pip install --global-option='build_ext' --global-option='-I/opt/homebrew/Cellar/portaudio/19.7.0/include' --global-option='-L/opt/homebrew/Cellar/portaudio/19.7.0/lib' pyaudio
```
