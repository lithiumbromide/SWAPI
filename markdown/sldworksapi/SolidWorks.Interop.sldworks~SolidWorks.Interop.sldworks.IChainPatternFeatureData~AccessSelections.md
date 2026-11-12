---
title: "AccessSelections Method (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "AccessSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~AccessSelections.html"
---

# AccessSelections Method (IChainPatternFeatureData)

Gains access to the selections that define this chain pattern feature.

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
Dim instance As IChainPatternFeatureData
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

- `TopDoc`: Top-level document (see **Remarks**)
- `Component`: Component in which to modify the feature (see **Remarks**)

### Return Value

True if the selections are successfully accessed, false if not

## VBA Syntax

See [ChainPatternFeatureData::AccessSelections](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~AccessSelections.html).

## Examples

[Create and Modify Distance Chain Pattern Feature (C#)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_CSharp.htm)
[Create and Modify Distance Chain Pattern Feature (VB.NET)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VBNET.htm)
[Create and Modify Distance Chain Pattern Feature (VBA)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VB.htm)

## Remarks

| To modify a feature in a... | Then... |
| --- | --- |
| Part | TopDoc argument is the ModelDoc2 object for the part Component argument is Nothing or null |
| Assembly | TopDoc is the ModelDoc2 object for the assembly Component argument is the Component2 object in which to modify the feature |

This method puts the model into a rollback state to allow access to the selections that define this feature. You must use either of the following methods to restore the rollback state:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you modified the feature
- [IChainPatternFeatureData::ReleaseSelectionAccess](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IChainPatternFeatureData~ReleaseSelectionAccess.html) if you did not

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
