---
title: "SaveAsPDF Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "SaveAsPDF"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~SaveAsPDF.html"
---

# SaveAsPDF Method (IPDMWDocument)

Gets the PDF file for this drawing document from the vault, if the setting to create a PDF file of a drawing document in the vault during check-in was selected.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAsPDF( _
   Optional ByVal saveDir As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim saveDir As System.String
Dim value As System.Integer

value = instance.SaveAsPDF(saveDir)
```

### C#

```csharp
System.int SaveAsPDF(
   System.string saveDir
)
```

### C++/CLI

```cpp
System.int SaveAsPDF(
   System.String^ saveDir
)
```

### Parameters

- `saveDir`: Folder where to save the PDF file

### Return Value

0 if the PDF file is found in the vault, non-0 if not

## VBA Syntax

See [PDMWDocument::SaveAsPDF](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~SaveAsPDF.html).

## Remarks

Before calling this method, call [IPDMDocument::HasPDF](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~HasPDF.html) to determine if a PDF file of the drawing document exists in the vault.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2008 FCS
