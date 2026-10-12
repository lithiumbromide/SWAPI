---
title: "ItemNumberStart Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "ItemNumberStart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~ItemNumberStart.html"
---

# ItemNumberStart Property (IAutoBalloonOptions)

Gets and sets the starting item number.

## Syntax

### Visual Basic (Declaration)

```vb
Property ItemNumberStart As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
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

See [AutoBalloonOptions::ItemNumberStart](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~ItemNumberStart.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
