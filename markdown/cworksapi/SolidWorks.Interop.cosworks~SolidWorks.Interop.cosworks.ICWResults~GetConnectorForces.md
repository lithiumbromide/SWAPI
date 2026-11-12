---
title: "GetConnectorForces Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetConnectorForces"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetConnectorForces.html"
---

# GetConnectorForces Method (ICWResults)

Obsolete. Superseded by [ICWResults::GetConnectorForces2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWResults~GetConnectorForces2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConnectorForces( _
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

value = instance.GetConnectorForces(NStepNumber, SName, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetConnectorForces(
   System.int NStepNumber,
   System.string SName,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetConnectorForces(
   System.int NStepNumber,
   System.String^ SName,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NStepNumber`: Solution step number (use 1 for static)
- `SName`: Name of a pin, bolt, or bearing connector
- `NUnits`: Output units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of twelve doubles of the connector forces:

- x-component of the shear force
- y-component of the shear force
- z-component of the shear force
- Resultant shear force
- x-component of the axial force
- y-component of the axial force
- z-component of the axial force
- Resultant axial force
- x-component of the torsional moment
- y-component of the torsional moment
- z-component of the torsional moment
- Resultant torsional moment

## VBA Syntax

See [CWResults::GetConnectorForces](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetConnectorForces.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2013 SP0
