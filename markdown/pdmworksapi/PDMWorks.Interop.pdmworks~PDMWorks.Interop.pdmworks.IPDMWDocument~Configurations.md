---
title: "Configurations Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "Configurations"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Configurations.html"
---

# Configurations Property (IPDMWDocument)

Gets the configurations available for the specified document and revision.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Configurations As PDMWConfigurations
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As PDMWConfigurations

value = instance.Configurations
```

### C#

```csharp
PDMWConfigurations Configurations {get;}
```

### C++/CLI

```cpp
property PDMWConfigurations^ Configurations {
   PDMWConfigurations^ get();
}
```

### Property Value

Collection of [configurations](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfigurations.html)

## VBA Syntax

See [PDMWDocument::Configurations](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~Configurations.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
