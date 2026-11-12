---
title: "AddPrescribedDisplacement Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddPrescribedDisplacement"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddPrescribedDisplacement.html"
---

# AddPrescribedDisplacement Method (ICWLoadsAndRestraintsManager)

Applies the specified prescribed displacement to the specified geometric entities to create a fixture.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPrescribedDisplacement( _
   ByVal Displacements As System.Object, _
   ByVal NLengthUnit As System.Integer, _
   ByVal DispArray As System.Object, _
   ByVal RefGeom As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWRestraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim Displacements As System.Object
Dim NLengthUnit As System.Integer
Dim DispArray As System.Object
Dim RefGeom As System.Object
Dim ErrorCode As System.Integer
Dim value As CWRestraint

value = instance.AddPrescribedDisplacement(Displacements, NLengthUnit, DispArray, RefGeom, ErrorCode)
```

### C#

```csharp
CWRestraint AddPrescribedDisplacement(
   System.object Displacements,
   System.int NLengthUnit,
   System.object DispArray,
   System.object RefGeom,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWRestraint^ AddPrescribedDisplacement(
   System.Object^ Displacements,
   System.int NLengthUnit,
   System.Object^ DispArray,
   System.Object^ RefGeom,
   [Out] System.int ErrorCode
)
```

### Parameters

- `Displacements`: Array: [`disp_x_coord`, `disp_y_coord`, `disp_z_coord`, `x_bool`, `y_bool`, `z_bool`]

  where:

  | Array Element | Value | Description |
  | --- | --- | --- |
  | disp_x_coord | Double | Prescribed displacement in the x direction |
  | disp_y_coord | Double | Prescribed displacement in the y direction |
  | disp_z_coord | Double | Prescribed displacement in the z direction |
  | x_bool | 0 or 1 | Whether to use disp_x_coord (1 to use , 0 to not) |
  | y_bool | 0 or 1 | Whether to use disp_y_coord (1 to use , 0 to not) |
  | z_bool | 0 or 1 | Whether to use disp_z_coord (1 to use , 0 to not) |

  (see **Remarks**)
- `NLengthUnit`: Units of length as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)
- `DispArray`: Array of entities to which to apply the prescribed displacement specified in Displacements
- `RefGeom`: Reference entity for prescribed displacement direction
- `ErrorCode`: Error code as defined in [swsRestraintError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRestraintError_e.html)

### Return Value

[ICWRestraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddPrescribedDisplacement](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddPinConnector.html).

## Examples

[Add Prescribed Displacement (VBA)](Add_Prescribed_Displacement_Example_VB.htm)
[Add Prescribed Displacement (VB.NET)](Add_Prescribed_Displacement_Example_VBNET.htm)
[Add Prescribed Displacement (C#)](Add_Prescribed_Displacement_Example_CSharp.htm)

## Remarks

The Displacements parameter specifies:

- length for reference geometry or flat faces

- or -

- angle of rotation for cylindrical or spherical faces

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
