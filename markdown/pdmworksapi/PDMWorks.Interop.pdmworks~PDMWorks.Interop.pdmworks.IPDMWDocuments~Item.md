---
title: "Item Property (IPDMWDocuments)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocuments"
member: "Item"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments~Item.html"
---

# Item Property (IPDMWDocuments)

Gets the specified document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Default Property Item( _
   ByVal Index As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocuments
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

- `Index`: Number or name indicating which document to get (see Remarks)

### Property Value

[IPDMWDocument](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)

## VBA Syntax

See [PDMWDocuments::Item](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocuments~Item.html).

## Examples

[Get Specific Document (VBA)](Get_Specific_Document_Example_VB.htm)

## Remarks

If this collection was returned from [IPDMWDocument::References](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~References.html), then the document name refers to its revision name string, not its document name string.

## See Also

[IPDMWDocuments Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments.html)
[IPDMWDocuments Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments_members.html)
[IPDMWDocuments::Count Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments~Count.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
