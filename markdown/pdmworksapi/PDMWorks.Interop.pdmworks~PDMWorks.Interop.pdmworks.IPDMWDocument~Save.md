---
title: "Save Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "Save"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Save.html"
---

# Save Method (IPDMWDocument)

Copies the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Save( _
   Optional ByVal saveDir As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim saveDir As System.String
Dim value As System.Integer

value = instance.Save(saveDir)
```

### C#

```csharp
System.int Save(
   System.string saveDir
)
```

### C++/CLI

```cpp
System.int Save(
   System.String^ saveDir
)
```

### Parameters

- `saveDir`: Name of the folder to which to copy the document

### Return Value

0 if successful, non-0 if not

## VBA Syntax

See [PDMWDocument::Save](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~Save.html).

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::SaveAsPDF Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~SaveAsPDF.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
