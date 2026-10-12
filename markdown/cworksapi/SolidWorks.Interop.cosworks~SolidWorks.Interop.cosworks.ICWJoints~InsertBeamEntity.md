---
title: "InsertBeamEntity Method (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "InsertBeamEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~InsertBeamEntity.html"
---

# InsertBeamEntity Method (ICWJoints)

Inserts the specified beam in the joints.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertBeamEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints
Dim DispEntity As System.Object

instance.InsertBeamEntity(DispEntity)
```

### C#

```csharp
void InsertBeamEntity(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertBeamEntity(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: [Beam](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamBody.html) to insert

## VBA Syntax

See [CWJoints::InsertBeamEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~InsertBeamEntity.html).

## Remarks

To add a beam to the joints:

1. [Begin editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html).
2. Add a beam by calling this method.
3. [Save your modification](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeKeepModifiedJointOnUpdate.html).
4. [Calculate](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~CalculateJoints.html) the joints.
5. [End editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsEndEdit.html).

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)
[ICWJoints::RemoveBeamEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~RemoveBeamEntityAt.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
