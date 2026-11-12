---
title: "ShowInDrawingDoc Property (ISwQuickTip)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwQuickTip"
member: "ShowInDrawingDoc"
kind: "property"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip~ShowInDrawingDoc.html"
---

# ShowInDrawingDoc Property (ISwQuickTip)

Gets whether to show an add-in's Quick Tips in SOLIDWORKS drawing documents.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ShowInDrawingDoc As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwQuickTip
Dim value As System.Boolean

value = instance.ShowInDrawingDoc
```

### C#

```csharp
System.bool ShowInDrawingDoc {get;}
```

### C++/CLI

```cpp
property System.bool ShowInDrawingDoc {
   System.bool get();
}
```

### Property Value

True to show Quick Tips in SOLIDWORKS drawing documents, false to not

## VBA Syntax

See [SwQuickTip::ShowInDrawingDoc](ms-its:swpublishedapivb6.chm::/swpublished~SwQuickTip~ShowInDrawingDoc.html).

## See Also

[ISwQuickTip Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip.html)
[ISwQuickTip Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
