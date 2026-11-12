---
title: "IncludeDisplayNeutralAxis Property (ICWJoints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWJoints"
member: "IncludeDisplayNeutralAxis"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints~IncludeDisplayNeutralAxis.html"
---

# IncludeDisplayNeutralAxis Property (ICWJoints)

Gets or sets whether to show or hide a neutral axis for each beam.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeDisplayNeutralAxis As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWJoints
Dim value As System.Boolean

instance.IncludeDisplayNeutralAxis = value

value = instance.IncludeDisplayNeutralAxis
```

### C#

```csharp
System.bool IncludeDisplayNeutralAxis {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeDisplayNeutralAxis {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to show a neutral axis for each beam, false to hide them

## VBA Syntax

See [CWJoints::IncludeDisplayNeutralAxis](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWJoints~IncludeDisplayNeutralAxis.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## Remarks

To show or hide a neutral axis for each beam:

1. [Begin editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsBeginEdit.html).
2. Display or hide a neutral axis for each beam by calling this method.
3. [End editing](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints~JointsEndEdit.html).

## See Also

[ICWJoints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints.html)
[ICWJoints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWJoints_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
