---
title: "GetMomentComponentValues2 Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "GetMomentComponentValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetMomentComponentValues2.html"
---

# GetMomentComponentValues2 Method (ICWForce)

Gets the moment values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetMomentComponentValues2( _
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

instance.GetMomentComponentValues2(B1, B2, B3, D1, D2, D3)
```

### C#

```csharp
void GetMomentComponentValues2(
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
void GetMomentComponentValues2(
   [Out] System.bool B1,
   [Out] System.bool B2,
   [Out] System.bool B3,
   [Out] System.double D1,
   [Out] System.double D2,
   [Out] System.double D3
)
```

### Parameters

- `B1`: -1 or true if moment about the X direction exists, 0 or false if not (see **Remarks**)
- `B2`: -1 or true if moment about the Y direction exists, 0 or false if not (see **Remarks**)
- `B3`: -1 or true if moment about the Z direction exists, 0 or false if not (see **Remarks**)
- `D1`: Moment about X
- `D2`: Moment about Y
- `D3`: Moment about Z

## VBA Syntax

See [CWForce::GetMomentComponentValues2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~GetMomentComponentValues2.html).

## Remarks

This method is valid only for models with beam elements and if [ICWForce::ForceType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html) is set to [swsForceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceType_e.html).swsForceTypeForceOrMoment.

This method returns booleans or integers in out parameters B1, B2, and B3, depending on their prior declarations.

If out parameters B1, B2, and B3 are cast as:

- Booleans, true or false is returned in each out parameter.
- Longs or integers, -1 (=true) or 0 (=false) is returned in each out parameter.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
