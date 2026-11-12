---
title: "ItemNumberIncrement Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "ItemNumberIncrement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~ItemNumberIncrement.html"
---

# ItemNumberIncrement Property (IStackedBalloonOptions)

Gets and sets the item number increment.

## Syntax

### Visual Basic (Declaration)

```vb
Property ItemNumberIncrement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
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

See [StackedBalloonOptions::ItemNumberIncrement](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~ItemNumberIncrement.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
