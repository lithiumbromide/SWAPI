---
title: "SaveCriteria Method (IAdvancedSelectionCriteria)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSelectionCriteria"
member: "SaveCriteria"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~SaveCriteria.html"
---

# SaveCriteria Method (IAdvancedSelectionCriteria)

Saves the current query to the specified XML file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveCriteria( _
   ByVal CriteriaFileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSelectionCriteria
Dim CriteriaFileName As System.String
Dim value As System.Boolean

value = instance.SaveCriteria(CriteriaFileName)
```

### C#

```csharp
System.bool SaveCriteria(
   System.string CriteriaFileName
)
```

### C++/CLI

```cpp
System.bool SaveCriteria(
   System.String^ CriteriaFileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CriteriaFileName`: Path and filename (***.xml**) to which to save the current query

### Return Value

True if current query is saved successfully, false if not

## VBA Syntax

See [AdvancedSelectionCriteria::SaveCriteria](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSelectionCriteria~SaveCriteria.html).

## Remarks

Call this method after [adding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~AddItem2.html) criteria to the current advanced component selection criteria list.

As of SOLIDWORKS 2021, you can save queries only in XML format.

As is done using the Advanced Component Selection dialog (**Standard toolbar > Advanced Select**), this method creates a query file in XML format with one or more <Query> and <Boolean> elements. Each <Query> element represents a particular search by Category (Category1 in the user interface) and SubCategory (Category2 in the user interface) to satisfy a Condition expression:

?xml version="1.0" encoding="UTF-8"?>
<SWQueryList>
<Query Name="SelectPegs" Favourites_Index="1">
<Boolean Name="And" Category="Custom Property" SubCategory="IsPeg" Condition="=" Value="Yes"/>
</Query>
<Query Name="SelectBlockParts" Favourites_Index="2">
<Boolean Name="And" Category="Custom Property" SubCategory="IsBlockPart" Condition="=" Value="Yes"/>
</Query>
</SWQueryList>

## See Also

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html)
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
