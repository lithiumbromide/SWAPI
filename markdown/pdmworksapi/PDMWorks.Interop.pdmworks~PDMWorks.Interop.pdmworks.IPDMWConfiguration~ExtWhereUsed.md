---
title: "ExtWhereUsed Property (IPDMWConfiguration)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConfiguration"
member: "ExtWhereUsed"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~ExtWhereUsed.html"
---

# ExtWhereUsed Property (IPDMWConfiguration)

Gets the links to external documents that reference this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ExtWhereUsed As PDMWLinks
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConfiguration
Dim value As PDMWLinks

value = instance.ExtWhereUsed
```

### C#

```csharp
PDMWLinks ExtWhereUsed {get;}
```

### C++/CLI

```cpp
property PDMWLinks^ ExtWhereUsed {
   PDMWLinks^ get();
}
```

### Property Value

Collection of [links](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html) to external documents that reference this configuration

## VBA Syntax

See [PDMWConfiguration::ExtWhereUsed](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConfiguration~ExtWhereUsed.html).

## Remarks

An external document is any type of derived part, parent or child, including base, mirrored, and component parts.

## See Also

[IPDMWConfiguration Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration.html)
[IPDMWConfiguration Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration_members.html)
[IPDMWLinks Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
