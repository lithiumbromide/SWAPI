---
title: "GetEndPoint2 Method (ISketchEllipse)"
project: "SOLIDWORKS API Help"
interface: "ISketchEllipse"
member: "GetEndPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~GetEndPoint2.html"
---

# GetEndPoint2 Method (ISketchEllipse)

Gets the sketch point for the end point of the ellipse.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndPoint2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchEllipse
Dim value As System.Object

value = instance.GetEndPoint2()
```

### C#

```csharp
System.object GetEndPoint2()
```

### C++/CLI

```cpp
System.Object^ GetEndPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

End [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchEllipse::GetEndPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchEllipse~GetEndPoint2.html).

## Examples

See the [ISketchEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html) examples.

## See Also

[ISketchEllipse Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.html)
[ISketchEllipse Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.html)
[ISketchEllipse::IGetEndPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse~IGetEndPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
