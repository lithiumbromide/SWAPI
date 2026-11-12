---
title: "GetMomentComponentValues Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "GetMomentComponentValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetMomentComponentValues.html"
---

# GetMomentComponentValues Method (ICWForce)

Obsolete. Superseded by [ICWForce::GetMomentComponentValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetMomentComponentValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetMomentComponentValues( _
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

instance.GetMomentComponentValues(B1, B2, B3, D1, D2, D3)
```

### C#

```csharp
void GetMomentComponentValues(
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
void GetMomentComponentValues(
   [Out] System.int B1,
   [Out] System.int B2,
   [Out] System.int B3,
   [Out] System.double D1,
   [Out] System.double D2,
   [Out] System.double D3
)
```

### Parameters

- `B1`: 1 if moment about the X direction exists, 0 if not
- `B2`: 1 if moment about the Y direction exists, 0 if not
- `B3`: 1 if moment about the Z direction exists, 0 if not
- `D1`: Moment about X
- `D2`: Moment about Y
- `D3`: Moment about Z

## VBA Syntax

See [CWForce::GetMomentComponentValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~GetMomentComponentValues.html).

## Remarks

This method is valid only for models with beam elements and if [ICWForce::ForceType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html) is set to [swsForceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceType_e.html).swsForceTypeForceOrMoment.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::SetMomentComponentValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetMomentComponentValues.html)
[ICWForce::ForceType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html)
[ICWForce::SetReferenceGeometry Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetReferenceGeometry.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
