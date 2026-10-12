---
title: "DistanceFirstArcCondition Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "DistanceFirstArcCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceFirstArcCondition.html"
---

# DistanceFirstArcCondition Property (IMate2)

Gets the the first arc condition of this distance mate between cylindrical components.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DistanceFirstArcCondition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Integer

value = instance.DistanceFirstArcCondition
```

### C#

```csharp
System.int DistanceFirstArcCondition {get;}
```

### C++/CLI

```cpp
property System.int DistanceFirstArcCondition {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Arc condition as defined by [swDistanceMateArcConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDistanceMateArcConditions_e.html)

## VBA Syntax

See [Mate2::DistanceFirstArcCondition](ms-its:sldworksapivb6.chm::/sldworks~Mate2~DistanceFirstArcCondition.html).

## Examples

[Add and Edit Distance Mate (VBA)](Add_and_Edit_Distance_Mate_Example_VB.htm)
[Add and Edit Distance Mate (VB.NET)](Add_and_Edit_Distance_Mate_Example_VBNET.htm)
[Add and Edit Distance Mate (C#)](Add_and_Edit_Distance_Mate_Example_CSharp.htm)

## Remarks

This property is valid only for distance mates between:

- two cylindrical faces

- or -

- one cylindrical face and one axis.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::DistanceSecondArcCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceSecondArcCondition.html)
[IAssemblyDoc::AddDistanceMate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddDistanceMate.html)
[IAssemblyDoc::EditDistanceMate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditDistanceMate.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
