---
title: "IGetStartPoint2 Method (ISketchLine)"
project: "SOLIDWORKS API Help"
interface: "ISketchLine"
member: "IGetStartPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~IGetStartPoint2.html"
---

# IGetStartPoint2 Method (ISketchLine)

Gets the sketch point for the start point of the line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetStartPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchLine
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

Start [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or NULL if operation fails

## VBA Syntax

See [SketchLine::IGetStartPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchLine~IGetStartPoint2.html).

## See Also

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.html)
[ISketchLine::GetStartPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~GetStartPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
