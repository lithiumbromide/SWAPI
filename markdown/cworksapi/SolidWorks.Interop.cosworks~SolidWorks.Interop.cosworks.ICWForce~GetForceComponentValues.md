---
title: "GetForceComponentValues Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "GetForceComponentValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetForceComponentValues.html"
---

# GetForceComponentValues Method (ICWForce)

Obsolete. Superseded by [ICWForce::GetForceComponentValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetForceComponentValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetForceComponentValues( _
   ByRef B1 As System.Integer, _
   ByRef B2 As System.Integer, _
   ByRef B3 As System.Integer, _
   ByRef D1 As System.Double, _
   ByRef D2 As System.Double, _
   ByRef D3 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim B1 As System.Integer
Dim B2 As System.Integer
Dim B3 As System.Integer
Dim D1 As System.Double
Dim D2 As System.Double
Dim D3 As System.Double

instance.GetForceComponentValues(B1, B2, B3, D1, D2, D3)
```

### C#

```csharp
void GetForceComponentValues(
   out System.int B1,
   out System.int B2,
   out System.int B3,
   out System.double D1,
   out System.double D2,
   out System.double D3
)
```

### C++/CLI

```cpp
void GetForceComponentValues(
   [Out] System.int B1,
   [Out] System.int B2,
   [Out] System.int B3,
   [Out] System.double D1,
   [Out] System.double D2,
   [Out] System.double D3
)
```

### Parameters

- `B1`: 1 if force in the X direction exists, 0 if not
- `B2`: 1 if force in the Y direction exists, 0 if not
- `B3`: 1 if force in the Z direction exists, 0 if not
- `D1`: Force in the X direction
- `D2`: Force in the Y direction
- `D3`: Force in the Z direction

## VBA Syntax

See [CWForce::GetForceComponentValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~GetForceComponentValues.html).

## Remarks

This method is valid if [ICWForce::ForceType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html) is set to [swsForceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceType_e.html).swsForceTypeForceOrMoment.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::SetForceComponentValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetForceComponentValues.html)
[ICWForce::SetReferenceGeometry Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetReferenceGeometry.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
