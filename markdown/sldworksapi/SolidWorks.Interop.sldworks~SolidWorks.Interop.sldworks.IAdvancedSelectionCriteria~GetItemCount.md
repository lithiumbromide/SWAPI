---
title: "GetItemCount Method (IAdvancedSelectionCriteria)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSelectionCriteria"
member: "GetItemCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItemCount.html"
---

# GetItemCount Method (IAdvancedSelectionCriteria)

Gets the number of criteria in the advanced component selection criteria list.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetItemCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSelectionCriteria
Dim value As System.Integer

value = instance.GetItemCount()
```

### C#

```csharp
System.int GetItemCount()
```

### C++/CLI

```cpp
System.int GetItemCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of criteria in the advanced component selection criteria list

## VBA Syntax

See [AdvancedSelectionCriteria::GetItemCount](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSelectionCriteria~GetItemCount.html).

## Examples

See the [IAdvancedSelectionCriteria](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html) examples.

## Remarks

Call this method before calling [IAdvancedSelectionCriteriaClass::GetItem](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAdvancedSelectionCriteria~GetItem.html) and [IAdvancedSelectionCriteriaClass::DeleteItem](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAdvancedSelectionCriteria~DeleteItem.html) to get the number of criteria in the advanced component selection criteria list.

## See Also

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html)
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
