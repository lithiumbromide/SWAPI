---
title: "AddCyclicSymmetryRestraint Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddCyclicSymmetryRestraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddCyclicSymmetryRestraint.html"
---

# AddCyclicSymmetryRestraint Method (ICWLoadsAndRestraintsManager)

Adds a cyclic symmetry restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCyclicSymmetryRestraint( _
   ByVal FirstFace As System.Object, _
   ByVal SecondFace As System.Object, _
   ByVal Axis As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWRestraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim FirstFace As System.Object
Dim SecondFace As System.Object
Dim Axis As System.Object
Dim ErrorCode As System.Integer
Dim value As CWRestraint

value = instance.AddCyclicSymmetryRestraint(FirstFace, SecondFace, Axis, ErrorCode)
```

### C#

```csharp
CWRestraint AddCyclicSymmetryRestraint(
   System.object FirstFace,
   System.object SecondFace,
   System.object Axis,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWRestraint^ AddCyclicSymmetryRestraint(
   System.Object^ FirstFace,
   System.Object^ SecondFace,
   System.Object^ Axis,
   [Out] System.int ErrorCode
)
```

### Parameters

- `FirstFace`: First face (see **Remarks**)
- `SecondFace`: Second face (see **Remarks**)
- `Axis`: Axis of revolution (see **Remarks**)
- `ErrorCode`: Error code as defined in [swsCyclicRestraintError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCyclicRestraintError_e.html)

### Return Value

[ICWRestraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRestraint.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddCyclicSymmetryRestraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddCyclicSymmetryRestraint.html).

## Examples

[Add Cyclic Symmetry Restraint (VBA)](Add_Cyclic_Symmetry_Restraint_Example_VB.htm)
[Add Cyclic Symmetry Restraint (VB.NET)](Add_Cyclic_Symmetry_Restraint_Example_VBNET.htm)
[Add Cyclic Symmetry Restraint (C#)](Add_Cyclic_Symmetry_Restraint_Example_CSharp.htm)

## Remarks

The cyclic symmetry fixture is appropriate for turbines, fans, flywheels, and motor rotors. FirstFace and SecondFace are the faces of a cut section of a model that can be repeated in a cyclical pattern about Axis. The angle between FirstFace and SecondFace should be evenly divisible by 360. You cannot apply a cyclic symmetry restraint to an invalid section. See the **Creating Valid Sections for Cyclic Symmetry** topic in the SOLIDWORKS Simulation Helps for more information.

This method is valid only for static and nonlinear studies.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
