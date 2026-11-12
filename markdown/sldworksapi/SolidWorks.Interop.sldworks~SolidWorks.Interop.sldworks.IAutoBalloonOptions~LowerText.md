---
title: "LowerText Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "LowerText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~LowerText.html"
---

# LowerText Property (IAutoBalloonOptions)

Gets and sets the lower text of the balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property LowerText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
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

See [AutoBalloonOptions::LowerText](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~LowerText.html).

## Remarks

This property is valid only when [IAutoBalloonOptions::Style](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions~Style.html) is set to [swBalloonStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html).swBS_SplitCirc.

You can only get or set the lower text in a BOM balloon using [INote::GetBomBalloonText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonText.html) or [INote::SetBomBalloonText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.html) after [inserting a BOM balloon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.html).

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
