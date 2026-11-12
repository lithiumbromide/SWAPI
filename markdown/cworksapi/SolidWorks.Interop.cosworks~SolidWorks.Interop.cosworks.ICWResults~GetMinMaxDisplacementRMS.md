---
title: "GetMinMaxDisplacementRMS Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetMinMaxDisplacementRMS"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxDisplacementRMS.html"
---

# GetMinMaxDisplacementRMS Method (ICWResults)

Gets the algebraic minimum and maximum displacement RMS values for the specified component of this random vibration study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxDisplacementRMS( _
   ByVal NComponent As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NComponent As System.Integer
Dim DispPlane As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMinMaxDisplacementRMS(NComponent, DispPlane, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetMinMaxDisplacementRMS(
   System.int NComponent,
   System.object DispPlane,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxDisplacementRMS(
   System.int NComponent,
   System.Object^ DispPlane,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NComponent`: Displacement component as defined in [swsDisplacementComponent_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDisplacementComponent_e.html)
- `DispPlane`: Plane, axis, or coordinate system; valid only if NComponent is set to a directional component; specify nothing if reference geometry does not exist
- `NUnits`: Linear units for displacement translation as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [CWResults::GetMinMaxDisplacementRMS](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetMinMaxDisplacementRMS.html).

## Remarks

This method returns the following array:

{`node_with_minimum_displacement`, `minimum_displacement`, `node_with_maximum_displacement`, `maximum_displacement`},

where the nodes are integer indexes, and the displacements are in scientific notation.

This method returns root-mean-square (RMS) values. To obtain power spectral density (PSD) values, call [ICWResults::GetMinMaxDisplacement](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxDisplacement.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetMinMaxDisplacementForHarmonic Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxDisplacementForHarmonic.html)

## Availability

SOLIDWORKS Simulation API 2015 SP1.0
