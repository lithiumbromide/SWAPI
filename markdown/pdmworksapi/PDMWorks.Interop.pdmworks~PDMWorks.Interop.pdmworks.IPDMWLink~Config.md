---
title: "Config Property (IPDMWLink)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWLink"
member: "Config"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink~Config.html"
---

# Config Property (IPDMWLink)

Gets the name of the configuration for this link.

## Syntax

### Visual Basic (Declaration)

```vb
Property Config As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWLink
Dim value As System.String

instance.Config = value

value = instance.Config
```

### C#

```csharp
System.string Config {get; set;}
```

### C++/CLI

```cpp
property System.String^ Config {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the configuration for this link

## VBA Syntax

See [PDMWLink::Config](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWLink~Config.html).

## Remarks

If the source object is an [IPDMWDocument](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html) object, then the name of the configuration is not available.

## See Also

[IPDMWLink Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink.html)
[IPDMWLink Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLink_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
