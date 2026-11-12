---
title: "Document Property (IPDMWConfiguration)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConfiguration"
member: "Document"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~Document.html"
---

# Document Property (IPDMWConfiguration)

Gets the document for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Document As PDMWDocument
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConfiguration
Dim value As PDMWDocument

value = instance.Document
```

### C#

```csharp
PDMWDocument Document {get;}
```

### C++/CLI

```cpp
property PDMWDocument^ Document {
   PDMWDocument^ get();
}
```

### Property Value

[Document for this configuration](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)

## VBA Syntax

See [PDMWConfiguration::Document](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConfiguration~Document.html).

## See Also

[IPDMWConfiguration Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration.html)
[IPDMWConfiguration Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration_members.html)
[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
