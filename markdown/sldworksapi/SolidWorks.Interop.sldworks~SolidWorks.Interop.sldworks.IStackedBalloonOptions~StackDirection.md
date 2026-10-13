---
title: "StackDirection Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "StackDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~StackDirection.html"
---

# StackDirection Property (IStackedBalloonOptions)

Gets and sets the direction in which to stack balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property StackDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.Integer

instance.StackDirection = value

value = instance.StackDirection
```

### C#

```csharp
System.int StackDirection {get; set;}
```

### C++/CLI

```cpp
property System.int StackDirection {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Stack direction as defined in [swStackedBalloonDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStackedBalloonDirection_e.html)

## VBA Syntax

See [StackedBalloonOptions::StackDirection](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~StackDirection.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
