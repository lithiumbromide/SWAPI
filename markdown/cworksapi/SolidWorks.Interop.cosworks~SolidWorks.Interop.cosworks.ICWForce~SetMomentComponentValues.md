---
title: "SetMomentComponentValues Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "SetMomentComponentValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetMomentComponentValues.html"
---

# SetMomentComponentValues Method (ICWForce)

Obsolete. Superseded by [ICWForce::SetMomentComponentValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetMomentComponentValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMomentComponentValues( _
   ByVal B1 As System.Integer, _
   ByVal B2 As System.Integer, _
   ByVal B3 As System.Integer, _
   ByVal D1 As System.Double, _
   ByVal D2 As System.Double, _
   ByVal D3 As System.Double _
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

instance.SetMomentComponentValues(B1, B2, B3, D1, D2, D3)
```

### C#

```csharp
void SetMomentComponentValues(
   System.int B1,
   System.int B2,
   System.int B3,
   System.double D1,
   System.double D2,
   System.double D3
)
```

### C++/CLI

```cpp
void SetMomentComponentValues(
   System.int B1,
   System.int B2,
   System.int B3,
   System.double D1,
   System.double D2,
   System.double D3
)
```

### Parameters

- `B1`: 1 to set moment along plane dir 1, 0 to not
- `B2`: 1 to set moment along plane dir 2, 0 to not
- `B3`: 1 to set moment along the normal to plane, 0 to not
- `D1`: Moment about plane dir 1
- `D2`: Moment about plane dir 2
- `D3`: Moment about normal to plane

## VBA Syntax

See [CWForce::SetMomentComponentValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~SetMomentComponentValues.html).

## Remarks

This method is valid only for models with beam elements and if [ICWForce::ForceType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html) is set to [swsForceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceType_e.html).swsForceTypeForceOrMoment.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::GetMomentComponentValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetMomentComponentValues.html)
[ICWForce::SetReferenceGeometry Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetReferenceGeometry.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
