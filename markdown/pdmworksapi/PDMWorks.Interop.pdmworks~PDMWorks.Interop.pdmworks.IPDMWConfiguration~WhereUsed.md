---
title: "WhereUsed Property (IPDMWConfiguration)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConfiguration"
member: "WhereUsed"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~WhereUsed.html"
---

# WhereUsed Property (IPDMWConfiguration)

Gets the links to the documents that reference this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property WhereUsed As PDMWLinks
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConfiguration
Dim value As PDMWLinks

value = instance.WhereUsed
```

### C#

```csharp
PDMWLinks WhereUsed {get;}
```

### C++/CLI

```cpp
property PDMWLinks^ WhereUsed {
   PDMWLinks^ get();
}
```

### Property Value

Collection of [links](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html) of documents that reference this configuration

## VBA Syntax

See [PDMWConfiguration::WhereUsed](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConfiguration~WhereUsed.html).

## See Also

[IPDMWConfiguration Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration.html)
[IPDMWConfiguration Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration_members.html)
[IPDMWLinks Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
