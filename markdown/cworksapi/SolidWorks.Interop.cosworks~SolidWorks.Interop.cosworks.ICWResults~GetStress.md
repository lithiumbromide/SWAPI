---
title: "GetStress Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetStress"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStress.html"
---

# GetStress Method (ICWResults)

Gets the stress results for all nodes or elements at the specified solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStress( _
   ByVal NElementNumber As System.Integer, _
   ByVal NStepNum As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NElementNumber As System.Integer
Dim NStepNum As System.Integer
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetStress(NElementNumber, NStepNum, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetStress(
   System.int NElementNumber,
   System.int NStepNum,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetStress(
   System.int NElementNumber,
   System.int NStepNum,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NElementNumber`: Element number:

  - 0 = Nodal
  - 1 = Elemental
- `NStepNum`: Solution step number (use 1 for static)
- `DispPlane`: Reference geometry
- `NUnits`: Unit as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of stress results

## VBA Syntax

See [CWResults::GetStress](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetStress.html).

## Remarks

Sx, Sy, Sz, Txy, Tyz, Txz, P1, P2, P3, VON, and INT for all nodes or elements at the specified step number.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxStress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStress.html)
[ICWResults::GetStressComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressComponentForAllStepsAtNode.html)
[ICWResults::GetStressForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressForEntities.html)
[ICWResults::GetStressTensorValuesForAllNodesOfElement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressTensorValuesForAllNodesOfElement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
