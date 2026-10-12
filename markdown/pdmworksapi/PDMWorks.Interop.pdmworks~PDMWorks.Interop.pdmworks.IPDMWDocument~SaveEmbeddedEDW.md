---
title: "SaveEmbeddedEDW Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "SaveEmbeddedEDW"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~SaveEmbeddedEDW.html"
---

# SaveEmbeddedEDW Method (IPDMWDocument)

Saves the eDrawings embedded in the SOLIDWORKS document, if one exists.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveEmbeddedEDW( _
   ByVal saveFileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim saveFileName As System.String
Dim value As System.Integer

value = instance.SaveEmbeddedEDW(saveFileName)
```

### C#

```csharp
System.int SaveEmbeddedEDW(
   System.string saveFileName
)
```

### C++/CLI

```cpp
System.int SaveEmbeddedEDW(
   System.String^ saveFileName
)
```

### Parameters

- `saveFileName`: Filename or folder to which to save the embedded eDrawings

### Return Value

0 if successful, non-0 if not

## VBA Syntax

See [PDMWDocument::SaveEmbeddedEDW](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~SaveEmbeddedEDW.html).

## Examples

[Extract Embedded eDrawings Data (VBA)](Extract_Embedded_eDrawings_Data_Example_VB.htm)

## Remarks

Saving a SOLIDWORKS document with embedded eDrawings data is not supported in SOLIDWORKS 2006 and later, because eDrawings can now read native SOLIDWORKS files. This method only returns data for files with embedded eDrawings data created in SOLIDWORKS 2005 and earlier.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::GetEmbeddedEDWAsBase64 Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~GetEmbeddedEDWAsBase64.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
