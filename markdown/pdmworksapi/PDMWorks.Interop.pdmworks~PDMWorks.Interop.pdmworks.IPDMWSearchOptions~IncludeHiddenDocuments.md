---
title: "IncludeHiddenDocuments Property (IPDMWSearchOptions)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchOptions"
member: "IncludeHiddenDocuments"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions~IncludeHiddenDocuments.html"
---

# IncludeHiddenDocuments Property (IPDMWSearchOptions)

Gets or sets whether to include hidden projects and documents in a search.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeHiddenDocuments As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchOptions
Dim value As System.Boolean

instance.IncludeHiddenDocuments = value

value = instance.IncludeHiddenDocuments
```

### C#

```csharp
System.bool IncludeHiddenDocuments {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeHiddenDocuments {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to search hidden projects and documents, false to exclude them

## VBA Syntax

See [PDMWSearchOptions::IncludeHiddenDocuments](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchOptions~IncludeHiddenDocuments.html).

## Examples

[Create Search Criteria and Search Vault (VBA)](Create_Search_Criteria_and_Search_Vault_Example_VB.htm)

## Remarks

By default, hidden projects and documents are not searched.

## See Also

[IPDMWSearchOptions Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions.html)
[IPDMWSearchOptions Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
