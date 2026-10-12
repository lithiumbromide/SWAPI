---
title: "DeleteGroup Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "DeleteGroup"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DeleteGroup.html"
---

# DeleteGroup Method (IPDMWConnection)

Deletes the specified group.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteGroup( _
   ByVal Name As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim Name As System.String

instance.DeleteGroup(Name)
```

### C#

```csharp
void DeleteGroup(
   System.string Name
)
```

### C++/CLI

```cpp
void DeleteGroup(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the group to delete

## VBA Syntax

See [PDMWConnection::DeleteGroup](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~DeleteGroup.html).

## Remarks

Only a vault administrator can use this method.

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)
[IPDMWConnection::CreateGroup](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CreateGroup.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
