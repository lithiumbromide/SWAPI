---
title: "UpperText Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "UpperText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~UpperText.html"
---

# UpperText Property (IStackedBalloonOptions)

Gets and sets the upper text of the balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpperText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.String

instance.UpperText = value

value = instance.UpperText
```

### C#

```csharp
System.string UpperText {get; set;}
```

### C++/CLI

```cpp
property System.String^ UpperText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Upper text of the balloons

## VBA Syntax

See [StackedBalloonOptions::UpperText](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~UpperText.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
