---
title: "SetMomentComponentValues2 Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "SetMomentComponentValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetMomentComponentValues2.html"
---

# SetMomentComponentValues2 Method (ICWForce)

Sets the moment values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMomentComponentValues2( _
   ByVal B1 As System.Boolean, _
   ByVal B2 As System.Boolean, _
   ByVal B3 As System.Boolean, _
   ByVal D1 As System.Double, _
   ByVal D2 As System.Double, _
   ByVal D3 As System.Double _
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

instance.SetMomentComponentValues2(B1, B2, B3, D1, D2, D3)
```

### C#

```csharp
void SetMomentComponentValues2(
   System.bool B1,
   System.bool B2,
   System.bool B3,
   System.double D1,
   System.double D2,
   System.double D3
)
```

### C++/CLI

```cpp
void SetMomentComponentValues2(
   System.bool B1,
   System.bool B2,
   System.bool B3,
   System.double D1,
   System.double D2,
   System.double D3
)
```

### Parameters

- `B1`: -1 or true to set moment along plane dir 1, 0 or false to not (see **Remarks**)
- `B2`: -1 or true to set moment along plane dir 2, 0 or false to not (see **Remarks**)
- `B3`: -1 or true to set moment along the normal to plane, 0 or false to not (see **Remarks**)
- `D1`: Moment about plane dir 1
- `D2`: Moment about plane dir 2
- `D3`: Moment about normal to plane

## VBA Syntax

See [CWForce::SetMomentComponentValues2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~SetMomentComponentValues2.html).

## Remarks

This method is valid only for models with beam elements and if [ICWForce::ForceType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html) is set to [swsForceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceType_e.html).swsForceTypeForceOrMoment.

Specify booleans or integers in parameters B1, B2, and B3: true = -1 and false = 0.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
