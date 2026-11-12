---
title: "PerimeterCircle Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "PerimeterCircle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~PerimeterCircle.html"
---

# PerimeterCircle Method (ISketchManager)

Draws a 3-point perimeter arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function PerimeterCircle( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal X3 As System.Double, _
   ByVal Y3 As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim X1 As System.Double
Dim Y1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim X3 As System.Double
Dim Y3 As System.Double
Dim value As System.Object

value = instance.PerimeterCircle(X1, Y1, X2, Y2, X3, Y3)
```

### C#

```csharp
System.object PerimeterCircle(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double X3,
   System.double Y3
)
```

### C++/CLI

```cpp
System.Object^ PerimeterCircle(
   System.double X1,
   System.double Y1,
   System.double X2,
   System.double Y2,
   System.double X3,
   System.double Y3
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X1`: coordinate for first point
- `Y1`: y coordinate for first point
- `X2`: x coordinate for second point
- `Y2`: y coordinate for second point
- `X3`: x coordinate for third point
- `Y3`: y coordinate for third point

### Return Value

[3-point perimeter arc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc.html)

## VBA Syntax

See [SketchManager::PerimeterCircle](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~PerimeterCircle.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
