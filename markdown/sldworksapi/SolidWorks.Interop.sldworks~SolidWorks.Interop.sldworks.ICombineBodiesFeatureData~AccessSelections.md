---
title: "AccessSelections Method (ICombineBodiesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICombineBodiesFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~AccessSelections.html"
---

# AccessSelections Method (ICombineBodiesFeatureData)

Gains access to the selections that define this combine feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AccessSelections( _
   ByVal PTopDoc As ModelDoc2, _
   ByVal PComponent As Component2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICombineBodiesFeatureData
Dim PTopDoc As ModelDoc2
Dim PComponent As Component2
Dim value As System.Boolean

value = instance.AccessSelections(PTopDoc, PComponent)
```

### C#

```csharp
System.bool AccessSelections(
   ModelDoc2 PTopDoc,
   Component2 PComponent
)
```

### C++/CLI

```cpp
System.bool AccessSelections(
   ModelDoc2^ PTopDoc,
   Component2^ PComponent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PTopDoc`: Top-level document
- `PComponent`: Component in which the feature is to be modified

### Return Value

True if the selections were successfully accessed

## VBA Syntax

See [CombineBodiesFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~CombineBodiesFeatureData~AccessSelections.html).

## Examples

[Combine Bodies (C#)](Combine_Bodies_Example_CSharp.htm)
[Combine Bodies (VB.NET)](Combine_Bodies_Example_VBNET.htm)
[Combine Bodies (VBA)](Combine_Bodies_Example_VB.htm)

## Remarks

Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the IModelDoc2 for the part Component argument is NULL |
| Assembly | TopDoc is the IModelDoc2 object for the assembly Component argument is the IComponent2 object in which the feature is to be modified |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifiyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you modified the feature
- [ICombineBodiesFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICombineBodiesFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.html)
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
