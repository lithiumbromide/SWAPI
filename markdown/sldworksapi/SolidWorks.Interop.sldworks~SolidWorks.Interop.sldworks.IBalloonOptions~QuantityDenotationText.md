---
title: "QuantityDenotationText Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "QuantityDenotationText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~QuantityDenotationText.html"
---

# QuantityDenotationText Property (IBalloonOptions)

Gets and sets the label of the BOM item quantity.

## Syntax

### Visual Basic (Declaration)

```vb
Property QuantityDenotationText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
Dim value As System.String

instance.QuantityDenotationText = value

value = instance.QuantityDenotationText
```

### C#

```csharp
System.string QuantityDenotationText {get; set;}
```

### C++/CLI

```cpp
property System.String^ QuantityDenotationText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Item quantity label

## VBA Syntax

See [BalloonOptions::QuantityDenotationText](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~QuantityDenotationText.html).

## Examples

See [IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
