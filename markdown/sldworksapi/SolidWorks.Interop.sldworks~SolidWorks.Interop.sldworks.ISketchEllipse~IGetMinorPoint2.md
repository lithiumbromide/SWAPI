---
title: "IGetMinorPoint2 Method (ISketchEllipse)"
project: "SOLIDWORKS API Help"
interface: "ISketchEllipse"
member: "IGetMinorPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~IGetMinorPoint2.html"
---

# IGetMinorPoint2 Method (ISketchEllipse)

Gets the sketch point for the minor point of the ellipse.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMinorPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchEllipse
Dim value As SketchPoint

value = instance.IGetMinorPoint2()
```

### C#

```csharp
SketchPoint IGetMinorPoint2()
```

### C++/CLI

```cpp
SketchPoint^ IGetMinorPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Minor [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchEllipse::IGetMinorPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchEllipse~IGetMinorPoint2.html).

## See Also

[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchEllipse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.html)
[ISketchEllipse::GetMinorPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetMinorPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
