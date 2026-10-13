---
title: "SearchFilters Property (ISwDMSearchOption)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSearchOption"
member: "SearchFilters"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption~SearchFilters.html"
---

# SearchFilters Property (ISwDMSearchOption)

Gets or sets the search filters.

## Syntax

### Visual Basic (Declaration)

```vb
Property SearchFilters As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSearchOption
Dim value As System.Integer

instance.SearchFilters = value

value = instance.SearchFilters
```

### C#

```csharp
System.int SearchFilters {get; set;}
```

### C++/CLI

```cpp
property System.int SearchFilters {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Filter search as defined by [SwDMSearchFilters](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmSearchFilters.html)

## VBA Syntax

See [SwDMSearchOption::SearchFilters](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSearchOption~SearchFilters.html).

## Examples

[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)

## See Also

[ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.html)
[ISwDMSearchOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
