---
title: "RemoveBeamEntityAt Method (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "RemoveBeamEntityAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~RemoveBeamEntityAt.html"
---

# RemoveBeamEntityAt Method (ICWJoints)

Removes the specified beam from the joints.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveBeamEntityAt( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints
Dim NIndex As System.Integer

instance.RemoveBeamEntityAt(NIndex)
```

### C#

```csharp
void RemoveBeamEntityAt(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveBeamEntityAt(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of the beam to remove

## VBA Syntax

See [CWJoints::RemoveBeamEntityAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~RemoveBeamEntityAt.html).

## Remarks

To determine a valid index for the beam to remove, call [IBeamManager::BeamCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamManager~BeamCount.html).

To remove a beam:

1. [Begin editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html).
2. Remove a beam by calling this method.
3. [Save your modification.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeKeepModifiedJointOnUpdate.html)
4. [Calculate](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~CalculateJoints.html) the joints.
5. [End editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsEndEdit.html).

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)
[ICWJoints::InsertBeamEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~InsertBeamEntity.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
