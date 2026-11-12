---
title: "QuantityOverride Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "QuantityOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~QuantityOverride.html"
---

# QuantityOverride Property (IBalloonOptions)

Gets and sets whether to override the BOM item quantity.

## Syntax

### Visual Basic (Declaration)

```vb
Property QuantityOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
Dim value As System.Boolean

instance.QuantityOverride = value

value = instance.QuantityOverride
```

### C#

```csharp
System.bool QuantityOverride {get; set;}
```

### C++/CLI

```cpp
property System.bool QuantityOverride {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the BOM item quantity, false to not

## VBA Syntax

See [BalloonOptions::QuantityOverride](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~QuantityOverride.html).

## Examples

See [IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
