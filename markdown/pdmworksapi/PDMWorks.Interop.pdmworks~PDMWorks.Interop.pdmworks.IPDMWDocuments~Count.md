---
title: "Count Property (IPDMWDocuments)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocuments"
member: "Count"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments~Count.html"
---

# Count Property (IPDMWDocuments)

Gets the number of documents.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Count As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocuments
Dim value As System.Integer

value = instance.Count
```

### C#

```csharp
System.int Count {get;}
```

### C++/CLI

```cpp
property System.int Count {
   System.int get();
}
```

### Property Value

Number of documents

## VBA Syntax

See [PDMWDocuments::Count](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocuments~Count.html).

## Examples

[Get Names of Projects for All Documents in Vault (VB.NET)](Get_Names_Projects_for_Documents_in_Vault_Example_VBNET.htm)

## See Also

[IPDMWDocuments Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments.html)
[IPDMWDocuments Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments_members.html)
[IPDMWDocuments::Item Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocuments~Item.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
