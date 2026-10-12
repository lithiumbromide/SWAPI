---
title: "ItemNumberStart Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "ItemNumberStart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~ItemNumberStart.html"
---

# ItemNumberStart Property (IStackedBalloonOptions)

Gets and sets the starting item number.

## Syntax

### Visual Basic (Declaration)

```vb
Property ItemNumberStart As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.Integer

instance.ItemNumberStart = value

value = instance.ItemNumberStart
```

### C#

```csharp
System.int ItemNumberStart {get; set;}
```

### C++/CLI

```cpp
property System.int ItemNumberStart {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Starting item number

## VBA Syntax

See [StackedBalloonOptions::ItemNumberStart](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~ItemNumberStart.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
