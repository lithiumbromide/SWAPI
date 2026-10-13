---
title: "Statuses Property (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "Statuses"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Statuses.html"
---

# Statuses Property (IPDMWConnection)

Gets the defined lifecycle statuses.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Statuses As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim value As System.Object

value = instance.Statuses
```

### C#

```csharp
System.object Statuses {get;}
```

### C++/CLI

```cpp
property System.Object^ Statuses {
   System.Object^ get();
}
```

### Property Value

Array of strings of defined lifecycle statuses

## VBA Syntax

See [PDMWConnection::Statuses](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~Statuses.html).

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)
[IPDMWDocument::ChangeStatus Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ChangeStatus.html)
[IPDMWDocument::GetStatus Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~GetStatus.html)

## Availability

SOLIDWORKS Workgroup PDM 2005 FCS
