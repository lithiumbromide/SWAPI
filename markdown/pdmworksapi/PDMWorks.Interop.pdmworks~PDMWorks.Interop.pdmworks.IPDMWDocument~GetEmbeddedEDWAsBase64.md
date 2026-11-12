---
title: "GetEmbeddedEDWAsBase64 Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "GetEmbeddedEDWAsBase64"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~GetEmbeddedEDWAsBase64.html"
---

# GetEmbeddedEDWAsBase64 Method (IPDMWDocument)

Gets embedded eDrawing data with Base64 encoding, if available.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEmbeddedEDWAsBase64() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.String

value = instance.GetEmbeddedEDWAsBase64()
```

### C#

```csharp
System.string GetEmbeddedEDWAsBase64()
```

### C++/CLI

```cpp
System.String^ GetEmbeddedEDWAsBase64();
```

### Return Value

Embedded eDrawing data with Base64 encoding

## VBA Syntax

See [PDMWDocument::GetEmbeddedEDWAsBase64](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~GetEmbeddedEDWAsBase64.html).

## Remarks

Data can then be formatted inline into the eDrawing ActiveX control to display within a web page or HTML-formatted email.

Saving a SOLIDWORKS document with embedded eDrawings data is not supported in SOLIDWORKS 2006 and later, because eDrawings can now read native SOLIDWORKS files. This method only returns data for files with embedded eDrawings data created in SOLIDWORKS 2005 and earlier.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWDocument::SaveEmbeddedEDW Method](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~SaveEmbeddedEDW.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
