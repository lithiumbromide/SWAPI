---
title: "GetItem Method (IAdvancedSelectionCriteria)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSelectionCriteria"
member: "GetItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItem.html"
---

# GetItem Method (IAdvancedSelectionCriteria)

Obsolete. Superseded by [IAdvancedSelectionCriteria::GetItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetItem( _
   ByVal Index As System.Integer, _
   ByRef Property As System.String, _
   ByRef Condition As System.Integer, _
   ByRef Value As System.String, _
   ByRef IsAnd As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSelectionCriteria
Dim Index As System.Integer
Dim Property As System.String
Dim Condition As System.Integer
Dim Value As System.String
Dim IsAnd As System.Boolean
Dim value As System.Integer

value = instance.GetItem(Index, Property, Condition, Value, IsAnd)
```

### C#

```csharp
System.int GetItem(
   System.int Index,
   out System.string Property,
   out System.int Condition,
   out System.string Value,
   out System.bool IsAnd
)
```

### C++/CLI

```cpp
System.int GetItem(
   System.int Index,
   [Out] System.String^ Property,
   [Out] System.int Condition,
   [Out] System.String^ Value,
   [Out] System.bool IsAnd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index number of the criteria in the advanced component selection list
- `Property`: Name of property
- `Condition`: Condition as defined in [swAdvSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAdvSelectType_e.html)
- `Value`: Text of the value
- `IsAnd`: True if all of the criteria in the advanced component selection list must be met, false if only this criteria in the advanced component selection list must be met

### Return Value

Value of the Index argument or -1 if criteria specified by Index not found

## VBA Syntax

See [AdvancedSelectionCriteria::GetItem](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSelectionCriteria~GetItem.html).

## Examples

[Use Advanced Component Selection (VBA)](Use_Advanced_Component_Selection_Example_VB.htm)
[Use Advanced Component Selection (VB.NET)](Use_Advanced_Component_Selection_Example_VBNET.htm)
[Use Advanced Component Selection (C#)](Use_Advanced_Component_Selection_Example_CSharp.htm)

## Remarks

Call [IAdvancedSelectionCriteria::GetItemCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAdvancedSelectionCriteria~GetItemCount.html) to get a valid value for Index before calling this method.

## See Also

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html)
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
