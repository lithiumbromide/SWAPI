---
title: "GetSelectByIdSpecification Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetSelectByIdSpecification"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.html"
---

# GetSelectByIdSpecification Method (ISelectionMgr)

Gets the selection specification for the specified object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectByIdSpecification( _
   ByVal Object As System.Object, _
   ByRef SelectByString As System.String, _
   ByRef ObjectType As System.String, _
   ByRef Type As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim Object As System.Object
Dim SelectByString As System.String
Dim ObjectType As System.String
Dim Type As System.Integer
Dim value As System.Boolean

value = instance.GetSelectByIdSpecification(Object, SelectByString, ObjectType, Type)
```

### C#

```csharp
System.bool GetSelectByIdSpecification(
   System.object Object,
   out System.string SelectByString,
   out System.string ObjectType,
   out System.int Type
)
```

### C++/CLI

```cpp
System.bool GetSelectByIdSpecification(
   System.Object^ Object,
   [Out] System.String^ SelectByString,
   [Out] System.String^ ObjectType,
   [Out] System.int Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Object`: Object for which to get the selection specification
- `SelectByString`: Feature name of Object; "" if Object is not a feature
- `ObjectType`: Type of Object
- `Type`: Type of Object as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

True if successful, false if not

## VBA Syntax

See [SelectionMgr::GetSelectByIdSpecification](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetSelectByIdSpecification.html).

## Examples

[Get Selection Specification (VBA)](Get_Selection_Specification_Example_VB.htm)
[Get Selection Specification (VB.NET)](Get_Selection_Specification_Example_VBNET.htm)
[Get Selection Specification (C#)](Get_Selection_Specification_Example_CSharp.htm)

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[ISelectionMgr::GetSelectionSpecification Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.html)
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
[ISelectionMgr::DeSelect2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.html)
[ISelectionMgr::GetSelectedObjectMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.html)
[ISelectionMgr::SetSelectionPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectionPoint2.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
