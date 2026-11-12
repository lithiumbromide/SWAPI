---
title: "ItemNumberIncrement Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "ItemNumberIncrement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~ItemNumberIncrement.html"
---

# ItemNumberIncrement Property (IBalloonOptions)

Gets and sets the item number increment.

## Syntax

### Visual Basic (Declaration)

```vb
Property ItemNumberIncrement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
Dim value As System.Integer

instance.ItemNumberIncrement = value

value = instance.ItemNumberIncrement
```

### C#

```csharp
System.int ItemNumberIncrement {get; set;}
```

### C++/CLI

```cpp
property System.int ItemNumberIncrement {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Item number increment

## VBA Syntax

See [BalloonOptions::ItemNumberIncrement](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~ItemNumberIncrement.html).

## Examples

See [IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
