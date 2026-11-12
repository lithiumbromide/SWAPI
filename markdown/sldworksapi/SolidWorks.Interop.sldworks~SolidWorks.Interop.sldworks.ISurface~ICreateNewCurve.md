---
title: "ICreateNewCurve Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "ICreateNewCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateNewCurve.html"
---

# ICreateNewCurve Method (ISurface)

Creates a new empty curve for the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateNewCurve() As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As Curve

value = instance.ICreateNewCurve()
```

### C#

```csharp
Curve ICreateNewCurve()
```

### C++/CLI

```cpp
Curve^ ICreateNewCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Newly created [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Surface::ICreateNewCurve](ms-its:sldworksapivb6.chm::/sldworks~Surface~ICreateNewCurve.html).

## Remarks

The intention is that with a handle on such (initially empty) curves, appropriate construction can be called that eventually amounts to non-trivial objects.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::CreateNewCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateNewCurve.html)
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.html)
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.html)
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.html)
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.html)
[ICurve::CreateTrimmedCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.html)
