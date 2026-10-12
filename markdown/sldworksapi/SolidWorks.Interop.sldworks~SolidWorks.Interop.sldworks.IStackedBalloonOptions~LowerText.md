---
title: "LowerText Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "LowerText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~LowerText.html"
---

# LowerText Property (IStackedBalloonOptions)

Gets and sets the lower text of the balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property LowerText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.String

instance.LowerText = value

value = instance.LowerText
```

### C#

```csharp
System.string LowerText {get; set;}
```

### C++/CLI

```cpp
property System.String^ LowerText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Lower text of the balloons (see **Remarks**)

## VBA Syntax

See [StackedBalloonOptions::LowerText](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~LowerText.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

This property is valid only when [IStackedBalloonOptions::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions~Style.html) is set to [swBalloonStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html).swBS_SplitCirc. See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
