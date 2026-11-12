---
title: "UpperText Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "UpperText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~UpperText.html"
---

# UpperText Property (IAutoBalloonOptions)

Gets and sets the upper text of the balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpperText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
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

See [AutoBalloonOptions::UpperText](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~UpperText.html).

## Remarks

You can only get or set the upper text in a BOM autoballoon using [INote::GetBomBalloonText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonText.html) or [INote::SetBomBalloonText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.html) after [inserting a BOM balloon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.html).

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
