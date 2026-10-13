---
title: "PinBallRadiusUnit Property (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "PinBallRadiusUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~PinBallRadiusUnit.html"
---

# PinBallRadiusUnit Property (ICWJoints)

Gets or sets the unit for the optimal tolerance value for non-touching structural members within a certain distance, which is also referred to as a pinball.

## Syntax

### Visual Basic (Declaration)

```vb
Property PinBallRadiusUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints
Dim value As System.Integer

instance.PinBallRadiusUnit = value

value = instance.PinBallRadiusUnit
```

### C#

```csharp
System.int PinBallRadiusUnit {get; set;}
```

### C++/CLI

```cpp
property System.int PinBallRadiusUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units for pinball radius as defined in [swsPinballUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPinballUnit_e.html)

## VBA Syntax

See [CWJoints::PinBallRadiusUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~PinBallRadiusUnit.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## Remarks

To specify the unit for the pinball radius:

1. [Begin editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html).
2. Specify to [overwrite the pinball value](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeTreatAsJointForClearanceLessThan.html).
3. [Optionally change the pinball radius](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~PinBallRadius.html).
4. Change the unit for the pinball radius by calling this method.
5. [Calculate](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~CalculateJoints.html) the joints.
6. [End editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsEndEdit.html).

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)
[ICWJoints::IncludeTreatAsJointForClearanceLessThan Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~IncludeTreatAsJointForClearanceLessThan.html)
[ICWJoints::PinBallRadius Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~PinBallRadius.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
