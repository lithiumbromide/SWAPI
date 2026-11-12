---
title: "IGetCenterPoint2 Method (ISketchEllipse)"
project: "SOLIDWORKS API Help"
interface: "ISketchEllipse"
member: "IGetCenterPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~IGetCenterPoint2.html"
---

# IGetCenterPoint2 Method (ISketchEllipse)

Gets the sketch point for the center point of the ellipse.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCenterPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchEllipse
Dim value As SketchPoint

value = instance.IGetCenterPoint2()
```

### C#

```csharp
SketchPoint IGetCenterPoint2()
```

### C++/CLI

```cpp
SketchPoint^ IGetCenterPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Center [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchEllipse::IGetCenterPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchEllipse~IGetCenterPoint2.html).

## See Also

[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchEllipse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.html)
[ISketchEllipse::GetCenterPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetCenterPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
