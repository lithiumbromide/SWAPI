---
title: "ISelectionManager Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ISelectionManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISelectionManager.html"
---

# ISelectionManager Property (IModelDoc2)

Gets the [ISelectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr.html) object for this document, which makes the currently selected object available.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ISelectionManager As SelectionMgr
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As SelectionMgr

value = instance.ISelectionManager
```

### C#

```csharp
SelectionMgr ISelectionManager {get;}
```

### C++/CLI

```cpp
property SelectionMgr^ ISelectionManager {
   SelectionMgr^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[ISelectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr.html) object

## VBA Syntax

See [ModelDoc2::ISelectionManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ISelectionManager.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Deselect Every Other Selected Object (C++)](Deselect_Every_Other_Selected_Object_Example_CPlusPlus_COM.htm)
[Display of Item in FeatureManager Design Tree (C++)](Display_of_Item_in_Feature_Manager_Example_CPlusPlus_COM.htm)
[Get Curve Spline Points (C++)](Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm)
[Get Parent Features (C++)](Get_Parent_Features_Example_CPlusPlus_COM.htm)
[Get Selected Feature (C++)](Get_Selected_Feature_Example_CPlusPlus_COM.htm)
[Get Sketch Segment Constraints (C++)](Get_Sketch_Segment_Constraints_Example_CPlusPlus_COM.htm)
[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)

## Remarks

[ISelectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr.html) objects are transient because they are invalid as soon as another selection is made. So, do not hold on to these pointers for any length of time.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SelectionManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectionManager.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
