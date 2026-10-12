---
title: "SetExcitationDirectionValues Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "SetExcitationDirectionValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationDirectionValues.html"
---

# SetExcitationDirectionValues Method (ICWBaseExcitation)

Sets the excitation direction values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetExcitationDirectionValues( _
   ByVal DVal1 As System.Double, _
   ByVal DVal2 As System.Double, _
   ByVal DVal3 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim DVal1 As System.Double
Dim DVal2 As System.Double
Dim DVal3 As System.Double

instance.SetExcitationDirectionValues(DVal1, DVal2, DVal3)
```

### C#

```csharp
void SetExcitationDirectionValues(
   System.double DVal1,
   System.double DVal2,
   System.double DVal3
)
```

### C++/CLI

```cpp
void SetExcitationDirectionValues(
   System.double DVal1,
   System.double DVal2,
   System.double DVal3
)
```

### Parameters

- `DVal1`: Excitation along plane direction 1 (see **Remarks**)
- `DVal2`: Excitation along plane direction 2 (see **Remarks**)
- `DVal3`: Excitation along plane direction 3 (see **Remarks**)

## VBA Syntax

See [CWBaseExcitation::SetExcitationDirectionValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~SetExcitationDirectionValues.html).

## Remarks

For uniform base excitations, you can specify the direction of excitation by calling either:

- this method, [ICWBaseExcitation::SetExcitationDirections](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetExcitationDirections.html), and [ICWBaseExcitation::SetExcitationReverseDirections](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationReverseDirections.html) to explicitly specify the excitation direction components and values

- or -

- [ICWBaseExcitation::SetDirectionEntityForUniformExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetDirectionEntityForUniformExcitation.html) to specify the face, edge, or plane in whose direction the excitation is uniformly applied.

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)
[ICWBaseExcitation::GetExcitationDirectionValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationDirectionValues.html)
[ICWBaseExcitation::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~Unit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
