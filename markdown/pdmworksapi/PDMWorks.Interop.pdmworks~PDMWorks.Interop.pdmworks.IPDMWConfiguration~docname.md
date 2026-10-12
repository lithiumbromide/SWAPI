---
title: "docname Property (IPDMWConfiguration)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConfiguration"
member: "docname"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~docname.html"
---

# docname Property (IPDMWConfiguration)

Gets the name of the source document for the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property docname As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConfiguration
Dim value As System.String

instance.docname = value

value = instance.docname
```

### C#

```csharp
System.string docname {get; set;}
```

### C++/CLI

```cpp
property System.String^ docname {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the source document

## VBA Syntax

See [PDMWConfiguration::docname](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConfiguration~docname.html).

## See Also

[IPDMWConfiguration Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration.html)
[IPDMWConfiguration Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
