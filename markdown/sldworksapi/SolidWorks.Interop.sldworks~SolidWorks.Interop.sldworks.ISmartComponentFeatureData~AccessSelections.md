---
title: "AccessSelections Method (ISmartComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISmartComponentFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData~AccessSelections.html"
---

# AccessSelections Method (ISmartComponentFeatureData)

Gains access to the selection lists on the PropertyManager page of a Smart Component.

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessSelections( _
   ByVal ShowPMP As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISmartComponentFeatureData
Dim ShowPMP As System.Boolean
Dim value As System.Boolean

value = instance.AccessSelections(ShowPMP)
```

### C#

```csharp
System.bool AccessSelections(
   System.bool ShowPMP
)
```

### C++/CLI

```cpp
System.bool AccessSelections(
   System.bool ShowPMP
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ShowPMP`: True to display the PropertyManager page, false to not (see **Remarks**)

### Return Value

True if the selections where successfully accessed, false if not

## VBA Syntax

See [SmartComponentFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~SmartComponentFeatureData~AccessSelections.html).

## Examples

[Delete Smart Feature (C#)](Delete_Smart_Feature_Example_CSharp.htm)
[Delete Smart Feature (VB.NET)](Delete_Smart_Feature_Example_VBNET.htm)
[Delete Smart Feature (VBA)](Delete_Smart_Feature_Example_VB.htm)

## Remarks

ShowPMP only controls the display of the PropertyManager page. This method allows access to the PropertyManager page selection lists regardless of whether the PropertyManager page is displayed. The selection lists have marks as defined in [swSmartComponentSelectionTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSmartComponentSelectionTypes_e.html).

This method opens the training assembly in which this Smart Component is defined.

**To delete a feature or component from a Smart Component:**

1. Open the Smart Component in SOLIDWORKS.
2. Call [IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) on the "Smart Feature" to get the [ISmartComponentFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISmartComponentFeatureData.html) object.
3. Call this method to open the training assembly of the Smart Component.
4. Call [ISldWorks::ActiveDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActiveDoc.html) to set an assembly document variable.
5. To get a specific feature or component, call [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html)(index, mark), where mark is defined in [swSmartComponentSelectionTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSmartComponentSelectionTypes_e.html) and index is the position of the item in the selection list.
6. Select an already selected feature or component to delete it from its selection list. If the object returned by ISelectionMgr::GetSelectedObject6 is a:

  - feature, call [IFeature::Select2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Select2.html) to delete that feature from the feature selection list.
  - component, call [IComponent2::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Select4.html) to delete that component from the component selection list.
7. Close the training assembly and release access to the selection lists.

**To insert a feature or component into a Smart Component:**

1. Open the Smart Component in SOLIDWORKS.
2. Call [IFeature::GetDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetDefinition.html) on the "Smart Feature" to get the [ISmartComponentFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISmartComponentFeatureData.html) object.
3. Call this method to open the training assembly of the Smart Component.
4. Call [ISldWorks::ActiveDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActiveDoc.html) to point to the training assembly.
5. Call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to specify the feature or component you want to insert, setting Mark to an option in [swSmartComponentSelectionTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSmartComponentSelectionTypes_e.html).
6. Close the training assembly and release access to the selection lists.

**To close the training assembly and release access to the selection lists on the PropertyManager page:**

- Call [ISmartComponentFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISmartComponentFeatureData~ReleaseSelectionAccess.html) if you did not insert or delete features and components.
- Call [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) to rebuild the Smart Component if you inserted or deleted features and components.

## See Also

[ISmartComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.html)
[ISmartComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
