---
title: "IGetFocalPoint2 Method (ISketchParabola)"
project: "SOLIDWORKS API Help"
interface: "ISketchParabola"
member: "IGetFocalPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~IGetFocalPoint2.html"
---

# IGetFocalPoint2 Method (ISketchParabola)

Gets the sketch point for the focal point of the parabola.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFocalPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchParabola
Dim value As SketchPoint

value = instance.IGetFocalPoint2()
```

### C#

```csharp
SketchPoint IGetFocalPoint2()
```

### C++/CLI

```cpp
SketchPoint^ IGetFocalPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Focal [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchParabola::IGetFocalPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchParabola~IGetFocalPoint2.html).

## See Also

[ISketchParabola Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.html)
[ISketchParabola Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola_members.html)
[ISketchParabola::GetFocalPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~GetFocalPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
