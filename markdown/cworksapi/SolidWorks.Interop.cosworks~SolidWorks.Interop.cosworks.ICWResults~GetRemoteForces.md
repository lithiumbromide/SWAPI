---
title: "GetRemoteForces Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetRemoteForces"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetRemoteForces.html"
---

# GetRemoteForces Method (ICWResults)

Gets the x-, y-, and z-component and resultant forces applied to selected entities as a result of transferring a remote load in static studies.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRemoteForces( _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NUnits As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NStepNumber As System.Integer
Dim DispPlane As System.Object
Dim ArraySelectedEntities As System.Object
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetRemoteForces(NStepNumber, DispPlane, ArraySelectedEntities, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetRemoteForces(
   System.int NStepNumber,
   System.object DispPlane,
   System.object ArraySelectedEntities,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetRemoteForces(
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.Object^ ArraySelectedEntities,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NStepNumber`: Solution step number (use 1 for static)
- `DispPlane`: Plane, axis, or coordinate system relative to which the results are listed
- `ArraySelectedEntities`: Selected faces, edges (shells only), vertices, and components
- `NUnits`: Output units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of four doubles of the remote load forces for all selections in ArraySelectedEntities:

1. Summation of x-components of remote load forces for all selections
2. Summation of y-components of remote load forces for all selections
3. Summation of z-components of remote load forces for all selections
4. Resultant remote load force for all selections

## VBA Syntax

See [CWResults::GetRemoteForces](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetRemoteForces.html).

## Examples

[Get Remote Load Forces (VBA)](Get_Remote_Load_Forces_Example_VB.htm)
[Get Remote Load Forces (VB.NET)](Get_Remote_Load_Forces_Example_VBNET.htm)
[Get Remote Load Forces (C#)](Get_Remote_Load_Forces_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2013 SP0
