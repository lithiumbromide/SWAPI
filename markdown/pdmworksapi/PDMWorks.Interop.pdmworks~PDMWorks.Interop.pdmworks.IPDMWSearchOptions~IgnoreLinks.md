---
title: "IgnoreLinks Property (IPDMWSearchOptions)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchOptions"
member: "IgnoreLinks"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions~IgnoreLinks.html"
---

# IgnoreLinks Property (IPDMWSearchOptions)

Gets or sets whether to ignore links or shortcuts during the search.

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreLinks As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchOptions
Dim value As System.Boolean

instance.IgnoreLinks = value

value = instance.IgnoreLinks
```

### C#

```csharp
System.bool IgnoreLinks {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnoreLinks {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to ignore links or shortcuts, false to search them

## VBA Syntax

See [PDMWSearchOptions::IgnoreLinks](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchOptions~IgnoreLinks.html).

## Examples

[Create Search Criteria and Search Vault (VBA)](Create_Search_Criteria_and_Search_Vault_Example_VB.htm)

## Remarks

By default, links and shortcuts are searched.

## See Also

[IPDMWSearchOptions Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions.html)
[IPDMWSearchOptions Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
