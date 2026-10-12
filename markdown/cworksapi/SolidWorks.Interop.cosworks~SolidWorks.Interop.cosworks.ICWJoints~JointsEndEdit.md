---
title: "JointsEndEdit Method (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "JointsEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~JointsEndEdit.html"
---

# JointsEndEdit Method (ICWJoints)

Ends editing of joints.

## Syntax

### Visual Basic (Declaration)

```vb
Function JointsEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints
Dim value As System.Integer

value = instance.JointsEndEdit()
```

### C#

```csharp
System.int JointsEndEdit()
```

### C++/CLI

```cpp
System.int JointsEndEdit();
```

## VBA Syntax

See [CWJoints::JointsEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~JointsEndEdit.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## Remarks

To edit joints:

1. [Begin editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html).
2. Modify the joints by [adding beam elements](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~InsertBeamEntity.html), [removing beam elements](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~RemoveBeamEntityAt.html), or [deleting joints](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~DeleteJoint.html).
3. Specify to [overwrite the pinball value.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeTreatAsJointForClearanceLessThan.html)
4. Modify [pinball radius](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~PinBallRadius.html) and [pinball radius unit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~PinBallRadiusUnit.html).
5. Specify whether to [display a neutral axis](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeDisplayNeutralAxis.html) for each axis.
6. [Save your modifications.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeKeepModifiedJointOnUpdate.html)
7. [Calculate](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~CalculateJoints.html) the joints.
8. End editing by calling this method.

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
