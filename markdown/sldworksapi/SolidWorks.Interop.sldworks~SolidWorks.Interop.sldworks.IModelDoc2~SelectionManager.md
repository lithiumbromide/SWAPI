---
title: "SelectionManager Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SelectionManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectionManager.html"
---

# SelectionManager Property (IModelDoc2)

Gets the [ISelectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr.html) object for this document, which makes the currently selected object available.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectionManager As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

instance.SelectionManager = value

value = instance.SelectionManager
```

### C#

```csharp
System.object SelectionManager {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SelectionManager {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::SelectionManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SelectionManager.html).

## Examples

[Get Object's Persistent Reference ID (C++)](Get_Object_s_Persistent_Reference_ID_Example_CPlusPlus_COM.htm)
[Create Plane Thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)
[Determine If Sketch Suitable for Feature (VBA)](Determine_If_Sketch_Suitable_for_Feature_Example_VB.htm)
[Find Total Length of Sketch Segments in Sketch (VBA)](Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm)
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)

## Remarks

[ISelectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr.html) objects are transient because they are invalid as soon as another selection is made. So, do not hold on to these pointers for any length of time.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ISelectionManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISelectionManager.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
