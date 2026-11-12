---
title: "ChangeStatus Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "ChangeStatus"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ChangeStatus.html"
---

# ChangeStatus Method (IPDMWDocument)

Changes the lifecycle status of the document to the specified lifecycle status.

## Syntax

### Visual Basic (Declaration)

```vb
Function ChangeStatus( _
   ByVal i_bstrStatus As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim i_bstrStatus As System.String
Dim value As System.Integer

value = instance.ChangeStatus(i_bstrStatus)
```

### C#

```csharp
System.int ChangeStatus(
   System.string i_bstrStatus
)
```

### C++/CLI

```cpp
System.int ChangeStatus(
   System.String^ i_bstrStatus
)
```

### Parameters

- `i_bstrStatus`: Value corresponding to one of the life-cycle statuses created in VaultAdmin

### Return Value

0 if successful, non-0 if not

## VBA Syntax

See [PDMWDocument::ChangeStatus](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~ChangeStatus.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWConnection::Statuses Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Statuses.html)
[IPDMWDocument::GetStatus Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~GetStatus.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
