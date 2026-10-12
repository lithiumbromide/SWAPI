---
title: "EditRollback Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "EditRollback"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditRollback.html"
---

# EditRollback Method (IFeatureManager)

Rolls back or forward the rollback bar to a specific location in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditRollback( _
   ByVal Location As System.Integer, _
   ByVal Feature As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Location As System.Integer
Dim Feature As System.String
Dim value As System.Boolean

value = instance.EditRollback(Location, Feature)
```

### C#

```csharp
System.bool EditRollback(
   System.int Location,
   System.string Feature
)
```

### C++/CLI

```cpp
System.bool EditRollback(
   System.int Location,
   System.String^ Feature
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Location`: Location to which to move the rollback bar as defined in [swMoveRollbackBarTo_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveRollbackBarTo_e.html)
- `Feature`: Name of the feature

### Return Value

True if moving the rollback bar back or forward was successful, false if not

## VBA Syntax

See [FeatureManager::EditRollback](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~EditRollback.html).

## Examples

[Roll Back Model (C#)](Roll_Back_Model_Example_CSharp.htm)
[Roll Back Model (VB.NET)](Roll_Back_Model_Example_VBNET.htm)
[Roll Back Model (VBA)](Roll_Back_Model_Example_VB.htm)

## Remarks

When the model is in a rollback state, it reverts to an earlier state, suppressing recently added features. You can add new features or edit existing features while the model is in the rolled-back state.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeature::IsRolledBack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsRolledBack.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
