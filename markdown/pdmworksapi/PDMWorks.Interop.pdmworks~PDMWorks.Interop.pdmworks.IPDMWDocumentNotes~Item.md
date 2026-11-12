---
title: "Item Property (IPDMWDocumentNotes)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocumentNotes"
member: "Item"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNotes~Item.html"
---

# Item Property (IPDMWDocumentNotes)

Gets the specified notes for this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Default Property Item( _
   ByVal Index As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocumentNotes
Dim Index As System.Object
Dim value As System.Object

value = instance.Item(Index)
```

### C#

```csharp
System.object this[
   System.object Index
]; {get;}
```

### C++/CLI

```cpp
property System.Object^ default [System.Object^] {
   System.Object^ get(System.Object^ Index);
}
```

### Parameters

- `Index`: Number indicating which note to get

### Property Value

[IPDMWDocumentNote](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNote.html)

## VBA Syntax

See [PDMWDocumentNotes::Item](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocumentNotes~Item.html).

## See Also

[IPDMWDocumentNotes Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNotes.html)
[IPDMWDocumentNotes Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNotes_members.html)
[IPDMWDocumentNotes::Count Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocumentNotes~Count.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 SP3
