---
title: "DocRevision Property (IPDMWConfiguration)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConfiguration"
member: "DocRevision"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~DocRevision.html"
---

# DocRevision Property (IPDMWConfiguration)

Gets the revision of the source document for the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property DocRevision As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConfiguration
Dim value As System.String

instance.DocRevision = value

value = instance.DocRevision
```

### C#

```csharp
System.string DocRevision {get; set;}
```

### C++/CLI

```cpp
property System.String^ DocRevision {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Revision of the source document for the configuration

## VBA Syntax

See [PDMWConfiguration::DocRevision](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConfiguration~DocRevision.html).

## See Also

[IPDMWConfiguration Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration.html)
[IPDMWConfiguration Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
