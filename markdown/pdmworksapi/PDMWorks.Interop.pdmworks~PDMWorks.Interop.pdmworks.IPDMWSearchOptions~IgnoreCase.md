---
title: "IgnoreCase Property (IPDMWSearchOptions)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWSearchOptions"
member: "IgnoreCase"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions~IgnoreCase.html"
---

# IgnoreCase Property (IPDMWSearchOptions)

Gets or sets whether to ignore text case in text string searches.

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreCase As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWSearchOptions
Dim value As System.Boolean

instance.IgnoreCase = value

value = instance.IgnoreCase
```

### C#

```csharp
System.bool IgnoreCase {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnoreCase {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to ignore text case in text string searches, false to not

## VBA Syntax

See [PDMWSearchOptions::IgnoreCase](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWSearchOptions~IgnoreCase.html).

## Examples

[Create Search Criteria and Search Vault (VBA)](Create_Search_Criteria_and_Search_Vault_Example_VB.htm)

## Requirements

By default, text case is ignored in text string searches.

## See Also

[IPDMWSearchOptions Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions.html)
[IPDMWSearchOptions Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWSearchOptions_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
