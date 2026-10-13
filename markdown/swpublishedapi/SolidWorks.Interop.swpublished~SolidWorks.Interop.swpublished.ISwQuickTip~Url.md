---
title: "Url Property (ISwQuickTip)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwQuickTip"
member: "Url"
kind: "property"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip~Url.html"
---

# Url Property (ISwQuickTip)

Gets the URL of the HMTL page to display in the add-in's Quick Tips.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Url As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwQuickTip
Dim value As System.String

value = instance.Url
```

### C#

```csharp
System.string Url {get;}
```

### C++/CLI

```cpp
property System.String^ Url {
   System.String^ get();
}
```

### Property Value

URL of HTML page

## VBA Syntax

See [SwQuickTip::Url](ms-its:swpublishedapivb6.chm::/swpublished~SwQuickTip~Url.html).

## See Also

[ISwQuickTip Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip.html)
[ISwQuickTip Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
