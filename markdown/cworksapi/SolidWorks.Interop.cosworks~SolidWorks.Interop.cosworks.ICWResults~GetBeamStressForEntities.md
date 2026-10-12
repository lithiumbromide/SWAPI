---
title: "GetBeamStressForEntities Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetBeamStressForEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamStressForEntities.html"
---

# GetBeamStressForEntities Method (ICWResults)

Gets the stress values for the specified type of stress for the selected beams.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBeamStressForEntities( _
   ByVal NComponent As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim NStepNumber As System.Integer
Dim ArraySelectedEntities As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetBeamStressForEntities(NComponent, NStepNumber, ArraySelectedEntities, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetBeamStressForEntities(
   System.int NComponent,
   System.int NStepNumber,
   System.object ArraySelectedEntities,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetBeamStressForEntities(
   System.int NComponent,
   System.int NStepNumber,
   System.Object^ ArraySelectedEntities,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Type of stress as defined in [swsBeamStressType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBeamStressType_e.html)
- `NStepNumber`: Number of steps to complete a non-linear analysis; otherwise, value is 1
- `ArraySelectedEntities`: Selected [beams](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamBody.html)
- `NUnits`: Unit as defined by [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `ErrorCode`: Error as defined by [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of the stress values for the specified type of stress for the elements of the selected beams. Every element has two ends, so the output is as follows:

- Beam element number
- End1 stress
- End2 stress
- Beam element number
- End1 stress
- End2 stress
- etc.

## VBA Syntax

See [CWResults::GetBeamStressForEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetBeamStressForEntities.html)

## Examples

[Get Forces and Stresses for Selected Beams (VBA)](Get_Forces_for_Selected_Beams_Example_VB.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetBeamForcesForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamForcesForEntities.html)
[ICWResults::GetBeamMinMaxStress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamMinMaxStress.html)
[ICWResults::GetBeamRadius Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBeamRadius.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
