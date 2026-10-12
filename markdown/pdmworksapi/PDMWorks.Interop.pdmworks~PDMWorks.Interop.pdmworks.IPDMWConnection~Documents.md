---
title: "Documents Property (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "Documents"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Documents.html"
---

# Documents Property (IPDMWConnection)

Gets the documents for the specified project.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Documents( _
   Optional ByVal project As System.String _
) As PDMWDocuments
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim project As System.String
Dim value As PDMWDocuments

value = instance.Documents(project)
```

### C#

```csharp
PDMWDocuments Documents(
   System.string project
) {get;}
```

### C++/CLI

```cpp
property PDMWDocuments^ Documents {
   PDMWDocuments^ get(System.String^ project);
}
```

### Parameters

- `project`: Name of the project

### Property Value

[Collection of documents](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments.html)

## VBA Syntax

See [PDMWConnection::Documents](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~Documents.html).

## Examples

[Extract Embedded eDrawings Data (VBA)](Extract_Embedded_eDrawings_Data_Example_VB.htm)
[Get Specific Document (VBA)](Get_Specific_Document_Example_VB.htm)
[List Assemblies Where Part Used (VBA)](List_Assemblies_Where_Part_Used_Example_VB.htm)
[Get Names of Projects for All Documents in Vault (VB.NET)](Get_Names_Projects_for_Documents_in_Vault_Example_VBNET.htm)

## Remarks

| If... | Then... |
| --- | --- |
| A project is passed | The documents that exist within the project are returned |
| An empty string is passed | The contents of the vault are returned |

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)
[IPDMWConnection::DocumentList Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DocumentList.html)
[IPDMWProject::DocumentCount Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~DocumentCount.html)
[IPDMWProject::DocumentList Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~DocumentList.html)
[IPDMWProject::Documents Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~Documents.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
