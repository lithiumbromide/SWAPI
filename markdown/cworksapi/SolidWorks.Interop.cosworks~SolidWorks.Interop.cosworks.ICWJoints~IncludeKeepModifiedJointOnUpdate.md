---
title: "IncludeKeepModifiedJointOnUpdate Property (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "IncludeKeepModifiedJointOnUpdate"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~IncludeKeepModifiedJointOnUpdate.html"
---

# IncludeKeepModifiedJointOnUpdate Property (ICWJoints)

Gets or sets whether to save modifications made to the joints.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeKeepModifiedJointOnUpdate As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints
Dim value As System.Boolean

instance.IncludeKeepModifiedJointOnUpdate = value

value = instance.IncludeKeepModifiedJointOnUpdate
```

### C#

```csharp
System.bool IncludeKeepModifiedJointOnUpdate {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeKeepModifiedJointOnUpdate {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to save modifications, false to not

## VBA Syntax

See [CWJoints::IncludeKeepModifiedJointOnUpdate](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~IncludeKeepModifiedJointOnUpdate.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## Remarks

To save modifications made to the joints:

1. [Begin editing.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html)
2. Optionally modify the joints by [adding beam elements](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~InsertBeamEntity.html), [removing beam elements](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~RemoveBeamEntityAt.html), or [deleting joints](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~DeleteJoint.html).
3. Optionally [modify pinballs](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeTreatAsJointForClearanceLessThan.html) and whether to [display a neutral axis](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeDisplayNeutralAxis.html) for each beam.
4. Save all modifications by calling this method.
5. [Calculate](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~CalculateJoints.html) the joints.
6. [End editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsEndEdit.html).

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
