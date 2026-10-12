---
title: "GetSelections Method (IRefAxisFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefAxisFeatureData"
member: "GetSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelections.html"
---

# GetSelections Method (IRefAxisFeatureData)

Gets the selected entities for this reference axis feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelections( _
   ByRef EntitiesTypeVar As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRefAxisFeatureData
Dim EntitiesTypeVar As System.Object
Dim value As System.Object

value = instance.GetSelections(EntitiesTypeVar)
```

### C#

```csharp
System.object GetSelections(
   out System.object EntitiesTypeVar
)
```

### C++/CLI

```cpp
System.Object^ GetSelections(
   [Out] System.Object^ EntitiesTypeVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntitiesTypeVar`: Array of the types of selected entities for this reference axis feature as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Array of the selected entities

## VBA Syntax

See [RefAxisFeatureData::GetSelections](ms-its:sldworksapivb6.chm::/sldworks~RefAxisFeatureData~GetSelections.html).

## Examples

[Get Selections for Reference Axis Feature (C#)](Get_Selections_for_Reference_Axis_Feature_Example_CSharp.htm)
[Get Selections for Reference Axis Feature (VB.NET)](Get_Selections_for_Reference_Axis_Feature_Example_VBNET.htm)
[Get Selections for Reference Axis Feature (VBA)](Get_Selections_for_Reference_Axis_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRefAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData.html)
[IRefAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.html)
[IRefAxisFeatureData::IGetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~IGetSelections.html)
[IRefAxisFeatureData::GetSelectionsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~GetSelectionsCount.html)
[IRefAxisFeatureData::ISetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~ISetSelections.html)
[IRefAxisFeatureData::SetSelections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~SetSelections.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
