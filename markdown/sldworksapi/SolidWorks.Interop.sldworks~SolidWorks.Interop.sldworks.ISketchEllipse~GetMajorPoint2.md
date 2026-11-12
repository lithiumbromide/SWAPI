---
title: "GetMajorPoint2 Method (ISketchEllipse)"
project: "SOLIDWORKS API Help"
interface: "ISketchEllipse"
member: "GetMajorPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetMajorPoint2.html"
---

# GetMajorPoint2 Method (ISketchEllipse)

Gets the sketch point for the major point of the ellipse.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMajorPoint2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchEllipse
Dim value As System.Object

value = instance.GetMajorPoint2()
```

### C#

```csharp
System.object GetMajorPoint2()
```

### C++/CLI

```cpp
System.Object^ GetMajorPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Major [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchEllipse::GetMajorPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchEllipse~GetMajorPoint2.html).

## Examples

See the [ISketchEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html) examples.

## See Also

[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchEllipse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.html)
[ISketchEllipse::IGetMajorPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~IGetMajorPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
