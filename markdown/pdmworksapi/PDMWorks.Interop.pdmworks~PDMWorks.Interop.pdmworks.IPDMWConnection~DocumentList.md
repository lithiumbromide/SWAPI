---
title: "DocumentList Property (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "DocumentList"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DocumentList.html"
---

# DocumentList Property (IPDMWConnection)

Gets a the list of document names for the specified project.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DocumentList( _
   Optional ByVal project As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim project As System.String
Dim value As System.Object

value = instance.DocumentList(project)
```

### C#

```csharp
System.object DocumentList(
   System.string project
) {get;}
```

### C++/CLI

```cpp
property System.Object^ DocumentList {
   System.Object^ get(System.String^ project);
}
```

### Parameters

- `project`: Name of the project to which the documents belong

### Property Value

Array of the list of documents belonging to the specified project

## VBA Syntax

See [PDMWConnection::DocumentList](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~DocumentList.html).

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)
[IPDMWConnection::Documents Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Documents.html)
[IPDMWProject::DocumentCount Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~DocumentCount.html)
[IPDMWProject::DocumentList Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~DocumentList.html)
[IPDMWProject::Documents Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~Documents.html)

## Availability

SOLIDWORKS Workgroup PDM 2007 FCS
