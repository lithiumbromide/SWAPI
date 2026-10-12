---
title: "HideGuide Property (ISwQuickTip)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwQuickTip"
member: "HideGuide"
kind: "property"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip~HideGuide.html"
---

# HideGuide Property (ISwQuickTip)

Gets the state of the add-in's Quick Tips.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HideGuide As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwQuickTip
Dim value As System.Boolean

value = instance.HideGuide
```

### C#

```csharp
System.bool HideGuide {get;}
```

### C++/CLI

```cpp
property System.bool HideGuide {
   System.bool get();
}
```

### Property Value

True if add-in's Quick Tips is hidden, false if it is shown

## VBA Syntax

See [SwQuickTip::HideGuide](ms-its:swpublishedapivb6.chm::/swpublished~SwQuickTip~HideGuide.html).

## See Also

[ISwQuickTip Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip.html)
[ISwQuickTip Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
