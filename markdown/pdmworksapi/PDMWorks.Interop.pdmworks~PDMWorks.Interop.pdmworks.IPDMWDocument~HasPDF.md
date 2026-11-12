---
title: "HasPDF Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "HasPDF"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~HasPDF.html"
---

# HasPDF Property (IPDMWDocument)

Gets whether this drawing document has a PDF file in the vault.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HasPDF As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.Integer

value = instance.HasPDF
```

### C#

```csharp
System.int HasPDF {get;}
```

### C++/CLI

```cpp
property System.int HasPDF {
   System.int get();
}
```

### Property Value

0 if this drawing document does not have a PDF file in the vault, 1 if it does

## VBA Syntax

See [PDMWDocument::HasPDF](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~HasPDF.html).

## Remarks

Call [IPDMDocument::SaveAsPDF](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~SaveAsPDF.html) to get the PDF file of the drawing document from the vault, if it exists.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2008 FCS
