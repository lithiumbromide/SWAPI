---
title: "AddMate5 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddMate5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate5.html"
---

# AddMate5 Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::CreateMate.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMate5( _
   ByVal MateTypeFromEnum As System.Integer, _
   ByVal AlignFromEnum As System.Integer, _
   ByVal Flip As System.Boolean, _
   ByVal Distance As System.Double, _
   ByVal DistanceAbsUpperLimit As System.Double, _
   ByVal DistanceAbsLowerLimit As System.Double, _
   ByVal GearRatioNumerator As System.Double, _
   ByVal GearRatioDenominator As System.Double, _
   ByVal Angle As System.Double, _
   ByVal AngleAbsUpperLimit As System.Double, _
   ByVal AngleAbsLowerLimit As System.Double, _
   ByVal ForPositioningOnly As System.Boolean, _
   ByVal LockRotation As System.Boolean, _
   ByVal WidthMateOption As System.Integer, _
   ByRef ErrorStatus As System.Integer _
) As Mate2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim MateTypeFromEnum As System.Integer
Dim AlignFromEnum As System.Integer
Dim Flip As System.Boolean
Dim Distance As System.Double
Dim DistanceAbsUpperLimit As System.Double
Dim DistanceAbsLowerLimit As System.Double
Dim GearRatioNumerator As System.Double
Dim GearRatioDenominator As System.Double
Dim Angle As System.Double
Dim AngleAbsUpperLimit As System.Double
Dim AngleAbsLowerLimit As System.Double
Dim ForPositioningOnly As System.Boolean
Dim LockRotation As System.Boolean
Dim WidthMateOption As System.Integer
Dim ErrorStatus As System.Integer
Dim value As Mate2

value = instance.AddMate5(MateTypeFromEnum, AlignFromEnum, Flip, Distance, DistanceAbsUpperLimit, DistanceAbsLowerLimit, GearRatioNumerator, GearRatioDenominator, Angle, AngleAbsUpperLimit, AngleAbsLowerLimit, ForPositioningOnly, LockRotation, WidthMateOption, ErrorStatus)
```

### C#

```csharp
Mate2 AddMate5(
   System.int MateTypeFromEnum,
   System.int AlignFromEnum,
   System.bool Flip,
   System.double Distance,
   System.double DistanceAbsUpperLimit,
   System.double DistanceAbsLowerLimit,
   System.double GearRatioNumerator,
   System.double GearRatioDenominator,
   System.double Angle,
   System.double AngleAbsUpperLimit,
   System.double AngleAbsLowerLimit,
   System.bool ForPositioningOnly,
   System.bool LockRotation,
   System.int WidthMateOption,
   out System.int ErrorStatus
)
```

### C++/CLI

```cpp
Mate2^ AddMate5(
   System.int MateTypeFromEnum,
   System.int AlignFromEnum,
   System.bool Flip,
   System.double Distance,
   System.double DistanceAbsUpperLimit,
   System.double DistanceAbsLowerLimit,
   System.double GearRatioNumerator,
   System.double GearRatioDenominator,
   System.double Angle,
   System.double AngleAbsUpperLimit,
   System.double AngleAbsLowerLimit,
   System.bool ForPositioningOnly,
   System.bool LockRotation,
   System.int WidthMateOption,
   [Out] System.int ErrorStatus
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MateTypeFromEnum`: Type of mate as defined in [swMateType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateType_e.html) (see **Remarks**)
- `AlignFromEnum`: Type of alignment as defined in [swMateAlign_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateAlign_e.html)
- `Flip`: True to flip the mate entities, false to not; valid only if MateTypeFromEnum is swMatetype_e.swMateDISTANCE
- `Distance`: Distance value; valid only if MateTypeFromEnum is swMateType_e.swMateDISTANCE
- `DistanceAbsUpperLimit`: Absolute maximum distance value; valid only if MateTypeFromEnum is swMateType_e.swMateDISTANCE (see **Remarks**)
- `DistanceAbsLowerLimit`: Absolute minimum distance value; valid only if MateTypeFromEnum is swMateType_e.swMateDISTANCE (see **Remarks**)
- `GearRatioNumerator`: Gear ratio numerator value; valid only if MateTypeFromEnum is swMateType_e.swMateGEAR
- `GearRatioDenominator`: Gear ratio denominator value; valid only if MateTypeFromEnum is swMateType_e.swMateGEAR
- `Angle`: Angle value; valid only if MateTypeFromEnum is swMateType_e.swMateANGLE
- `AngleAbsUpperLimit`: Absolute maximum angle value; valid only if MateTypeFromEnum is swMateType_e.swMateANGLE
- `AngleAbsLowerLimit`: Absolute minimum angle value; valid only if MateTypeFromEnum is swMateType_e.swMateANGLE
- `ForPositioningOnly`: True to only position the components according to the mating relationship and not return a mate, false to return a mate
- `LockRotation`: True to lock component rotation, false to not
- `WidthMateOption`: Width mate options as defined in [swMateWidthOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateWidthOptions_e.html); valid only if MateTypeFromEnum is swMateType_e.swMateWIDTH
- `ErrorStatus`: Success or error as defined by [swAddMateError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

### Return Value

[Mate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2.html)

## VBA Syntax

See [AssemblyDoc::AddMate5](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddMate5.html).

## Examples

[Add and Mate Component (VBA)](Add_Component_and_Mate_Example_VB.htm)
[Add and Mate Component (VB.NET)](Add_Component_and_Mate_Example_VBNET.htm)
[Add and Mate Component (C#)](Add_Component_and_Mate_Example_CSharp.htm)
[Copy Component With Profile Center Mate (C#)](Copy_Component_With_Profile_Center_Mate_Example_CSharp.htm)
[Copy Component With Profile Center Mate (VB.NET)](Copy_Component_With_Profile_Center_Mate_Example_VBNET.htm)
[Copy Component With Profile Center Mate (VBA)](Copy_Component_With_Profile_Center_Mate_Example_VB.htm)

## Remarks

To create:

- Standard, advanced, and mechanical mates, use [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html).
- Misaligned concentric mates, use [IAssemblyDoc::AddConcentricMateWithTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddConcentricMateWithTolerance.html).
- Cylindrical distance mates, use [IAssemblyDoc::AddDistanceMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddDistanceMate.html).

The difference between this method and the now obsolete IAssemblyDoc::AddMate4 is the WidthMateOption parameter.

To specify a distance mate without limits, set the DistanceAbsUpperLimit and DistanceAbsLowerLimit parameters equal to the Distance parameter.

If MateTypeFromEnum is swMateType_e.swMateDISTANCE or swMateType_e.swMateANGLE, and the mate is applied to the closest position that meets the mate condition specified by Distance or Angle, then setting Flip to true moves the components to the other possible mate position.

To add a standard or mechanical mate:

1. Call [IModelDoc2::ClearSelection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ClearSelection2.html) before selecting entities to mate.
2. Call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select each entity to mate.

  | If MateTypeFromEnum is... | Use selection mark... |
  | --- | --- |
  | swMateType_e.swMateCAMFOLLOWER | 8 |
  | swMateType_e.swMateWIDTH | 16 |
  | Other swMateType_e option | 1 |
3. Call this method.
4. Call IModelDoc2::ClearSelection2 after the mate is created.

If entities are not preselected, then ErrorStatus is swAddMateError_e.swAddMateError_IncorrectSelections, and nothing is returned.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::EditMate3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditMate3.html)
[IAssemblyDoc::EditConcentricMate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditConcentricMate.html)
[IAssemblyDoc::EditDistanceMate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditDistanceMate.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
