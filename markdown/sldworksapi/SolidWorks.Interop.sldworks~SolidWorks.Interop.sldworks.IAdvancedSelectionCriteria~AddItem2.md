---
title: "AddItem2 Method (IAdvancedSelectionCriteria)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSelectionCriteria"
member: "AddItem2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~AddItem2.html"
---

# AddItem2 Method (IAdvancedSelectionCriteria)

Adds the specified advanced component selection criterion to the list.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddItem2( _
   ByVal Category1 As System.String, _
   ByVal Category2 As System.String, _
   ByVal Condition As System.Integer, _
   ByVal Value As System.String, _
   ByVal IsAnd As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSelectionCriteria
Dim Category1 As System.String
Dim Category2 As System.String
Dim Condition As System.Integer
Dim Value As System.String
Dim IsAnd As System.Boolean
Dim value As System.Integer

value = instance.AddItem2(Category1, Category2, Condition, Value, IsAnd)
```

### C#

```csharp
System.int AddItem2(
   System.string Category1,
   System.string Category2,
   System.int Condition,
   System.string Value,
   System.bool IsAnd
)
```

### C++/CLI

```cpp
System.int AddItem2(
   System.String^ Category1,
   System.String^ Category2,
   System.int Condition,
   System.String^ Value,
   System.bool IsAnd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Category1`: Name of Category1 (see **Remarks**)
- `Category2`: Name of Category2 (see **Remarks**)
- `Condition`: Condition as defined in [swAdvSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAdvSelectType_e.html) (see **Remarks**)
- `Value`: Text value satisfying Condition (see **Remarks**)
- `IsAnd`: True if all of the criteria in the advanced component selection list must be met, false if only this criteria in the advanced component selection list must be met

### Return Value

Index number of the newly added criterion in the advanced component selection criteria list

## VBA Syntax

See [AdvancedSelectionCriteria::AddItem2](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSelectionCriteria~AddItem2.html).

## Remarks

For a list of possible Category1, Category2, Condition, and Value values, see the **Assemblies > Basic Component Operations > Selecting Components > Advanced Component Selection > Search Criteria for Advanced Component Selection** topic in the SOLIDWORKS Design user-interface help.

After calling this method multiple times to add criteria:

- [Save](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~SaveCriteria.html) the criteria.
- [Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~Select.html) the components satisfying the criteria.

## See Also

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html)
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
