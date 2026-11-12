---
title: "SetForceComponentValues2 Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "SetForceComponentValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetForceComponentValues2.html"
---

# SetForceComponentValues2 Method (ICWForce)

Sets the force component values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetForceComponentValues2( _
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

instance.SetForceComponentValues2(B1, B2, B3, D1, D2, D3)
```

### C#

```csharp
void SetForceComponentValues2(
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
void SetForceComponentValues2(
   System.bool B1,
   System.bool B2,
   System.bool B3,
   System.double D1,
   System.double D2,
   System.double D3
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

See [CWForce::SetForceComponentValues2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~SetForceComponentValues2.html).

## Remarks

This method is valid if [ICWForce::ForceType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html) is set to [swsForceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceType_e.html).swsForceTypeForceOrMoment.

Specify booleans or integers in parameters B1, B2, and B3: true = -1 and false = 0.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
