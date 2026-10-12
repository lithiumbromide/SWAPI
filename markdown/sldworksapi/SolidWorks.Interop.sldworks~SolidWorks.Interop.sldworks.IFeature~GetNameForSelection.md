---
title: "GetNameForSelection Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetNameForSelection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNameForSelection.html"
---

# GetNameForSelection Method (IFeature)

Gets the selected feature's type and name.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNameForSelection( _
   ByRef Type As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Type As System.String
Dim value As System.String

value = instance.GetNameForSelection(Type)
```

### C#

```csharp
System.string GetNameForSelection(
   out System.string Type
)
```

### C++/CLI

```cpp
System.String^ GetNameForSelection(
   [Out] System.String^ Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of feature as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Name of feature

## VBA Syntax

See [Feature::GetNameForSelection](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetNameForSelection.html).

## Examples

[Get Feature Type and Name (C#)](Get_Type_and_Name_of_Feature_Example_CSharp.htm)
[Get Feature Type and Name (VB.NET)](Get_Feature_Type_and_Name_Example_VBNET.htm)
[Get Feature Type and Name (VBA)](Get_Feature_Type_and_Name_Example_VB.htm)
[Get Selections for Reference Axis Feature (C#)](Get_Selections_for_Reference_Axis_Feature_Example_CSharp.htm)
[Get Selections for Reference Axis Feature (VB.NET)](Get_Selections_for_Reference_Axis_Feature_Example_VBNET.htm)
[Get Selections for Reference Axis Feature (VBA)](Get_Selections_for_Reference_Axis_Feature_Example_VB.htm)

## Remarks

Call this method before calling [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to get the type and name to pass to that method.

**NOTE**: [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.html), [IFeature::GetTypeName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetTypeName2.html), and [IFeature::Name](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Name.html) do not return the type and name required by IModelDocExtension::SelectByID2.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeatureStatistics::FeatureTypes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~FeatureTypes.html)
[IFeatureStatistics:FeatureNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics~FeatureNames.html)
[ISelectionMgr::GetSelectedObject6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)
[ISelectionMgr::GetSelectionSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.html)
[ISelectionMgr::GetSelectByIdSpecification Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
