---
title: "AddForce3 Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddForce3"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddForce3.html"
---

# AddForce3 Method (ICWLoadsAndRestraintsManager)

Creates a force.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddForce3( _
   ByVal ForceType As System.Integer, _
   ByVal SelectionType As System.Integer, _
   ByVal RefDirType As System.Integer, _
   ByVal InterpolationMode As System.Integer, _
   ByVal DistPercentageOpt As System.Integer, _
   ByVal NumOfRows As System.Integer, _
   ByVal DistValue As System.Object, _
   ByVal ForceValue As System.Object, _
   ByVal NonUniformLoading As System.Boolean, _
   ByVal NULoadingOnBeam As System.Boolean, _
   ByVal NonUniformLoadDistDef As System.Integer, _
   ByVal NonUniformLoadDistType As System.Integer, _
   ByVal Ucode As System.Integer, _
   ByVal TorqueNFVal As System.Double, _
   ByVal Comps As System.Object, _
   ByVal FlipOrigin As System.Boolean, _
   ByVal IsCurvedBeam As System.Boolean, _
   ByVal DispArray As System.Object, _
   ByVal RefGeom As System.Object, _
   ByVal PerUnitLength As System.Boolean, _
   ByRef ErrorCode As System.Integer _
) As CWForce
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim ForceType As System.Integer
Dim SelectionType As System.Integer
Dim RefDirType As System.Integer
Dim InterpolationMode As System.Integer
Dim DistPercentageOpt As System.Integer
Dim NumOfRows As System.Integer
Dim DistValue As System.Object
Dim ForceValue As System.Object
Dim NonUniformLoading As System.Boolean
Dim NULoadingOnBeam As System.Boolean
Dim NonUniformLoadDistDef As System.Integer
Dim NonUniformLoadDistType As System.Integer
Dim Ucode As System.Integer
Dim TorqueNFVal As System.Double
Dim Comps As System.Object
Dim FlipOrigin As System.Boolean
Dim IsCurvedBeam As System.Boolean
Dim DispArray As System.Object
Dim RefGeom As System.Object
Dim PerUnitLength As System.Boolean
Dim ErrorCode As System.Integer
Dim value As CWForce

value = instance.AddForce3(ForceType, SelectionType, RefDirType, InterpolationMode, DistPercentageOpt, NumOfRows, DistValue, ForceValue, NonUniformLoading, NULoadingOnBeam, NonUniformLoadDistDef, NonUniformLoadDistType, Ucode, TorqueNFVal, Comps, FlipOrigin, IsCurvedBeam, DispArray, RefGeom, PerUnitLength, ErrorCode)
```

### C#

```csharp
CWForce AddForce3(
   System.int ForceType,
   System.int SelectionType,
   System.int RefDirType,
   System.int InterpolationMode,
   System.int DistPercentageOpt,
   System.int NumOfRows,
   System.object DistValue,
   System.object ForceValue,
   System.bool NonUniformLoading,
   System.bool NULoadingOnBeam,
   System.int NonUniformLoadDistDef,
   System.int NonUniformLoadDistType,
   System.int Ucode,
   System.double TorqueNFVal,
   System.object Comps,
   System.bool FlipOrigin,
   System.bool IsCurvedBeam,
   System.object DispArray,
   System.object RefGeom,
   System.bool PerUnitLength,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWForce^ AddForce3(
   System.int ForceType,
   System.int SelectionType,
   System.int RefDirType,
   System.int InterpolationMode,
   System.int DistPercentageOpt,
   System.int NumOfRows,
   System.Object^ DistValue,
   System.Object^ ForceValue,
   System.bool NonUniformLoading,
   System.bool NULoadingOnBeam,
   System.int NonUniformLoadDistDef,
   System.int NonUniformLoadDistType,
   System.int Ucode,
   System.double TorqueNFVal,
   System.Object^ Comps,
   System.bool FlipOrigin,
   System.bool IsCurvedBeam,
   System.Object^ DispArray,
   System.Object^ RefGeom,
   System.bool PerUnitLength,
   [Out] System.int ErrorCode
)
```

### Parameters

- `ForceType`: Type of force as defined in [swsForceType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsForceType_e.html) (see **Remarks**)
- `SelectionType`: Type of selection as defined in [swsSelectionType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSelectionType_e.html)
- `RefDirType`: Type of RefGeom to specify direction of this force:

  - 0 = edge
  - 1 = axis
  - 2 = face or plane
  - -1 = no direction reference

  (see **Remarks**)
- `InterpolationMode`: Interpolation mode as defined in [swsTableDrivenInterpolationType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTableDrivenInterpolationType_e.html); only used in calculation if NonUniformLoadDistDef is swsBeamNonUniformLoadDef_e.swsTableDrivenLoad
- `DistPercentageOpt`: Table-driven distribution option as defined in [swsTableDrivenDistOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTableDrivenDistOption_e.html); only used in calculation if NonUniformLoadDistDef is swsBeamNonUniformLoadDef_e.swsTableDrivenLoad
- `NumOfRows`: Number of rows for a table-driven nonuniform distribution; only used in calculation if NonUniformLoadDistDef is swsBeamNonUniformLoadDef_e.swsTableDrivenLoad
- `DistValue`: Array of the percentage or absolute distances of the forces along the beam for a table-driven nonuniform distribution; only used in calculation if NonUniformLoadDistDef is swsBeamNonUniformLoadDef_e.swsTableDrivenLoad; specify an empty array for a non-beam force
- `ForceValue`: Array of the values of the forces along the beam for a table-driven nonuniform distribution; only used in calculation if NonUniformLoadDistDef is swsBeamNonUniformLoadDef_e.swsTableDrivenLoad; specify an empty array for a non-beam force
- `NonUniformLoading`: True for nonuniform distribution, false for uniform distribution
- `NULoadingOnBeam`: True for nonuniform distribution along a beam, false for uniform distribution along a beam
- `NonUniformLoadDistDef`: Definition of nonuniform distribution along a beam as defined in [swsBeamNonUniformLoadDef_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBeamNonUniformLoadDef_e.html); valid only if NULoadingOnBeam is true
- `NonUniformLoadDistType`: Type of nonuniform distribution along a beam as defined in [swsBeamNonUniformLoadType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBeamNonUniformLoadType_e.html); valid only if NULoadingOnBeam is true
- `Ucode`: Components in Comps to use for a force in a selected direction:

  - 1 = Fx
  - 2 = Fy
  - 4 = Fz
  - 8 = Mx
  - 16 = My
  - 32 = Mz

  For combinations of forces and moments in various directions, add up the corresponding values; use 0 for a normal force

  (see **Remarks**)
- `TorqueNFVal`: Torque or normal force value; valid only if:

  - RefDirType is -1
  - ForceType is not swsForceType_e.swsForceTypeForceOrMoment

  For beams, valid only for swsBeamNonUniformLoadDef_e.swsTotalLoad or swsBeamNonUniformLoadDef_e.swsCentralLoad
- `Comps`: Array of force and moment component values; set elements to use in Ucode; for beams, valid only if NonUniformLoadDistDef is swsBeamNonUniformLoadDef_e.swsTotalLoad or swsBeamNonUniformLoadDef_e.swsCentralLoad (see **Remarks**)
- `FlipOrigin`: True to flip the beam origin, false to not; only used if NonUniformLoadDistDef is swsBeamNonUniformLoadDef_e.swsTableDrivenLoad
- `IsCurvedBeam`: True if the beam is curved, false if the beam is straight
- `DispArray`: Array of entities to which to apply this force
- `RefGeom`: Reference direction entity used to indicate the direction of force; valid only if RefDirType is not -1 (see **Remarks**)
- `PerUnitLength`: True to change the unit of the force or moment value to a per unit length, false to not; valid only if SelectionType is swsSelectionType_e.swsSelectionBeams
- `ErrorCode`: Error as defined in [swsForceError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsForceError_e.html)

### Return Value

[Force](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWForce.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddForce3](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddForce3.html).

## Examples

[Apply Loads to Beam (C#)](Apply_Loads_to_Beam_Example_CSharp.htm)
[Apply Loads to Beam (VB.NET)](Apply_Loads_to_Beam_Example_VBNET.htm)
[Apply Loads to Beam (VBA)](Apply_Loads_to_Beam_Example_VB.htm)
[Apply Table-driven Load to Multiple Beams (C#)](Apply_Table-driven_Load_to_Multiple_Beams_Example_CSharp.htm)
[Apply Table-driven Load to Multiple Beams (VB.NET)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VBNET.htm)
[Apply Table-driven Load to Multiple Beams (VBA)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VB.htm)
[Add Nonuniform Force Distribution (VBA)](Add_Force_Example_VB.htm)
[Add Nonuniform Force Distribution (VB.NET)](Add_Force_Example_VBNET.htm)
[Add Nonuniform Force Distribution (C#)](Add_Force_Example_CSharp.htm)

## Remarks

You must specify Comps with a non-empty array of non-zero elements for all ForceTypes. Use Ucode to specify which elements of the Comps array to use for forces in a selected direction.

| If ForceType = swsForceType_e ... | Then... |  |  |
| --- | --- | --- | --- |
| swsForceTypeNormal or swsForceTypeTorque | Specify: Comps with an array of six values: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0] Ucode with 0 |  |  |
| swsForceTypeForceOrMoment | If RefDirType and RefGeom specify direction reference... And the model is a... Then specify Comps with array... And Ucode with... Edge Shell or beam [ force_along_edge , moment_along_edge ] 4 to use force_along_edge 32 to use moment_along_edge 36 to use both Edge Solid [ force_along_edge ] 4 to use force_along_edge Face or plane Shell or beam [ force_along_plane_dir_1 , force_along_plane_dir_2 , force_along_normal_to_plane , moment_along_plane_dir_1 , moment_along_plane_dir_2 , moment_along_normal_to_plane ] Combinations of values corresponding to the Comps array components to use Face or plane Solid [ force_along_plane_dir_1 , force_along_plane_dir_2 , force_along_normal_to_plane ] Combinations of values corresponding to the Comps array components to use Axis Shell or beam [ force_in_radial_direction, force_in_circumferential_direction, force_along_axis, moment_in_radial_direction, moment_in_circumferential_direction, moment_along_axis ] Combinations of values corresponding to the Comps array components to use Axis Solid [ force_in_radial_direction, force_in_circumferential_direction, force_along_axis ] Combinations of values corresponding to the Comps array components to use |  |  |
| If RefDirType and RefGeom specify direction reference... | And the model is a... | Then specify Comps with array... | And Ucode with... |
| Edge | Shell or beam | [ force_along_edge , moment_along_edge ] | 4 to use force_along_edge 32 to use moment_along_edge 36 to use both |
| Edge | Solid | [ force_along_edge ] | 4 to use force_along_edge |
| Face or plane | Shell or beam | [ force_along_plane_dir_1 , force_along_plane_dir_2 , force_along_normal_to_plane , moment_along_plane_dir_1 , moment_along_plane_dir_2 , moment_along_normal_to_plane ] | Combinations of values corresponding to the Comps array components to use |
| Face or plane | Solid | [ force_along_plane_dir_1 , force_along_plane_dir_2 , force_along_normal_to_plane ] | Combinations of values corresponding to the Comps array components to use |
| Axis | Shell or beam | [ force_in_radial_direction, force_in_circumferential_direction, force_along_axis, moment_in_radial_direction, moment_in_circumferential_direction, moment_along_axis ] | Combinations of values corresponding to the Comps array components to use |
| Axis | Solid | [ force_in_radial_direction, force_in_circumferential_direction, force_along_axis ] | Combinations of values corresponding to the Comps array components to use |

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2011 SP0
