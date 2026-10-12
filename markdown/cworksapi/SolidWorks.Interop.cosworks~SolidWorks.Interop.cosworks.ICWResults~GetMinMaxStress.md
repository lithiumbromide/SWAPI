---
title: "GetMinMaxStress Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxStress"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStress.html"
---

# GetMinMaxStress Method (ICWResults)

Gets the algebraic minimum and maximum for the specified stress component, element, and solution step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxStress( _
   ByVal NComponent As System.Integer, _
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
Dim NComponent As System.Integer
Dim NElementNumber As System.Integer
Dim NStepNum As System.Integer
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMinMaxStress(NComponent, NElementNumber, NStepNum, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxStress(
   System.int NComponent,
   System.int NElementNumber,
   System.int NStepNum,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxStress(
   System.int NComponent,
   System.int NElementNumber,
   System.int NStepNum,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Stress component as defined in [swsStressComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStressComponent_e.html)
- `NElementNumber`: Element number
- `NStepNum`: Solution step number (use 1 for static)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if reference geometry does not exist
- `NUnits`: Units as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWResults::GetMinMaxStress](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMinMaxStress.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Create Drop Test Study (VBA)](Create_Drop_Test_Study_Example_VB.htm)
[Create Drop Test Study (VB.NET)](Create_Drop_Test_Study_Example_VBNET.htm)
[Create Drop Test Study (C#)](Create_Drop_Test_Study_Example_CSharp.htm)

## Remarks

This method returns the following array:

{`node_with_minimum_stress`, `minimum_stress`, `node_with_maximum_stress`, `maximum_stress`},

where the nodes are integer indexes, and the stresses are in scientific notation.

For random vibration studies, this method returns power spectral density (PSD) values. To obtain root-mean-square (RMS) values in random vibration studies, call [ICWResults::GetMinMaxStressRMS](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStressRMS.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetStress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStress.html)
[ICWResults::GetStressComponentForAllStepsAtNode Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressComponentForAllStepsAtNode.html)
[ICWResults::GetStressForEntities Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressForEntities.html)
[ICWResults::GetMinMaxStressForHarmonic Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStressForHarmonic.html)
[ICWResults::GetStressTensorValuesForAllNodesOfElement Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetStressTensorValuesForAllNodesOfElement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
