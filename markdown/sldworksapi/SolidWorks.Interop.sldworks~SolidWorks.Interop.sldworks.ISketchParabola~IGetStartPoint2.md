---
title: "IGetStartPoint2 Method (ISketchParabola)"
project: "SOLIDWORKS API Help"
interface: "ISketchParabola"
member: "IGetStartPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~IGetStartPoint2.html"
---

# IGetStartPoint2 Method (ISketchParabola)

Gets the sketch point for the start point of the parabola.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetStartPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchParabola
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

See [SketchParabola::IGetStartPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchParabola~IGetStartPoint2.html).

## See Also

[ISketchParabola Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.html)
[ISketchParabola Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola_members.html)
[ISketchParabola::GetStartPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~GetStartPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
