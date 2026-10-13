---
title: "References Property (IPDMWConfiguration)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConfiguration"
member: "References"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~References.html"
---

# References Property (IPDMWConfiguration)

Gets the links to documents referenced by this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property References As PDMWLinks
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConfiguration
Dim value As PDMWLinks

value = instance.References
```

### C#

```csharp
PDMWLinks References {get;}
```

### C++/CLI

```cpp
property PDMWLinks^ References {
   PDMWLinks^ get();
}
```

### Property Value

Collection of [links](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html) to documents referenced by this configuration

## VBA Syntax

See [PDMWConfiguration::References](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConfiguration~References.html).

## See Also

[IPDMWConfiguration Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration.html)
[IPDMWConfiguration Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration_members.html)
[IPDMWLinks Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
