---
title: "ShowInPartDoc Property (ISwQuickTip)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwQuickTip"
member: "ShowInPartDoc"
kind: "property"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip~ShowInPartDoc.html"
---

# ShowInPartDoc Property (ISwQuickTip)

Gets whether to show the add-in's Quick Tips in SOLIDWORKS part documents.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ShowInPartDoc As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwQuickTip
Dim value As System.Boolean

value = instance.ShowInPartDoc
```

### C#

```csharp
System.bool ShowInPartDoc {get;}
```

### C++/CLI

```cpp
property System.bool ShowInPartDoc {
   System.bool get();
}
```

### Property Value

True to show Quick Tips in SOLIDWORKS part documents, false to not

## VBA Syntax

See [SwQuickTip::ShowInPartDoc](ms-its:swpublishedapivb6.chm::/swpublished~SwQuickTip~ShowInPartDoc.html).

## See Also

[ISwQuickTip Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip.html)
[ISwQuickTip Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
