---
title: "GetSelectionSpecification Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectionSpecification"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.html"
---

# GetSelectionSpecification Method (ISelectionMgr)

Gets the selection specification at the specified index of the current selection list.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectionSpecification( _
   ByVal Index As System.Integer, _
   ByRef SelectByString As System.String, _
   ByRef ObjectType As System.String, _
   ByRef Type As System.Integer, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Index As System.Integer
Dim SelectByString As System.String
Dim ObjectType As System.String
Dim Type As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.GetSelectionSpecification(Index, SelectByString, ObjectType, Type, X, Y, Z)
```

### C#

```csharp
System.bool GetSelectionSpecification(
   System.int Index,
   out System.string SelectByString,
   out System.string ObjectType,
   out System.int Type,
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### C++/CLI

```cpp
System.bool GetSelectionSpecification(
   System.int Index,
   [Out] System.String^ SelectByString,
   [Out] System.String^ ObjectType,
   [Out] System.int Type,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 1 <= Index in the current list of selected items <= [ISelectionMgr::GetSelectedObjectCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.html)
- `SelectByString`: Feature name of object at Index; "" if object is not a feature
- `ObjectType`: Type of object at Index
- `Type`: Type of object at Index as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `X`: X coordinate of object at Index; 0 if SelectByString is not ""
- `Y`: Y coordinate of object at Index; 0 if SelectByString is not ""
- `Z`: Z coordinate of object at Index; 0 if SelectByString is not ""

### Return Value

True if successful, false if not

## VBA Syntax

See [SelectionMgr::GetSelectionSpecification](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectionSpecification.html).

## Examples

[Get Selection Specification (VBA)](Get_Selection_Specification_Example_VB.htm)
[Get Selection Specification (VB.NET)](Get_Selection_Specification_Example_VBNET.htm)
[Get Selection Specification (C#)](Get_Selection_Specification_Example_CSharp.htm)

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::GetSelectByIdSpecification Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.html)
[ISelectionMgr::GetSelectedObject6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)
[IModelDocExtension::SelectByID2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html)
[IFeature::GetNameForSelection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNameForSelection.html)
[ISelectionMgr::GetSelectedObjectLoop2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.html)
[ISelectionMgr::GetSelectedObjectMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.html)
[ISelectionMgr::GetSelectedObjectsComponent4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent4.html)
[ISelectionMgr::GetSelectedObjectsDrawingView2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.html)
[ISelectionMgr::GetSelectedObjectType3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html)
[ISelectionMgr::GetSelectionPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.html)
[ISelectionMgr::GetSelectionPointInSketchSpace2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.html)
[ISelectionMgr::SetSelectedObjectMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectedObjectMark.html)
[ISelectionMgr::SetSelectionPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectionPoint2.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
