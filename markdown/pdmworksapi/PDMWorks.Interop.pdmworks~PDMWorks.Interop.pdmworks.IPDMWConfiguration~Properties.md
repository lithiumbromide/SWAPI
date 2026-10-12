---
title: "Properties Property (IPDMWConfiguration)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConfiguration"
member: "Properties"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~Properties.html"
---

# Properties Property (IPDMWConfiguration)

Gets the properties for the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Properties As PDMWProperties
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConfiguration
Dim value As PDMWProperties

value = instance.Properties
```

### C#

```csharp
PDMWProperties Properties {get;}
```

### C++/CLI

```cpp
property PDMWProperties^ Properties {
   PDMWProperties^ get();
}
```

### Property Value

Collection of [properties](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties.html) for the configuration

## VBA Syntax

See [PDMWConfiguration::Properties](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConfiguration~Properties.html).

## See Also

[IPDMWConfiguration Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration.html)
[IPDMWConfiguration Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration_members.html)
[IPDMWProperties Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
