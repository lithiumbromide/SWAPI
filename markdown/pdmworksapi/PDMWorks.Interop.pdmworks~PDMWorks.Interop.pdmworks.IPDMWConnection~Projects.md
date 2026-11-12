---
title: "Projects Property (IPDMWConnection)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConnection"
member: "Projects"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Projects.html"
---

# Projects Property (IPDMWConnection)

Gets the SOLIDWORKS Workgroup PDM projects.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Projects As PDMWProjects
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConnection
Dim value As PDMWProjects

value = instance.Projects
```

### C#

```csharp
PDMWProjects Projects {get;}
```

### C++/CLI

```cpp
property PDMWProjects^ Projects {
   PDMWProjects^ get();
}
```

### Property Value

Collection of [SOLIDWORKS Workgroup PDM projects](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProjects.html)

## VBA Syntax

See [PDMWConnection::Projects](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConnection~Projects.html).

## See Also

[IPDMWConnection Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection.html)
[IPDMWConnection Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
