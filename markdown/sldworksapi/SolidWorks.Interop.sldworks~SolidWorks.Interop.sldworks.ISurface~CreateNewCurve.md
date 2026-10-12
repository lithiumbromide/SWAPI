---
title: "CreateNewCurve Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "CreateNewCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateNewCurve.html"
---

# CreateNewCurve Method (ISurface)

Creates a new empty curve for the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateNewCurve() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Object

value = instance.CreateNewCurve()
```

### C#

```csharp
System.object CreateNewCurve()
```

### C++/CLI

```cpp
System.Object^ CreateNewCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Newly created [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Surface::CreateNewCurve](ms-its:sldworksapivb6.chm::/sldworks~Surface~CreateNewCurve.html).

## Remarks

The intention is that with a handle on such (initially empty) curves, appropriate construction can be called that eventually amounts to non-trivial objects.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::ICreateNewCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateNewCurve.html)
[ISurface::MakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurve.html)
[ISurface::MakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~MakeIsoCurves.html)
[ISurface::IMakeIsoCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurve.html)
[ISurface::IMakeIsoCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IMakeIsoCurves.html)
[ICurve::CreateTrimmedCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.html)
