---
title: "project Property (IPDMWSearchResult)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchResult"
member: "project"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult~project.html"
---

# project Property (IPDMWSearchResult)

Gets the name of the project in the search results.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property project As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchResult
Dim value As System.String

value = instance.project
```

### C#

```csharp
System.string project {get;}
```

### C++/CLI

```cpp
property System.String^ project {
   System.String^ get();
}
```

### Property Value

Name of project

## VBA Syntax

See [PDMWSearchResult::project](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchResult~project.html).

## See Also

[IPDMWSearchResult Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult.html)
[IPDMWSearchResult Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchResult_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
