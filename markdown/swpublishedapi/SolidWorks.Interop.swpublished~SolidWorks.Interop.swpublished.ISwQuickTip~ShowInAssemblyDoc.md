---
title: "ShowInAssemblyDoc Property (ISwQuickTip)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwQuickTip"
member: "ShowInAssemblyDoc"
kind: "property"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip~ShowInAssemblyDoc.html"
---

# ShowInAssemblyDoc Property (ISwQuickTip)

Gets whether to show an add-in's Quick Tips in SOLIDWORKS assembly documents.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ShowInAssemblyDoc As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwQuickTip
Dim value As System.Boolean

value = instance.ShowInAssemblyDoc
```

### C#

```csharp
System.bool ShowInAssemblyDoc {get;}
```

### C++/CLI

```cpp
property System.bool ShowInAssemblyDoc {
   System.bool get();
}
```

### Property Value

True to show Quick Tips in SOLIDWORKS assembly documents, false to not

## VBA Syntax

See [SwQuickTip::ShowInAssemblyDoc](ms-its:swpublishedapivb6.chm::/swpublished~SwQuickTip~ShowInAssemblyDoc.html).

## See Also

[ISwQuickTip Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip.html)
[ISwQuickTip Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
