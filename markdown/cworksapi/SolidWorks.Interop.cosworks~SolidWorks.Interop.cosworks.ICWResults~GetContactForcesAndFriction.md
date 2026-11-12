---
title: "GetContactForcesAndFriction Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetContactForcesAndFriction"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetContactForcesAndFriction.html"
---

# GetContactForcesAndFriction Method (ICWResults)

Gets the specified contact or friction forces for the specified entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetContactForcesAndFriction( _
   ByVal NStepNumber As System.Integer, _
   ByVal DispPlane As System.Object, _
   ByVal ArraySelectedEntities As System.Object, _
   ByVal NForceType As System.Integer, _
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
Dim NForceType As System.Integer
Dim NUnits As System.Integer
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetContactForcesAndFriction(NStepNumber, DispPlane, ArraySelectedEntities, NForceType, NUnits, ErrorCode)
```

### C#

```csharp
System.object GetContactForcesAndFriction(
   System.int NStepNumber,
   System.object DispPlane,
   System.object ArraySelectedEntities,
   System.int NForceType,
   System.int NUnits,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetContactForcesAndFriction(
   System.int NStepNumber,
   System.Object^ DispPlane,
   System.Object^ ArraySelectedEntities,
   System.int NForceType,
   System.int NUnits,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NStepNumber`: Solution step number at which to calculate the contact forces for non-linear and drop test studies; 1 for static studies
- `DispPlane`: Plane, axis, or coordinate system relative to which the contact forces are calculated
- `ArraySelectedEntities`: Array of entities for which to calculate contact forces
- `NForceType`: Type of contact force as defined in [swsNForceType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNForceType_e.html)
- `NUnits`: Units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of four doubles of the contact forces for all selections in ArraySelectedEntities:

1. Summation of x-components of contact forces
2. Summation of y-components of contact forces
3. Summation of z-components of contact forces
4. Resultant contact force

## VBA Syntax

See [CWResults::GetContactForcesAndFriction](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetContactForcesAndFriction.html).

## Examples

[Get Contact or Friction Forces (VBA)](Get_Normal_Contact_Friction_Force_Example_VB.htm)
[Get Contact or Friction Forces (VB.NET)](Get_Normal_Contact_Friction_Force_Example_VBNET.htm)
[Get Contact or Friction Forces (C#)](Get_Normal_Contact_Friction_Force_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2013 SP0
