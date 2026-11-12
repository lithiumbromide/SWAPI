---
title: "DeleteItem Method (IAdvancedSelectionCriteria)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSelectionCriteria"
member: "DeleteItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~DeleteItem.html"
---

# DeleteItem Method (IAdvancedSelectionCriteria)

Deletes a criteria from the advanced component selection list.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteItem( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSelectionCriteria
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.DeleteItem(Index)
```

### C#

```csharp
System.bool DeleteItem(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool DeleteItem(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index number of the criteria to delete

### Return Value

True if criteria is deleted, false if not

## VBA Syntax

See [AdvancedSelectionCriteria::DeleteItem](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSelectionCriteria~DeleteItem.html).

## Remarks

Call [IAdvancedSelectionCriteria::GetItemCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAdvancedSelectionCriteria~GetItemCount.html) to get a valid value for Index before calling this method.

## See Also

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html)
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
