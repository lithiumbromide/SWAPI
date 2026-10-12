---
title: "GetForceComponentValues2 Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "GetForceComponentValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetForceComponentValues2.html"
---

# GetForceComponentValues2 Method (ICWForce)

Gets the force component values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetForceComponentValues2( _
   ByRef B1 As System.Boolean, _
   ByRef B2 As System.Boolean, _
   ByRef B3 As System.Boolean, _
   ByRef D1 As System.Double, _
   ByRef D2 As System.Double, _
   ByRef D3 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim B1 As System.Boolean
Dim B2 As System.Boolean
Dim B3 As System.Boolean
Dim D1 As System.Double
Dim D2 As System.Double
Dim D3 As System.Double

instance.GetForceComponentValues2(B1, B2, B3, D1, D2, D3)
```

### C#

```csharp
void GetForceComponentValues2(
   out System.bool B1,
   out System.bool B2,
   out System.bool B3,
   out System.double D1,
   out System.double D2,
   out System.double D3
)
```

### C++/CLI

```cpp
void GetForceComponentValues2(
   [Out] System.bool B1,
   [Out] System.bool B2,
   [Out] System.bool B3,
   [Out] System.double D1,
   [Out] System.double D2,
   [Out] System.double D3
)
```

### Parameters

- `B1`: -1 or true if force in the X direction exists, 0 or false if not (see **Remarks**)
- `B2`: -1 or true if force in the Y direction exists, 0 or false if not (see **Remarks**)
- `B3`: -1 or true if force in the Z direction exists, 0 or false if not (see **Remarks**)
- `D1`: Force in the X direction
- `D2`: Force in the Y direction
- `D3`: Force in the Z direction

## VBA Syntax

See [CWForce::GetForceComponentValues2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~GetForceComponentValues2.html).

## Remarks

This method is valid if [ICWForce::ForceType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html) is set to [swsForceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceType_e.html).swsForceTypeForceOrMoment.

This method returns booleans or integers in out parameters B1, B2, and B3, depending on their prior declarations.

If out parameters B1, B2, and B3 are cast as:

- Booleans, true or false is returned in each out parameter.
- Longs or integers, -1 (=true) or 0 (=false) is returned in each out parameter.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
