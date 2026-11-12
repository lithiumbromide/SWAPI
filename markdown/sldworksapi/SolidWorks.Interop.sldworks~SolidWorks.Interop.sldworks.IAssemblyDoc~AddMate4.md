---
title: "AddMate4 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddMate4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate4.html"
---

# AddMate4 Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::AddMate5.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddMate5.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMate4( _
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
Dim ErrorStatus As System.Integer
Dim value As Mate2

value = instance.AddMate4(MateTypeFromEnum, AlignFromEnum, Flip, Distance, DistanceAbsUpperLimit, DistanceAbsLowerLimit, GearRatioNumerator, GearRatioDenominator, Angle, AngleAbsUpperLimit, AngleAbsLowerLimit, ForPositioningOnly, LockRotation, ErrorStatus)
```

### C#

```csharp
Mate2 AddMate4(
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
   out System.int ErrorStatus
)
```

### C++/CLI

```cpp
Mate2^ AddMate4(
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
   [Out] System.int ErrorStatus
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MateTypeFromEnum`: Type of mate as defined in [swMateType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateType_e.html) (see **Remarks**)
- `AlignFromEnum`: Type of alignment as defined in [swMateAlign_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateAlign_e.html)
- `Flip`: True to flip the component, false otherwise
- `Distance`: Distance value to use with distance or limit mates
- `DistanceAbsUpperLimit`: Absolute maximum distance value (see **Remarks**)
- `DistanceAbsLowerLimit`: Absolute minimum distance value (see **Remarks**)
- `GearRatioNumerator`: Gear ratio numerator value for gear mates
- `GearRatioDenominator`: Gear ratio denominator value for gear mates
- `Angle`: Angle value to use with angle mates
- `AngleAbsUpperLimit`: Absolute maximum angle value
- `AngleAbsLowerLimit`: Absolute minimum angle value
- `ForPositioningOnly`: True to only position the components according to the mating relationship and not return a mate, false to return a mate
- `LockRotation`: True to lock component rotation, false to not
- `ErrorStatus`: Success or error as defined by [swAddMateError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

## VBA Syntax

See [AssemblyDoc::AddMate4](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddMate4.html).

## Remarks

The difference between this method and the now obsolete IAssemblyDoc::AddMate3 is that this method's LockRotation parameter provides the option to lock the rotation of components in the mate.

To specify a distance mate without limits, set the DistanceAbsUpperLimit and DistanceAbsLowerLimit parameters equal to the Distance parameter.

If MateTypeFromEnum is swMateType_e.swMateDISTANCE or swMateType_e.swMateANGLE, and the mate is applied to the closest position that meets the mate condition specified by Distance or Angle, then setting Flip to true moves the assembly to the other possible mate position.

To add a mate:

1. Call [IModelDoc2::ClearSelection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ClearSelection2.html) before selecting entities to mate.
2. Call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select each entity to mate.

  | If MateTypeFromEnum is... | Use selection mark... |
  | --- | --- |
  | swMateType_e.swMateCAMFOLLOWER | 8 |
  | swMateType_e.swMateWIDTH | 16 |
  | Other swMateType_e option | 1 |
3. Call this method.
4. Call IModelDoc2::ClearSelection2 after the mate is created.

If nothing is preselected, then ErrorStatus is swAddMateError_IncorrectSelections, and nothing is returned.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
