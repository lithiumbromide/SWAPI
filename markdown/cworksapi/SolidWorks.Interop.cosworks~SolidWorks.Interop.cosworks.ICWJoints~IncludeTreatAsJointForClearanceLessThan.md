---
title: "IncludeTreatAsJointForClearanceLessThan Property (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "IncludeTreatAsJointForClearanceLessThan"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~IncludeTreatAsJointForClearanceLessThan.html"
---

# IncludeTreatAsJointForClearanceLessThan Property (ICWJoints)

Gets or sets whether to overwrite the optimal tolerance value for non-touching structural members within a certain distance, also called pinballs.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeTreatAsJointForClearanceLessThan As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints
Dim value As System.Boolean

instance.IncludeTreatAsJointForClearanceLessThan = value

value = instance.IncludeTreatAsJointForClearanceLessThan
```

### C#

```csharp
System.bool IncludeTreatAsJointForClearanceLessThan {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeTreatAsJointForClearanceLessThan {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to overwrite the pinball value, false to not

## VBA Syntax

See [CWJoints::IncludeTreatAsJointForClearanceLessThan](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~IncludeTreatAsJointForClearanceLessThan.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## Remarks

To overwrite the pinball value:

1. [Begin editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html).
2. Specify to overwrite the pinball value by calling this method.
3. [Change the pinball radius](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~PinBallRadius.html).
4. [Change the unit for the pinball radius](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~PinBallRadiusUnit.html).
5. [Calculate](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~CalculateJoints.html) the joints.
6. [End editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsEndEdit.html).

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)
[ICWJoints::PinBallRadius Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~PinBallRadius.html)
[ICWJoints::PinBallRadiusUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~PinBallRadiusUnit.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
