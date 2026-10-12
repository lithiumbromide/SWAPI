---
title: "QuantityOverrideValue Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "QuantityOverrideValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~QuantityOverrideValue.html"
---

# QuantityOverrideValue Property (IBalloonOptions)

Gets and sets the override value for the BOM item quantity.

## Syntax

### Visual Basic (Declaration)

```vb
Property QuantityOverrideValue As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
Dim value As System.String

instance.QuantityOverrideValue = value

value = instance.QuantityOverrideValue
```

### C#

```csharp
System.string QuantityOverrideValue {get; set;}
```

### C++/CLI

```cpp
property System.String^ QuantityOverrideValue {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

BOM item quantity override value; valid only when [IBalloonOptions::QuantityOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions~QuantityOverride.html) is true

## VBA Syntax

See [BalloonOptions::QuantityOverrideValue](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~QuantityOverrideValue.html).

## Examples

See [IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
