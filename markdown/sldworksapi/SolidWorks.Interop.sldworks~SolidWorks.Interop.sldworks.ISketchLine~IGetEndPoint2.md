---
title: "IGetEndPoint2 Method (ISketchLine)"
project: "SOLIDWORKS API Help"
interface: "ISketchLine"
member: "IGetEndPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~IGetEndPoint2.html"
---

# IGetEndPoint2 Method (ISketchLine)

Gets the sketch point for the end point of the line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEndPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchLine
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

End [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or NULL if the operation fails

## VBA Syntax

See [SketchLine::IGetEndPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchLine~IGetEndPoint2.html).

## See Also

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.html)
[ISketchLine::GetEndPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~GetEndPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
