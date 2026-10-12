---
title: "GetDocumentSize Method (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "GetDocumentSize"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~GetDocumentSize.html"
---

# GetDocumentSize Method (IPDMWDocument)

Gets the size (in bytes) of the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDocumentSize() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.Object

value = instance.GetDocumentSize()
```

### C#

```csharp
System.object GetDocumentSize()
```

### C++/CLI

```cpp
System.Object^ GetDocumentSize();
```

### Return Value

Size (in bytes) of the document (see **Remarks**)

## VBA Syntax

See [PDMWDocument::GetDocumentSize](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~GetDocumentSize.html).

## Examples

[Get Size of Document Larger Than 2GB (VBA)](Get_Size_of_Document_Larger_Than_2GB_Example_VB.htm)

## Remarks

Convert the return value to a double. See the example for details.

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMDocument::Size Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Size.html)
[IPDMDocument::SizeH Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~SizeH.html)

## Availability

SOLIDWORKS Workgroup PDM 2013 FCS
