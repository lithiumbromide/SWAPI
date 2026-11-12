---
title: "IGetMajorPoint2 Method (ISketchEllipse)"
project: "SOLIDWORKS API Help"
interface: "ISketchEllipse"
member: "IGetMajorPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~IGetMajorPoint2.html"
---

# IGetMajorPoint2 Method (ISketchEllipse)

Gets the sketch point for the major point of the ellipse.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMajorPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchEllipse
Dim value As SketchPoint

value = instance.IGetMajorPoint2()
```

### C#

```csharp
SketchPoint IGetMajorPoint2()
```

### C++/CLI

```cpp
SketchPoint^ IGetMajorPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Major [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchEllipse::IGetMajorPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchEllipse~IGetMajorPoint2.html).

## See Also

[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchEllipse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.html)
[ISketchEllipse::GetMajorPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetMajorPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
