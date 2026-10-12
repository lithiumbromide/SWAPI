---
title: "SizeH Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "SizeH"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~SizeH.html"
---

# SizeH Property (IPDMWDocument)

Gets the size that represents the 32 high-order bits of a document larger than 2GB.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SizeH As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.Integer

value = instance.SizeH
```

### C#

```csharp
System.int SizeH {get;}
```

### C++/CLI

```cpp
property System.int SizeH {
   System.int get();
}
```

### Property Value

Size that represents the 32 high-order bits of a document larger than 2GB (see **Remarks**)

## VBA Syntax

See [PDMWDocument::SizeH](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~SizeH.html).

## Examples

[Get Size of Document Larger Than 2GB (VBA)](Get_Size_of_Document_Larger_Than_2GB_Example_VB.htm)

## Remarks

| To get the size of a document... | Call... |
| --- | --- |
| Smaller than 2GB | IPDMWDocument::Size |
| Larger than 2GB | this property and IPDMWDocument::Size and combine their return values |
| Any size | IPDMWDocument::GetDocumentSize |

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2013 FCS
