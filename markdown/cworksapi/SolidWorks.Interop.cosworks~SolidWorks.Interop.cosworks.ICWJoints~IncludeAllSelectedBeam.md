---
title: "IncludeAllSelectedBeam Property (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "IncludeAllSelectedBeam"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~IncludeAllSelectedBeam.html"
---

# IncludeAllSelectedBeam Property (ICWJoints)

Get or sets whether to include all beams in the joints.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeAllSelectedBeam As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints
Dim value As System.Boolean

instance.IncludeAllSelectedBeam = value

value = instance.IncludeAllSelectedBeam
```

### C#

```csharp
System.bool IncludeAllSelectedBeam {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeAllSelectedBeam {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to include all beams in the joints, false to not

## VBA Syntax

See [CWJoints::IncludeAllSelectedBeam](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~IncludeAllSelectedBeam.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## Remarks

To include all beams in the joints:

1. [Begin editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html).
2. Include all beams by calling this method.
3. [Save your modification.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~IncludeKeepModifiedJointOnUpdate.html)
4. [Calculate](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~CalculateJoints.html) the joints.
5. [End editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsEndEdit.html).

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)
[ICWJoints::IncludeUserSelectedBeam Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~IncludeUserSelectedBeam.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
