---
title: "GetItem2 Method (IAdvancedSelectionCriteria)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSelectionCriteria"
member: "GetItem2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItem2.html"
---

# GetItem2 Method (IAdvancedSelectionCriteria)

Gets the specified advanced component selection criterion.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetItem2( _
   ByVal Index As System.Integer, _
   ByRef Category1 As System.String, _
   ByRef Category2 As System.String, _
   ByRef Condition As System.Integer, _
   ByRef Value As System.String, _
   ByRef IsAnd As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSelectionCriteria
Dim Index As System.Integer
Dim Category1 As System.String
Dim Category2 As System.String
Dim Condition As System.Integer
Dim Value As System.String
Dim IsAnd As System.Boolean
Dim value As System.Integer

value = instance.GetItem2(Index, Category1, Category2, Condition, Value, IsAnd)
```

### C#

```csharp
System.int GetItem2(
   System.int Index,
   out System.string Category1,
   out System.string Category2,
   out System.int Condition,
   out System.string Value,
   out System.bool IsAnd
)
```

### C++/CLI

```cpp
System.int GetItem2(
   System.int Index,
   [Out] System.String^ Category1,
   [Out] System.String^ Category2,
   [Out] System.int Condition,
   [Out] System.String^ Value,
   [Out] System.bool IsAnd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index number of the criterion to retrieve
- `Category1`: Name of Category1 (see **Remarks**)
- `Category2`: Name of Category2 (see **Remarks**)
- `Condition`: Condition as defined in [swAdvSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAdvSelectType_e.html) (see **Remarks**)
- `Value`: Text value satisfying Condition (see **Remarks**)
- `IsAnd`: True if all of the criteria in the advanced component selection criteria list must be met, false if only this criterion must be met

### Return Value

Value of the Index argument or -1 if criterion specified by Index not found

## VBA Syntax

See [AdvancedSelectionCriteria::GetItem2](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSelectionCriteria~GetItem2.html).

## Examples

See the [IAdvancedSelectionCriteria](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html) examples.

## Remarks

Call [IAdvancedSelectionCriteria::GetItemCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAdvancedSelectionCriteria~GetItemCount.html) to get a valid value for Index before calling this method.

For a list of possible Category1, Category2, Condition, and Value values, see **Assemblies > Basic Component Operations > Selecting Components > Advanced Component Selection > Search Criteria for Advanced Component Selection** topic in the SOLIDWORKS Design user-interface help.

## See Also

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html)
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
