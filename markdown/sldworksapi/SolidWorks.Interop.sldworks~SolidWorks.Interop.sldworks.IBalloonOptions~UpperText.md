---
title: "UpperText Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "UpperText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~UpperText.html"
---

# UpperText Property (IBalloonOptions)

Gets and sets the upper text of the balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpperText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
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

Upper text of the balloon (see **Remarks**)

## VBA Syntax

See [BalloonOptions::UpperText](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~UpperText.html).

## Remarks

You can only get or set the upper text in a BOM balloon using [INote::GetBomBalloonText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonText.html) or [INote::SetBomBalloonText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.html) after [inserting a BOM balloon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.html).

See the SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
