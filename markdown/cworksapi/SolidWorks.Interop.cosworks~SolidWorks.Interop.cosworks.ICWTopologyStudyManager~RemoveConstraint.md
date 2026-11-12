---
title: "RemoveConstraint Method (ICWTopologyStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: "RemoveConstraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~RemoveConstraint.html"
---

# RemoveConstraint Method (ICWTopologyStudyManager)

Removes the specified constraint from this topology study.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveConstraint( _
   ByVal SConstraintName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
Dim SConstraintName As System.String
Dim value As System.Integer

value = instance.RemoveConstraint(SConstraintName)
```

### C#

```csharp
System.int RemoveConstraint(
   System.string SConstraintName
)
```

### C++/CLI

```cpp
System.int RemoveConstraint(
   System.String^ SConstraintName
)
```

### Parameters

- `SConstraintName`: Name of the constraint to remove

### Return Value

Result code as defined in [swsTopologyStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyError_e.html)

## VBA Syntax

See [CWTopologyStudyManager::RemoveConstraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager~RemoveConstraint.html).

## Examples

See the [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html) example.

## Remarks

You cannot remove the default constraint that is assigned to the goal.

## See Also

[ICWTopologyStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
