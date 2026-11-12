---
title: "ShowQuantity Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "ShowQuantity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~ShowQuantity.html"
---

# ShowQuantity Property (IBalloonOptions)

Gets and sets whether to display the BOM item quantity.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowQuantity As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
Dim value As System.Boolean

instance.ShowQuantity = value

value = instance.ShowQuantity
```

### C#

```csharp
System.bool ShowQuantity {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowQuantity {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show the BOM item quantity, false to not

## VBA Syntax

See [BalloonOptions::ShowQuantity](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~ShowQuantity.html).

## Examples

See [IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
