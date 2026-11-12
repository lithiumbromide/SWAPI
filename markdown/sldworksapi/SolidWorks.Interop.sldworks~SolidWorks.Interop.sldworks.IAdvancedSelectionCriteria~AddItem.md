---
title: "AddItem Method (IAdvancedSelectionCriteria)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSelectionCriteria"
member: "AddItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~AddItem.html"
---

# AddItem Method (IAdvancedSelectionCriteria)

Obsolete. Superseded by [IAdvancedSelectionCriteria::AddItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~AddItem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddItem( _
   ByVal Property As System.String, _
   ByVal Condition As System.Integer, _
   ByVal Value As System.String, _
   ByVal IsAnd As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSelectionCriteria
Dim Property As System.String
Dim Condition As System.Integer
Dim Value As System.String
Dim IsAnd As System.Boolean
Dim value As System.Integer

value = instance.AddItem(Property, Condition, Value, IsAnd)
```

### C#

```csharp
System.int AddItem(
   System.string Property,
   System.int Condition,
   System.string Value,
   System.bool IsAnd
)
```

### C++/CLI

```cpp
System.int AddItem(
   System.String^ Property,
   System.int Condition,
   System.String^ Value,
   System.bool IsAnd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Property`: Name of property
- `Condition`: Condition as defined in [swAdvSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAdvSelectType_e.html)
- `Value`: Text of the value
- `IsAnd`: True if all of the criteria in the advanced component selection list must be met, false if only this criteria in the advanced component selection list must be met

### Return Value

Index number of the newly added criteria in the advanced component selection list

## VBA Syntax

See [AdvancedSelectionCriteria::AddItem](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSelectionCriteria~AddItem.html).

## Examples

[Use Advanced Component Selection (VBA)](Use_Advanced_Component_Selection_Example_VB.htm)
[Use Advanced Component Selection (VB.NET)](Use_Advanced_Component_Selection_Example_VBNET.htm)
[Use Advanced Component Selection (C#)](Use_Advanced_Component_Selection_Example_CSharp.htm)

## See Also

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html)
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
