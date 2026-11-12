---
title: "ExtReferences Property (IPDMWConfiguration)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConfiguration"
member: "ExtReferences"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~ExtReferences.html"
---

# ExtReferences Property (IPDMWConfiguration)

Gets the links to external documents referenced by this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ExtReferences As PDMWLinks
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConfiguration
Dim value As PDMWLinks

value = instance.ExtReferences
```

### C#

```csharp
PDMWLinks ExtReferences {get;}
```

### C++/CLI

```cpp
property PDMWLinks^ ExtReferences {
   PDMWLinks^ get();
}
```

### Property Value

Collection of [links](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html) to external documents referenced by this configuration

## VBA Syntax

See [PDMWConfiguration::ExtReferences](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConfiguration~ExtReferences.html).

## Remarks

An external document is any type of derived part, parent or child, including base, mirrored, and component parts.

## See Also

[IPDMWConfiguration Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration.html)
[IPDMWConfiguration Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration_members.html)
[IPDMWLinks Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
