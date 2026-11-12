---
title: "ApplicationName Property (ISwQuickTip)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwQuickTip"
member: "ApplicationName"
kind: "property"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip~ApplicationName.html"
---

# ApplicationName Property (ISwQuickTip)

Gets the name of add-in application.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ApplicationName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwQuickTip
Dim value As System.String

value = instance.ApplicationName
```

### C#

```csharp
System.string ApplicationName {get;}
```

### C++/CLI

```cpp
property System.String^ ApplicationName {
   System.String^ get();
}
```

### Property Value

Name of the add-in

## VBA Syntax

See [SwQuickTip::ApplicationName](ms-its:swpublishedapivb6.chm::/swpublished~SwQuickTip~ApplicationName.html).

## See Also

[ISwQuickTip Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip.html)
[ISwQuickTip Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwQuickTip_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
