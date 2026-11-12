---
title: "GetCenterPoint2 Method (ISketchEllipse)"
project: "SOLIDWORKS API Help"
interface: "ISketchEllipse"
member: "GetCenterPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetCenterPoint2.html"
---

# GetCenterPoint2 Method (ISketchEllipse)

Gets the sketch point for the center point of the ellipse.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCenterPoint2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchEllipse
Dim value As System.Object

value = instance.GetCenterPoint2()
```

### C#

```csharp
System.object GetCenterPoint2()
```

### C++/CLI

```cpp
System.Object^ GetCenterPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Center [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchEllipse::GetCenterPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchEllipse~GetCenterPoint2.html).

## Examples

See the [ISketchEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html) examples.

## See Also

[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchEllipse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.html)
[ISketchEllipse::IGetCenterPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~IGetCenterPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
