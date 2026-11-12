---
title: "ClearSelection2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ClearSelection2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.html"
---

# ClearSelection2 Method (IModelDoc2)

Clears the selection list.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ClearSelection2( _
   ByVal All As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim All As System.Boolean

instance.ClearSelection2(All)
```

### C#

```csharp
void ClearSelection2(
   System.bool All
)
```

### C++/CLI

```cpp
void ClearSelection2(
   System.bool All
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `All`: True clears the entire existing selection list, false clears only the items in the active selection list (see **Remarks**)

## VBA Syntax

See [ModelDoc2::ClearSelection2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ClearSelection2.html).

## Examples

[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)
[Get Bodies (C++)](Get_Bodies_Example_CPlusPlus_COM.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Add Distance Mates (VBA)](Add_Distance_Mates_Example_VB.htm)
[Create Plane Thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)
[Insert a Note (VBA)](Insert_a_Note_Example_VB.htm)
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)

## Remarks

False only works if the current PropertyManager page contains a selection list; otherwise, this method clears all selections.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISelectionMgr::SuspendSelectionList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SuspendSelectionList.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
