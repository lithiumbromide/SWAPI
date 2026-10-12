---
title: "WhereUsed Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "WhereUsed"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~WhereUsed.html"
---

# WhereUsed Property (IPDMWDocument)

Gets the links to the documents that reference this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property WhereUsed As PDMWLinks
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As PDMWLinks

value = instance.WhereUsed
```

### C#

```csharp
PDMWLinks WhereUsed {get;}
```

### C++/CLI

```cpp
property PDMWLinks^ WhereUsed {
   PDMWLinks^ get();
}
```

### Property Value

Collection of [links](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWLinks.html) to the documents that reference this document

## VBA Syntax

See [PDMWDocument::WhereUsed](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~WhereUsed.html).

## Examples

[List Assemblies Where Part Used (VBA)](List_Assemblies_Where_Part_Used_Example_VB.htm)

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
