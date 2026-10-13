---
title: "GetSpecificDocument Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "GetSpecificDocument"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~GetSpecificDocument.html"
---

# GetSpecificDocument Method (IPDMWConnection)

Gets the specified document and version of that document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSpecificDocument( _
   ByVal Name As System.String, _
   Optional ByVal Revision As System.String _
) As PDMWDocument
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim Name As System.String
Dim Revision As System.String
Dim value As PDMWDocument

value = instance.GetSpecificDocument(Name, Revision)
```

### C#

```csharp
PDMWDocument GetSpecificDocument(
   System.string Name,
   System.string Revision
)
```

### C++/CLI

```cpp
PDMWDocument^ GetSpecificDocument(
   System.String^ Name,
   System.String^ Revision
)
```

### Parameters

- `Name`: Name of the document to get
- `Revision`: Version of the document to get; if not specified, the most recent version of the specified document is used

### Return Value

Pointer to the specified document

## VBA Syntax

See [PDMWConnection::GetSpecificDocument](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~GetSpecificDocument.html).

## Examples

[Get Specific Document (VBA)](Get_Specific_Document_Example_VB.htm)

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)
[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
