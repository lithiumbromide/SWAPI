---
title: "Select Method (ISelectionSet)"
project: "SOLIDWORKS API Help"
interface: "ISelectionSet"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~Select.html"
---

# Select Method (ISelectionSet)

Selects all of the objects in this selection set.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionSet
Dim value As System.Boolean

value = instance.Select()
```

### C#

```csharp
System.bool Select()
```

### C++/CLI

```cpp
System.bool Select();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if all of the objects in this selection set are selected, false if not (see **Remarks**)

## VBA Syntax

See [SelectionSet::Select](ms-its:sldworksapivb6.chm::/sldworks~SelectionSet~Select.html).

## Examples

[Get Objects in Selection Set (C#)](Get_Objects_in_Selection_Set_Example_CSharp.htm)
[Get Objects in Selection Set (VB.NET)](Get_Objects_in_Selection_Set_Example_VBNET.htm)
[Get Objects in Selection Set (VBA)](Get_Objects_in_Selection_Set_Example_VB.htm)

## Remarks

To use this method:

1. Call [ISelectionMgr::SuspendSelectionList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~SuspendSelectionList.html) to suspend the current selection list, preserving its contents and starting a new selection list.
2. Call ISelectionSet::Select to add the objects in the selection set to the new selection list.
3. Process the objects in the new selection list.
4. Call [ISelectionMgr::ResumeSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList.html) to reinstate the suspended selection list.

## See Also

[ISelectionSet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.html)
[ISelectionSet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
