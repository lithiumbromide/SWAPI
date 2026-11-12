---
title: "AccessSelections Method (IHealEdgesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHealEdgesFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~AccessSelections.html"
---

# AccessSelections Method (IHealEdgesFeatureData)

Gains access to the selections that describe this heal edges feature.

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
Dim instance As IHealEdgesFeatureData
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
- `Component`: Component in which the feature is to be modified (see **Remarks**)

### Return Value

True if the selections are accessed, false if not

## VBA Syntax

See [HealEdgesFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~HealEdgesFeatureData~AccessSelections.html).

## Examples

[Modify Heal Edges Feature (VBA)](Modify_Heal_Edges_Feature_Example_VB.htm)
[Get Heal Edges Feature Data (C#)](Get_Heal_Edges_Feature_Data_Example_CSharp.htm)
[Get Heal Edges Feature Data (VB.NET)](Get_Heal_Edges_Feature_Data_Example_VBNET.htm)
[Get Heal Edges Feature Data (VBA)](Get_Heal_Edges_Feature_Data_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is Nothing or null |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefintion](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [IHealEdgesFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHealEdgesFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.html)
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
