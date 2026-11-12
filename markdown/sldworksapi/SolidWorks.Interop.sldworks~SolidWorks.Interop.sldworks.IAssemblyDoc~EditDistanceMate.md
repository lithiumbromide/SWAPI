---
title: "EditDistanceMate Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "EditDistanceMate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditDistanceMate.html"
---

# EditDistanceMate Method (IAssemblyDoc)

Edits a distance mate.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditDistanceMate( _
   ByVal AlignFromEnum As System.Integer, _
   ByVal Flip As System.Boolean, _
   ByVal Distance As System.Double, _
   ByVal DistanceAbsUpperLimit As System.Double, _
   ByVal DistanceAbsLowerLimit As System.Double, _
   ByVal FirstArcCondition As System.Integer, _
   ByVal SecondArcCondition As System.Integer, _
   ByRef ErrorStatus As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim AlignFromEnum As System.Integer
Dim Flip As System.Boolean
Dim Distance As System.Double
Dim DistanceAbsUpperLimit As System.Double
Dim DistanceAbsLowerLimit As System.Double
Dim FirstArcCondition As System.Integer
Dim SecondArcCondition As System.Integer
Dim ErrorStatus As System.Integer

instance.EditDistanceMate(AlignFromEnum, Flip, Distance, DistanceAbsUpperLimit, DistanceAbsLowerLimit, FirstArcCondition, SecondArcCondition, ErrorStatus)
```

### C#

```csharp
void EditDistanceMate(
   System.int AlignFromEnum,
   System.bool Flip,
   System.double Distance,
   System.double DistanceAbsUpperLimit,
   System.double DistanceAbsLowerLimit,
   System.int FirstArcCondition,
   System.int SecondArcCondition,
   out System.int ErrorStatus
)
```

### C++/CLI

```cpp
void EditDistanceMate(
   System.int AlignFromEnum,
   System.bool Flip,
   System.double Distance,
   System.double DistanceAbsUpperLimit,
   System.double DistanceAbsLowerLimit,
   System.int FirstArcCondition,
   System.int SecondArcCondition,
   [Out] System.int ErrorStatus
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AlignFromEnum`: Type of alignment as defined in [swMateAlign_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateAlign_e.html)
- `Flip`: True to flip the mate entities, false to not (see **Remarks**)
- `Distance`: Distance value (see **Remarks**)
- `DistanceAbsUpperLimit`: Absolute maximum distance value (see **Remarks**)
- `DistanceAbsLowerLimit`: Absolute minimum distance value (see **Remarks**)
- `FirstArcCondition`: First arc condition as defined in [swDistanceMateArcConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDistanceMateArcConditions_e.html); valid only for cylindrical distance mates (see **Remarks**)
- `SecondArcCondition`: Second arc condition as defined in swDistanceMateArcConditions_e; valid only for cylindrical distance mates (see **Remarks**)
- `ErrorStatus`: Success or error as defined by [swAddMateError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

## VBA Syntax

See [AssemblyDoc::EditDistanceMate](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~EditDistanceMate.html).

## Examples

[Add and Edit Distance Mate (VBA)](Add_and_Edit_Distance_Mate_Example_VB.htm)
[Add and Edit Distance Mate (VB.NET)](Add_and_Edit_Distance_Mate_Example_VBNET.htm)
[Add and Edit Distance Mate (C#)](Add_and_Edit_Distance_Mate_Example_CSharp.htm)

## Remarks

Select these entities before calling this method:

- Two entities that define the distance mate (use [IEntity::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.html) with Data = Nothing)
- Distance mate feature (use [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.html) with Mark = 0)

If the mate is applied to the closest position that meets the mate condition specified by Distance, then setting Flip to true moves the components to the other possible mate position.

Call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html) after calling this method.

See [IAssemblyDoc::AddDistanceMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddDistanceMate.html) Remarks.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::EditMate4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditMate4.html)
[IMate2::DistanceFirstArcCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceFirstArcCondition.html)
[IMate2::DistanceSecondArcCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceSecondArcCondition.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
