---
title: "PinBallRadius Property (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "PinBallRadius"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~PinBallRadius.html"
---

# PinBallRadius Property (ICWJoints)

Gets or sets the optimal tolerance value for non-touching structural members within a certain distance, which is also referred to as a pinball.

## Syntax

### Visual Basic (Declaration)

```vb
Property PinBallRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints
Dim value As System.Double

instance.PinBallRadius = value

value = instance.PinBallRadius
```

### C#

```csharp
System.double PinBallRadius {get; set;}
```

### C++/CLI

```cpp
property System.double PinBallRadius {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Radius

## VBA Syntax

See [CWJoints::PinBallRadius](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~PinBallRadius.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## Remarks

To specify the pinball radius:

1. [Begin editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html).
2. Specify to [overwrite the pinball value.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeTreatAsJointForClearanceLessThan.html)
3. Change the pinball radius by calling this method.
4. Optionally [change the unit for the pinball radius](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~PinBallRadiusUnit.html).
5. [Calculate](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~CalculateJoints.html) the joints.
6. [End editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsEndEdit.html).

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)
[ICWJoints::IncludeTreatAsJointForClearanceLessThan Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~IncludeTreatAsJointForClearanceLessThan.html)
[ICWJoints::PinBallRadiusUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~PinBallRadiusUnit.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
