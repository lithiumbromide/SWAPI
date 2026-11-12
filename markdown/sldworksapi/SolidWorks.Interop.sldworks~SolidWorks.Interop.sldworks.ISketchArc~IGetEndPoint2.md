---
title: "IGetEndPoint2 Method (ISketchArc)"
project: "SOLIDWORKS API Help"
interface: "ISketchArc"
member: "IGetEndPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~IGetEndPoint2.html"
---

# IGetEndPoint2 Method (ISketchArc)

Gets the sketch point for the end point of the arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEndPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchArc
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

[Sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [SketchArc::IGetEndPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchArc~IGetEndPoint2.html).

## See Also

[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)
[ISketchArc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.html)
[GetEndPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetEndPoint2.html)
[ISketchArc::GetCenterPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetCenterPoint2.html)
[ISketchArc::GetStartPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetStartPoint2.html)
[ISketchArc::IGetCenterPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~IGetCenterPoint2.html)
[ISketchArc::IGetStartPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~IGetStartPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
