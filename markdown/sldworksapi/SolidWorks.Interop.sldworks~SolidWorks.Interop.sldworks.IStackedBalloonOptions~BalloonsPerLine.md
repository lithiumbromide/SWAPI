---
title: "BalloonsPerLine Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "BalloonsPerLine"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~BalloonsPerLine.html"
---

# BalloonsPerLine Property (IStackedBalloonOptions)

Gets and sets the number of stacked balloons per line.

## Syntax

### Visual Basic (Declaration)

```vb
Property BalloonsPerLine As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.Integer

instance.BalloonsPerLine = value

value = instance.BalloonsPerLine
```

### C#

```csharp
System.int BalloonsPerLine {get; set;}
```

### C++/CLI

```cpp
property System.int BalloonsPerLine {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of balloons per line; specify a number >= 2

## VBA Syntax

See [StackedBalloonOptions::BalloonsPerLine](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~BalloonsPerLine.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
