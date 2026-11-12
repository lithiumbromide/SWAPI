---
title: "IGetStartPoint2 Method (ISketchEllipse)"
project: "SOLIDWORKS API Help"
interface: "ISketchEllipse"
member: "IGetStartPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~IGetStartPoint2.html"
---

# IGetStartPoint2 Method (ISketchEllipse)

Gets the sketch point for the start point of the ellipse.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetStartPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchEllipse
Dim value As SketchPoint

value = instance.IGetStartPoint2()
```

### C#

```csharp
SketchPoint IGetStartPoint2()
```

### C++/CLI

```cpp
SketchPoint^ IGetStartPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Start [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchEllipse::IGetStartPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchEllipse~IGetStartPoint2.html).

## See Also

[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchEllipse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.html)
[ISketchEllipse::GetStartPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetStartPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
