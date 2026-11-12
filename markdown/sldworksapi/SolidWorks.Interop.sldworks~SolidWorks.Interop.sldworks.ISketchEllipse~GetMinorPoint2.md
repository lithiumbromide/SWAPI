---
title: "GetMinorPoint2 Method (ISketchEllipse)"
project: "SOLIDWORKS API Help"
interface: "ISketchEllipse"
member: "GetMinorPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetMinorPoint2.html"
---

# GetMinorPoint2 Method (ISketchEllipse)

Gets the sketch point for the minor point of the ellipse.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinorPoint2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchEllipse
Dim value As System.Object

value = instance.GetMinorPoint2()
```

### C#

```csharp
System.object GetMinorPoint2()
```

### C++/CLI

```cpp
System.Object^ GetMinorPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Minor [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchEllipse::GetMinorPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchEllipse~GetMinorPoint2.html).

## Examples

See the [ISketchEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html) examples.

## See Also

[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchEllipse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.html)
[ISketchEllipse::IGetMinorPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~IGetMinorPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
