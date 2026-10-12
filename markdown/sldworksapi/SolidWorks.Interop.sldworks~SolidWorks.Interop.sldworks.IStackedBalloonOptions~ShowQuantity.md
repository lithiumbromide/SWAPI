---
title: "ShowQuantity Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "ShowQuantity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~ShowQuantity.html"
---

# ShowQuantity Property (IStackedBalloonOptions)

Gets and sets whether to display the BOM item quantities.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowQuantity As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
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

True to show BOM item quantities, false to not

## VBA Syntax

See [StackedBalloonOptions::ShowQuantity](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~ShowQuantity.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
