---
title: "SetRadius Method (ISketchArc)"
project: "SOLIDWORKS API Help"
interface: "ISketchArc"
member: "SetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~SetRadius.html"
---

# SetRadius Method (ISketchArc)

Sets the radius of the arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRadius( _
   ByVal Radius As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchArc
Dim Radius As System.Double
Dim value As System.Boolean

value = instance.SetRadius(Radius)
```

### C#

```csharp
System.bool SetRadius(
   System.double Radius
)
```

### C++/CLI

```cpp
System.bool SetRadius(
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Radius`: Radius in meters of the arc

### Return Value

True if successful, false if not

## VBA Syntax

See [SketchArc::SetRadius](ms-its:sldworksapivb6.chm::/sldworks~SketchArc~SetRadius.html).

## See Also

[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.html)
[ISketchArc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.html)
[ISketchArc::GetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetRadius.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
