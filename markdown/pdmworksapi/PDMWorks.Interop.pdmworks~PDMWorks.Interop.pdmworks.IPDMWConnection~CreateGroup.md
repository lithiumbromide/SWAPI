---
title: "CreateGroup Method (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "CreateGroup"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~CreateGroup.html"
---

# CreateGroup Method (IPDMWConnection)

Creates a new group.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateGroup( _
   ByVal Name As System.String _
) As PDMWGroup
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim Name As System.String
Dim value As PDMWGroup

value = instance.CreateGroup(Name)
```

### C#

```csharp
PDMWGroup CreateGroup(
   System.string Name
)
```

### C++/CLI

```cpp
PDMWGroup^ CreateGroup(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of new group

### Return Value

[IPDMWGroup](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWGroup.html) object

## VBA Syntax

See [PDMWConnection::CreateGroup](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~CreateGroup.html).

## Remarks

Only a vault administrator can use this method.

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)
[IPDMWConnection::DeleteGroup Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~DeleteGroup.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
