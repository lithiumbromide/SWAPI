---
title: "GetConnectorForces2 Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetConnectorForces2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetConnectorForces2.html"
---

# GetConnectorForces2 Method (ICWResults)

Gets the x-, y-, and z-component and resultant forces, bending moments, and torques for the specified connector and step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConnectorForces2( _
   ByVal NStepNumber As System.Integer, _
   ByVal SName As System.String, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NStepNumber As System.Integer
Dim SName As System.String
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetConnectorForces2(NStepNumber, SName, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetConnectorForces2(
   System.int NStepNumber,
   System.string SName,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetConnectorForces2(
   System.int NStepNumber,
   System.String^ SName,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NStepNumber`: Solution step number (use 1 for static)
- `SName`: Name of a pin, bolt, bearing, spring, spot weld, edge weld, linkage rod connector, or link connector (see **Remarks**)
- `NUnits`: Output units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `ErrorCode`: Error code as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of 16 doubles:

- x-component of the shear force
- y-component of the shear force
- z-component of the shear force
- Resultant shear force
- x-component of the axial force
- y-component of the axial force
- z-component of the axial force
- Resultant axial force
- x-component of the bending moment
- y-component of the bending moment
- z-component of the bending moment
- Resultant bending moment
- x-component of the torque
- y-component of the torque
- z-component of the torque
- Resultant torque

## VBA Syntax

See [CWResults::GetConnectorForces2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetConnectorForces2.html).

## Examples

[Get Connector Forces, Moments, and Torques (VBA)](Get_the_Pin,_Bolt,_or_Bearing_Connector_Forces_Example_VB.htm)
[Get Connector Forces, Moments, and Torques (VB.NET)](Get_the_Pin,_Bolt,_or_Bearing_Connector_Forces_Example_VBNET.htm)
[Get Connector Forces, Moments, and Torques (C#)](Get_the_Pin,_Bolt,_or_Bearing_Connector_Forces_Example_CSharp.htm)

## Remarks

For spot welds, specify SName with the spot weld point (e.g., "Spot Welds-1/Point1").

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetConnectorForcesWithTimeValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetConnectorForcesWithTimeValue.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
