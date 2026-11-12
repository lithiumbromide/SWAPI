---
title: "GetStatus Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "GetStatus"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~GetStatus.html"
---

# GetStatus Method (IPDMWDocument)

Gets the lifecycle status of the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStatus() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.String

value = instance.GetStatus()
```

### C#

```csharp
System.string GetStatus()
```

### C++/CLI

```cpp
System.String^ GetStatus();
```

### Return Value

Lifecycle status

## VBA Syntax

See [PDMWDocument::GetStatus](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~GetStatus.html).

## Examples

[Extract Embedded eDrawings Data (VBA)](Extract_Embedded_eDrawings_Data_Example_VB.htm)

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::ChangeStatus Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~ChangeStatus.html)
[IPDMWConnection::Statuses Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConnection~Statuses.html)

## Availability

SOLIDWORKS Workgroup PDM 2005 FCS
