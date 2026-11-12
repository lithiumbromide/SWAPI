---
title: "CalculateJoints Method (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "CalculateJoints"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~CalculateJoints.html"
---

# CalculateJoints Method (ICWJoints)

Calculates the joints at the free ends of structural members and at the intersection of two or more structural members.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CalculateJoints()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints

instance.CalculateJoints()
```

### C#

```csharp
void CalculateJoints()
```

### C++/CLI

```cpp
void CalculateJoints();
```

## VBA Syntax

See [CWJoints::CalculateJoints](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~CalculateJoints.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## Remarks

To calculate the joints:

1. [Begin editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html).
2. [Include all selected beams](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeAllSelectedBeam.html) or only the [user-selected beams](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeUserSelectedBeam.html).
3. Calculate the joints by calling this method.
4. Optionally modify the joints by:

  1. [Adding beams](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~InsertBeamEntity.html), [removing beams](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~RemoveBeamEntityAt.html), or [deleting joints](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~DeleteJoint.html).
  2. [Saving your modifications](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeKeepModifiedJointOnUpdate.html).
5. Optionally [display or hide a neutral axis](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeDisplayNeutralAxis.html) for each beam.
6. Optionally specify to [overwrite the pinball](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeTreatAsJointForClearanceLessThan.html) value and specify a new [pinball radius](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~PinBallRadius.html) and [pinball radius unit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~PinBallRadiusUnit.html).
7. Recalculate the joints by calling this method again.
8. [End editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsEndEdit.html).

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
