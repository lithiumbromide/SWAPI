---
title: "GetConnectorForcesWithTimeValue Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetConnectorForcesWithTimeValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetConnectorForcesWithTimeValue.html"
---

# GetConnectorForcesWithTimeValue Method (ICWResults)

Gets the component and resultant forces, bending moments, and torques for the specified connector at the specified time.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConnectorForcesWithTimeValue( _
   ByVal DTimeValue As System.Double, _
   ByVal SName As System.String, _
   ByVal NUnits As System.Integer, _
   ByRef DAccurateTimeValue As System.Double, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim DTimeValue As System.Double
Dim SName As System.String
Dim NUnits As System.Integer
Dim DAccurateTimeValue As System.Double
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetConnectorForcesWithTimeValue(DTimeValue, SName, NUnits, DAccurateTimeValue, ErrorCode)
```

### C#

```csharp
System.object GetConnectorForcesWithTimeValue(
   System.double DTimeValue,
   System.string SName,
   System.int NUnits,
   out System.double DAccurateTimeValue,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetConnectorForcesWithTimeValue(
   System.double DTimeValue,
   System.String^ SName,
   System.int NUnits,
   [Out] System.double DAccurateTimeValue,
   [Out] System.int ErrorCode
)
```

### Parameters

- `DTimeValue`: Time at which to get connector values
- `SName`: Name of a pin, bolt, bearing, spring, spot weld, edge weld, or link connector (see **Remarks**)
- `NUnits`: Output units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `DAccurateTimeValue`: Accurate time
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

See [CWResults::GetConnectorForcesWithTimeValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetConnectorForcesWithTimeValue.html).

## Examples

[Get Connector Forces, Moments, and Torques at a Time (VBA)](Get_Connector_Forces_at_a_Time_Example_VB.htm)
[Get Connector Forces, Moments, and Torques at a Time (VB.NET)](Get_Connector_Forces_at_a_Time_Example_VBNET.htm)
[Get Connector Forces, Moments, and Torques at a Time (C#)](Get_Connector_Forces_at_a_Time_Example_CSharp.htm)

## Remarks

For spot welds, specify SName with the spot weld point (e.g., "Spot Welds-1/Point1").

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetConnectorForces2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetConnectorForces2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
