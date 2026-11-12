---
title: "GetSelectedObjectsComponent4 Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectedObjectsComponent4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent4.html"
---

# GetSelectedObjectsComponent4 Method (ISelectionMgr)

Gets the selected component in an assembly or drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectedObjectsComponent4( _
   ByVal Index As System.Integer, _
   ByVal Mark As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim Mark As System.Integer
Dim value As System.Object

value = instance.GetSelectedObjectsComponent4(Index, Mark)
```

### C#

```csharp
System.object GetSelectedObjectsComponent4(
   System.int Index,
   System.int Mark
)
```

### C++/CLI

```cpp
System.Object^ GetSelectedObjectsComponent4(
   System.int Index,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index position within the current list of selected items, where the index ranges from 1 to [ISelectionMgr::GetSelectedObjectCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html) (see **Remarks**)
- `Mark`: - -1 = All selections regardless of marks

  0 = Only the selections without marks

  Any other value = Value that was used to mark and select an object

### Return Value

[Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) or [Drawing component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent.html)

## VBA Syntax

See [SelectionMgr::GetSelectedObjectsComponent4](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectedObjectsComponent4.html).

## Examples

[Move Assembly Components to New Folder (C#)](Move_Assembly_Components_to_New_Folder_Example_CSharp.htm)
[Move Assembly Components to New Folder (VB.NET)](Move_Assembly_Components_to_New_Folder_Example_VBNET.htm)
[Move Assembly Components to New Folder (VBA)](Move_Assembly_Components_to_New_Folder_Example_VB.htm)
[Select Drawing Component (C#)](Select_Drawing_Component_Example_CSharp.htm)
[Select Drawing Component (VB.NET)](Select_Drawing_Component_Example_VBNET.htm)
[Select Drawing Component (VBA)](Select_Drawing_Component_Example_VB.htm)

## Remarks

The index starts at 1, even when using C++. However, if you specify -1 for the Index argument, then the Mark argument is ignored and the dynamically highlighted component is selected if dynamic highlighting is turned on. See also IAssemblyDoc event [DynamicHighlightNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_DynamicHighlightNotifyEventHandler.html).

The difference between this method and the now obsolete [ISelectionMgr::GetSelectedObjectsComponent3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.html) is that ISelectionMgr::GetSelectedObjectsComponent4 can return an [IDrawingComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent.html) and ISelectionMgr::GetSelectedObjectsComponent3 cannot.

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::DeSelect2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.html)
[ISelectionMgr::GetSelectedObject6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)
[ISelectionMgr::GetSelectedObjectLoop2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.html)
[ISelectionMgr::GetSelectedObjectMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.html)
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.html)
[ISelectionMgr::GetSelectedObjectType3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html)
[ISelectionMgr::GetSelectionPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.html)
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.html)
[ISelectionMgr::IDeSelect2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.html)
[ISelectionMgr::IGetSelectionPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.html)
[ISelectionMgr::IGetSelectionPointInSketchSpace2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.html)
[IComponent2::Select4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select4.html)
[ISelectionMgr::GetSelectByIdSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.html)
[ISelectionMgr::GetSelectionSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.html)

## Availability

SOLIDWORKS 2013 SP03, Revision Number 21.3
