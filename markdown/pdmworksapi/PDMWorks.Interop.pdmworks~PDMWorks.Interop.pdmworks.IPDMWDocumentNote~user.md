---
title: "user Property (IPDMWDocumentNote)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocumentNote"
member: "user"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote~user.html"
---

# user Property (IPDMWDocumentNote)

Gets the name of the user who created this note.

## Syntax

### Visual Basic (Declaration)

```vb
Property user As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocumentNote
Dim value As System.String

instance.user = value

value = instance.user
```

### C#

```csharp
System.string user {get; set;}
```

### C++/CLI

```cpp
property System.String^ user {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the user who created this note

## VBA Syntax

See [PDMWDocumentNote::user](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocumentNote~user.html).

## See Also

[IPDMWDocumentNote Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote.html)
[IPDMWDocumentNote Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
