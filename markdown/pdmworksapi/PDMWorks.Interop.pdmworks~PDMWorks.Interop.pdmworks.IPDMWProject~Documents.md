---
title: "Documents Property (IPDMWProject)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProject"
member: "Documents"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~Documents.html"
---

# Documents Property (IPDMWProject)

Gets the documents for this project.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Documents As PDMWDocuments
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProject
Dim value As PDMWDocuments

value = instance.Documents
```

### C#

```csharp
PDMWDocuments Documents {get;}
```

### C++/CLI

```cpp
property PDMWDocuments^ Documents {
   PDMWDocuments^ get();
}
```

### Property Value

Collection of [documents](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProjects.html) for this project

## VBA Syntax

See [PDMWProject::Documents](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProject~Documents.html).

## See Also

[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)
[IPDMWProject Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject_members.html)
[IPDMWProject::DocumentCount Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~DocumentCount.html)
[IPDMWProject::DocumentList Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~DocumentList.html)
[IPDMWConnection::Documents Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Documents.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
