---
title: "ItemNumberIncrement Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "ItemNumberIncrement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~ItemNumberIncrement.html"
---

# ItemNumberIncrement Property (IAutoBalloonOptions)

Gets and sets the item number increment.

## Syntax

### Visual Basic (Declaration)

```vb
Property ItemNumberIncrement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
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

See [AutoBalloonOptions::ItemNumberIncrement](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~ItemNumberIncrement.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
