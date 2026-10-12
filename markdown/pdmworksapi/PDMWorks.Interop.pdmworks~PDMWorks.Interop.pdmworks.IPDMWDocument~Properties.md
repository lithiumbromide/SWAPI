---
title: "Properties Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "Properties"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Properties.html"
---

# Properties Property (IPDMWDocument)

Gets the properties of this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Properties As PDMWProperties
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
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

Collection of [properties](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties.html)

## VBA Syntax

See [PDMWDocument::Properties](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~Properties.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::Description Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Description.html)
[IPDMWDocument::Number Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Number.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
