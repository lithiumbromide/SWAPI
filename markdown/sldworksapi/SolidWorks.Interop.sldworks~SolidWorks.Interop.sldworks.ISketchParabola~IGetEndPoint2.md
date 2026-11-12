---
title: "IGetEndPoint2 Method (ISketchParabola)"
project: "SOLIDWORKS API Help"
interface: "ISketchParabola"
member: "IGetEndPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~IGetEndPoint2.html"
---

# IGetEndPoint2 Method (ISketchParabola)

Gets the sketch point for the end point of the parabola.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEndPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchParabola
Dim value As SketchPoint

value = instance.IGetEndPoint2()
```

### C#

```csharp
SketchPoint IGetEndPoint2()
```

### C++/CLI

```cpp
SketchPoint^ IGetEndPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

End [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchParabola::IGetEndPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchParabola~IGetEndPoint2.html).

## See Also

[ISketchParabola Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.html)
[ISketchParabola Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola_members.html)
[ISketchParabola::GetEndPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~GetEndPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
