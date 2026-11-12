---
title: "Size Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "Size"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~Size.html"
---

# Size Property (IPDMWDocument)

Gets the size (in bytes) of a document smaller than 2GB or the size that represents the 32 low-order bits of a document larger than 2GB.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Size As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.Integer

value = instance.Size
```

### C#

```csharp
System.int Size {get;}
```

### C++/CLI

```cpp
property System.int Size {
   System.int get();
}
```

### Property Value

Size (in bytes) of a document smaller than 2GB or the size that represents the 32 low-order bits of a document larger than 2GB (see **Remarks**)

## VBA Syntax

See [PDMWDocument::Size](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~Size.html).

## Examples

[Get Size of Document Larger Than 2GB (VBA)](Get_Size_of_Document_Larger_Than_2GB_Example_VB.htm)

## Remarks

| To get the size of a document... | Call... |
| --- | --- |
| Smaller than 2GB | this property |
| Larger than 2GB | this property and IPDMWDocument::SizeH and combine their return values |
| Any size | IPDMWDocument::GetDocumentSize |

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
