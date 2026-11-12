---
title: "IGetEndPoint2 Method (ISketchEllipse)"
project: "SOLIDWORKS API Help"
interface: "ISketchEllipse"
member: "IGetEndPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~IGetEndPoint2.html"
---

# IGetEndPoint2 Method (ISketchEllipse)

Gets the sketch point for the end point of the ellipse.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEndPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchEllipse
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

See [SketchEllipse::IGetEndPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchEllipse~IGetEndPoint2.html).

## See Also

[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchEllipse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.html)
[ISketchEllipse::GetEndPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetEndPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
