---
title: "AccessSelections Method (IDerivedPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~AccessSelections.html"
---

# AccessSelections Method (IDerivedPatternFeatureData)

Gains access to the selections that describe this derived pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessSelections( _
   ByVal TopDoc As System.Object, _
   ByVal Component As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPatternFeatureData
Dim TopDoc As System.Object
Dim Component As System.Object
Dim value As System.Boolean

value = instance.AccessSelections(TopDoc, Component)
```

### C#

```csharp
System.bool AccessSelections(
   System.object TopDoc,
   System.object Component
)
```

### C++/CLI

```cpp
System.bool AccessSelections(
   System.Object^ TopDoc,
   System.Object^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TopDoc`: Top-level document
- `Component`: Component in which the feature is to be modified

### Return Value

True if the selections were successfully accessed, false if not

## VBA Syntax

See [DerivedPatternFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~DerivedPatternFeatureData~AccessSelections.html).

## Examples

[Get and Set Seed Components (C#)](Get_and_Set_Seed_Components_Example_CSharp.htm)
[Get and Set Seed Components (VB.NET)](Get_and_Set_Seed_Components_Example_VBNET.htm)
[Get and Set Seed Components (VBA)](Get_and_Set_Seed_Components_Example_VB.htm)
[Get Number of Instances Skipped in Driving Feature (C#)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_CSharp.htm)
[Get Number of Instances Skipped in Driving Feature (VB.NET)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VBNET.htm)
[Get Number of Instances Skipped in Driving Feature (VBA)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is Nothing or null |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) and [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [IDerivedPatternFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDerivedPatternFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)
[IDerivedPatternFeatureData::IAccessSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~IAccessSelections2.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
