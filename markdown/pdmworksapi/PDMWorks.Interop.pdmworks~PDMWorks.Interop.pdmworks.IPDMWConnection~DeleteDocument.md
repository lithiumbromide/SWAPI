---
title: "DeleteDocument Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "DeleteDocument"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DeleteDocument.html"
---

# DeleteDocument Method (IPDMWConnection)

Deletes the specified document from the vault.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteDocument( _
   ByVal docname As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim docname As System.String
Dim value As System.Integer

value = instance.DeleteDocument(docname)
```

### C#

```csharp
System.int DeleteDocument(
   System.string docname
)
```

### C++/CLI

```cpp
System.int DeleteDocument(
   System.String^ docname
)
```

### Parameters

- `docname`: Name of the document to delete from the vault

### Return Value

0 if successful, non-0 if not

## VBA Syntax

See [PDMWConnection::DeleteDocument](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~DeleteDocument.html).

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 SP4
