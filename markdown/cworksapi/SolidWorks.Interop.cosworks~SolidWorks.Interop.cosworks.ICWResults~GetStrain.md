---
title: "GetStrain Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetStrain"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrain.html"
---

# GetStrain Method (ICWResults)

Gets the strain results for all nodes or elements at the specified solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStrain( _
   ByVal NElementNumber As System.Integer, _
   ByVal NStepNum As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NElementNumber As System.Integer
Dim NStepNum As System.Integer
Dim DispPlane As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetStrain(NElementNumber, NStepNum, DispPlane, ErrorCode)
```

### C#

```csharp
System.object GetStrain(
   System.int NElementNumber,
   System.int NStepNum,
   System.object DispPlane,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetStrain(
   System.int NElementNumber,
   System.int NStepNum,
   System.Object^ DispPlane,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NElementNumber`: Element number:

  - 0 = Nodal
  - 1 = Elemental
- `NStepNum`: Solution step number (use 1 for static)
- `DispPlane`: Reference geometry
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of strain results

## VBA Syntax

See [CWResults::GetStrain](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetStrain.html).

## Remarks

EPSx, EPSy, EPSz, GMxy, GMyz, GMxz, ESTRN, SEDENS, ENERGY, E1, E2, and E3 for all nodes or elements at NStepNum.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetStrainComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrainComponentForAllStepsAtNode.html)
[ICWResults::GetStrainForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStrainForEntities.html)
[ICWResults::GetMinMaxStrain Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStrain.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
