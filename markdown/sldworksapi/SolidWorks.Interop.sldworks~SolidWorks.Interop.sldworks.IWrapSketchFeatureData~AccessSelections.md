---
title: "AccessSelections Method (IWrapSketchFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWrapSketchFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData~AccessSelections.html"
---

# AccessSelections Method (IWrapSketchFeatureData)

Gains access to the selections that define this wrap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessSelections( _
   ByVal TopDoc As ModelDoc2, _
   ByVal Component As Component2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWrapSketchFeatureData
Dim TopDoc As ModelDoc2
Dim Component As Component2
Dim value As System.Boolean

value = instance.AccessSelections(TopDoc, Component)
```

### C#

```csharp
System.bool AccessSelections(
   ModelDoc2 TopDoc,
   Component2 Component
)
```

### C++/CLI

```cpp
System.bool AccessSelections(
   ModelDoc2^ TopDoc,
   Component2^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopDoc`: Top-level document
- `Component`: Component in which the feature is to be modified

### Return Value

TRUE if the selections are successfully accessed, FALSE if not

## VBA Syntax

See [WrapSketchFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~WrapSketchFeatureData~AccessSelections.html).

## Examples

[Change Wrap Feature Face (C#)](Change_Wrap_Feature_Face_Example_CSharp.htm)
[Change Wrap Feature Face (VB.NET)](Change_Wrap_Feature_Face_Example_VBNET.htm)
[Change Wrap Feature Face (VBA)](Change_Wrap_Feature_Face_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [IWrapFeatureData2::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWrapSketchFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[IWrapSketchFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.html)
[IWrapSketchFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
