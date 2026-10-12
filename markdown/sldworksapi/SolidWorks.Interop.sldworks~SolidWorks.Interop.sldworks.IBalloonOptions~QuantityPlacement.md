---
title: "QuantityPlacement Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "QuantityPlacement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~QuantityPlacement.html"
---

# QuantityPlacement Property (IBalloonOptions)

Gets and sets the placement of the BOM item quantity with respect to its balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property QuantityPlacement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
Dim value As System.Integer

instance.QuantityPlacement = value

value = instance.QuantityPlacement
```

### C#

```csharp
System.int QuantityPlacement {get; set;}
```

### C++/CLI

```cpp
property System.int QuantityPlacement {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Placement of the BOM item quantity as defined in [swBalloonQuantityPlacement_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonQuantityPlacement_e.html)

## VBA Syntax

See [BalloonOptions::QuantityPlacement](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~QuantityPlacement.html).

## Examples

See [IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
