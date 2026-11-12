---
title: "IGetApexPoint2 Method (ISketchParabola)"
project: "SOLIDWORKS API Help"
interface: "ISketchParabola"
member: "IGetApexPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~IGetApexPoint2.html"
---

# IGetApexPoint2 Method (ISketchParabola)

Gets the sketch point for the apex point of the parabola.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetApexPoint2() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchParabola
Dim value As SketchPoint

value = instance.IGetApexPoint2()
```

### C#

```csharp
SketchPoint IGetApexPoint2()
```

### C++/CLI

```cpp
SketchPoint^ IGetApexPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Apex [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or null if the operation fails

## VBA Syntax

See [SketchParabola::IGetApexPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchParabola~IGetApexPoint2.html).

## See Also

[ISketchParabola Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.html)
[ISketchParabola Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola_members.html)
[ISketchParabola::GetApexPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~GetApexPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
