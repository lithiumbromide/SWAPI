---
title: "MenuName Property (ISwQuickTip)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwQuickTip"
member: "MenuName"
kind: "property"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip~MenuName.html"
---

# MenuName Property (ISwQuickTip)

Gets the name of add-in's Quick Tips on the SOLIDWORKS Help menu.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MenuName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwQuickTip
Dim value As System.String

value = instance.MenuName
```

### C#

```csharp
System.string MenuName {get;}
```

### C++/CLI

```cpp
property System.String^ MenuName {
   System.String^ get();
}
```

### Property Value

Name of add-in's Quick Tips on the SOLIDWORKS Help menu

## VBA Syntax

See [SwQuickTip::MenuName](ms-its:swpublishedapivb6.chm::/swpublished~SwQuickTip~MenuName.html).

## See Also

[ISwQuickTip Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip.html)
[ISwQuickTip Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
