---
title: "AccessSelections Method (ICavityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICavityFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~AccessSelections.html"
---

# AccessSelections Method (ICavityFeatureData)

Gains access to the selections that define this cavity feature.

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
Dim instance As ICavityFeatureData
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

- `TopDoc`: Top-level document (see **Remarks**)
- `Component`: Component in which to modify the feature (see **Remarks**)

### Return Value

True if the selections are successfully accessed, false if not

## VBA Syntax

See [CavityFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~CavityFeatureData~AccessSelections.html).

## Examples

[Create and Modify Cavity Feature (C#)](Create_and_Modify_Cavity_Feature_Example_CSharp.htm)
[Create and Modify Cavity Feature (VB.NET)](Create_and_Modify_Cavity_Feature_Example_VBNET.htm)
[Create and Modify Cavity Feature (VBA)](Create_and_Modify_Cavity_Feature_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [ICavityFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICavityFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
