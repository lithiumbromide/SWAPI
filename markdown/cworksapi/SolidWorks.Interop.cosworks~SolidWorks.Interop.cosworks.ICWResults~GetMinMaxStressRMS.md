---
title: "GetMinMaxStressRMS Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxStressRMS"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStressRMS.html"
---

# GetMinMaxStressRMS Method (ICWResults)

Gets the algebraic minimum and maximum RMS values for the specified stress component and element of this random vibration study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxStressRMS( _
   ByVal NComponent As System.Integer, _
   ByVal NElementNumber As System.Integer, _
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
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMinMaxStressRMS(NComponent, NElementNumber, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxStressRMS(
   System.int NComponent,
   System.int NElementNumber,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxStressRMS(
   System.int NComponent,
   System.int NElementNumber,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Stress component as defined in [swsStressComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStressComponent_e.html)
- `NElementNumber`: Element number
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if reference geometry does not exist
- `NUnits`: Units as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWResults::GetMinMaxStressRMS](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMinMaxStressRMS.html).

## Remarks

This method returns the following array:

{`node_with_minimum_stress`, `minimum_stress`, `node_with_maximum_stress`, `maximum_stress`},

where the nodes are integer indexes, and the stresses are in scientific notation.

This method returns root-mean-square (RMS) values. To obtain power spectral density (PSD) values, call [ICWResults::GetMinMaxStress](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStress.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxStressForHarmonic Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxStressForHarmonic.html)

## Availability

SOLIDWORKS Simulation API 2015 SP1.0
