---
title: "SetCableParams Method (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "SetCableParams"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~SetCableParams.html"
---

# SetCableParams Method (ICWCable)

Sets the specified cable parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCableParams( _
   ByVal DDiameter As System.Double, _
   ByVal DSafeAxialStrength As System.Double, _
   ByVal DTensionPreLoadForce As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable
Dim DDiameter As System.Double
Dim DSafeAxialStrength As System.Double
Dim DTensionPreLoadForce As System.Double

instance.SetCableParams(DDiameter, DSafeAxialStrength, DTensionPreLoadForce)
```

### C#

```csharp
void SetCableParams(
   System.double DDiameter,
   System.double DSafeAxialStrength,
   System.double DTensionPreLoadForce
)
```

### C++/CLI

```cpp
void SetCableParams(
   System.double DDiameter,
   System.double DSafeAxialStrength,
   System.double DTensionPreLoadForce
)
```

### Parameters

- `DDiameter`: 0 <= Cable diameter (meters in SI units) <= 1000000000000000042420637374017961984
- `DSafeAxialStrength`: 0 <= Safe axial strength (Newtons/meter^2 in SI units) <= 1000000000000000042420637374017961984
- `DTensionPreLoadForce`: 0 <= Tension pre-load force (Newtons in SI units) <= 1000000000000000042420637374017961984

## VBA Syntax

See [CWCable::SetCableParams](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~SetCableParams.html).

## Examples

See the [ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html) example.

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
