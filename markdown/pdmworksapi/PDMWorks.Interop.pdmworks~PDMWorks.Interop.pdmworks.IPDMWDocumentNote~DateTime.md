---
title: "DateTime Property (IPDMWDocumentNote)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocumentNote"
member: "DateTime"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote~DateTime.html"
---

# DateTime Property (IPDMWDocumentNote)

Gets the date and time of the note associated with this document.

## Syntax

### Visual Basic (Declaration)

```vb
Property DateTime As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocumentNote
Dim value As System.String

instance.DateTime = value

value = instance.DateTime
```

### C#

```csharp
System.string DateTime {get; set;}
```

### C++/CLI

```cpp
property System.String^ DateTime {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Date and time of the note associated with this document

## VBA Syntax

See [PDMWDocumentNote::DateTime](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocumentNote~DateTime.html).

## See Also

[IPDMWDocumentNote Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote.html)
[IPDMWDocumentNote Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
