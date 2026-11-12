---
title: "SetForceComponentValues Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "SetForceComponentValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetForceComponentValues.html"
---

# SetForceComponentValues Method (ICWForce)

Obsolete. Superseded by [ICWForce::SetForceComponentValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetForceComponentValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetForceComponentValues( _
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

instance.SetForceComponentValues(B1, B2, B3, D1, D2, D3)
```

### C#

```csharp
void SetForceComponentValues(
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
void SetForceComponentValues(
   System.int B1,
   System.int B2,
   System.int B3,
   System.double D1,
   System.double D2,
   System.double D3
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

See [CWForce::SetForceComponentValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~SetForceComponentValues.html).

## Remarks

This method is valid if [ICWForce::ForceType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html) is set to [swsForceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceType_e.html).swsForceTypeForceOrMoment.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::GetForceComponentValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetForceComponentValues.html)
[ICWForce::ForceType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html)
[ICWForce::SetReferenceGeometry Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetReferenceGeometry.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
