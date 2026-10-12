---
title: "ItemNumberStart Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "ItemNumberStart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~ItemNumberStart.html"
---

# ItemNumberStart Property (IBalloonOptions)

Gets and sets the starting item number.

## Syntax

### Visual Basic (Declaration)

```vb
Property ItemNumberStart As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
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

See [BalloonOptions::ItemNumberStart](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~ItemNumberStart.html).

## Examples

See [IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
