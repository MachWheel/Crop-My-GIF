```{toctree}
:caption: 'Getting started'
:maxdepth: 3

usage
installation
cloning
compiling
```



```{toctree}
:caption: 'Startup modules'
:maxdepth: 1

startup
main
```


```{note}
Application startup behavior and entry-point.
```



```{toctree}
:caption: 'Model'
:maxdepth: 1

model.GifInfo
model.Selection
model.units
```


```{tip}
Data structures used by appliction.
```



```{toctree}
:caption: 'Main Controllers'
:maxdepth: 1

controllers.App
controllers.Gifbrowser
```


```{hint}
Listens and controls application events.
```


```{toctree}
:caption: 'Windows and Popups'
:maxdepth: 2

views
```

```{note}
Those are called in {doc}`controllers.App` and {doc}`controllers.Gifbrowser`
```


```{toctree}
:caption: 'UI Elements'
:maxdepth: 3

views._ui
```


```{attention}
**views._ui** functions should be called within {doc}`views`
```


```{toctree}
:caption: 'UI Controllers'
:maxdepth: 1

controllers._ui.Animation
controllers._ui.Display
controllers._ui.CropGUI
```

```{caution}
**controllers._ui** modules should be called within {doc}`controllers.App`
```

```{toctree}
:caption: 'GIF Controllers'
:maxdepth: 1

controllers._gif.Cropper
controllers._gif.Frames
```

```{warning}
**controllers._gif** modules should be called within {doc}`controllers.App`
```
