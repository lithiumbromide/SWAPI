---
title: "Description Property (IPDMWDocumentNote)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocumentNote"
member: "Description"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote~Description.html"
---

# Description Property (IPDMWDocumentNote)

Gets the description for this note.

## Syntax

### Visual Basic (Declaration)

```vb
Property Description As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocumentNote
Dim value As System.String

instance.Description = value

value = instance.Description
```

### C#

```csharp
System.string Description {get; set;}
```

### C++/CLI

```cpp
property System.String^ Description {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Description for this note

## VBA Syntax

See [PDMWDocumentNote::Description](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocumentNote~Description.html).

## See Also

[IPDMWDocumentNote Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote.html)
[IPDMWDocumentNote Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
