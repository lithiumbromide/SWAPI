---
title: "AddDistanceMate Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddDistanceMate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddDistanceMate.html"
---

# AddDistanceMate Method (IAssemblyDoc)

Adds a distance mate to this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDistanceMate( _
   ByVal AlignFromEnum As System.Integer, _
   ByVal Flip As System.Boolean, _
   ByVal Distance As System.Double, _
   ByVal DistanceAbsUpperLimit As System.Double, _
   ByVal DistanceAbsLowerLimit As System.Double, _
   ByVal FirstArcCondition As System.Integer, _
   ByVal SecondArcCondition As System.Integer, _
   ByRef ErrorStatus As System.Integer _
) As Mate2
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
Dim value As Mate2

value = instance.AddDistanceMate(AlignFromEnum, Flip, Distance, DistanceAbsUpperLimit, DistanceAbsLowerLimit, FirstArcCondition, SecondArcCondition, ErrorStatus)
```

### C#

```csharp
Mate2 AddDistanceMate(
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
Mate2^ AddDistanceMate(
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
- `Flip`: True to flip mate entities, false to not (see **Remarks**)
- `Distance`: Distance value (see **Remarks**)
- `DistanceAbsUpperLimit`: Absolute maximum distance value (see **Remarks**)
- `DistanceAbsLowerLimit`: Absolute minimum distance value (see **Remarks**)
- `FirstArcCondition`: First arc condition as defined in [swDistanceMateArcConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDistanceMateArcConditions_e.html); valid only for cylindrical distance mates (see **Remarks**)
- `SecondArcCondition`: Second arc condition as defined in swDistanceMateArcConditions_e; valid only for cylindrical distance mates (see **Remarks**)
- `ErrorStatus`: Success or error as defined by [swAddMateError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

### Return Value

[IMate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)

## VBA Syntax

See [AssemblyDoc::AddDistanceMate](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddDistanceMate.html).

## Examples

[Add and Edit Distance Mate (VBA)](Add_and_Edit_Distance_Mate_Example_VB.htm)
[Add and Edit Distance Mate (VB.NET)](Add_and_Edit_Distance_Mate_Example_VBNET.htm)
[Add and Edit Distance Mate (C#)](Add_and_Edit_Distance_Mate_Example_CSharp.htm)

## Remarks

To specify a distance mate without limits, set the DistanceAbsUpperLimit and DistanceAbsLowerLimit parameters equal to the Distance parameter.

If the mate is applied to the closest position that meets the mate condition specified by Distance, then setting Flip to true moves the components to the other possible mate position.

For cylindrical distance mates only, the following FirstArcCondition-to-SecondArcCondition distance combinations are possible:

| FirstArcCondition as defined in swDistanceMateArcConditions_e | to | SecondArcCondition as defined in swDistanceMateArcConditions_e |
| --- | --- | --- |
| swArcCondition_Center |  | swArcCondition_Center |
| swArcCondition_Center |  | swArcCondition_Minimum |
| swArcCondition_Center |  | swArcCondition_Maximum |
| swArcCondition_Minimum |  | swArcCondition_Center |
| swArcCondition_Minimum |  | swArcCondition_Minimum |
| swArcCondition_Minimum |  | swArcCondition_Maximum |
| swArcCondition_Maximum |  | swArcCondition_Center |
| swArcCondition_Maximum |  | swArcCondition_Minimum |
| swArcCondition_Maximum |  | swArcCondition_Maximum |

To add a distance mate:

1. Call [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html) and [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) to get each mate entity. (For cylindrical distance mates, the selections must be two cylindrical faces or one cylindrical face and one axis.)
2. Call [IModelDoc2::ClearSelection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ClearSelection2.html).
3. Call [IEntity::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.html) to select each entity.
4. Call this method.
5. Call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html) after the mate is created.

If entities are not preselected, then ErrorStatus is swAddMateError_e.swAddMateError_IncorrectSelections, and nothing is returned.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AddMate5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate5.html)
[IAssemblyDoc::EditDistanceMate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditDistanceMate.html)
[IMate2::DistanceFirstArcCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceFirstArcCondition.html)
[IMate2::DistanceSecondArcCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceSecondArcCondition.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
