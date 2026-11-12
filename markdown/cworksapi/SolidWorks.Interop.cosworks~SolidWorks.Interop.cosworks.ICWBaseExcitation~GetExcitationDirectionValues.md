---
title: "GetExcitationDirectionValues Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "GetExcitationDirectionValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationDirectionValues.html"
---

# GetExcitationDirectionValues Method (ICWBaseExcitation)

Gets the excitation values in each direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetExcitationDirectionValues( _
   ByRef DVal1 As System.Double, _
   ByRef DVal2 As System.Double, _
   ByRef DVal3 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim DVal1 As System.Double
Dim DVal2 As System.Double
Dim DVal3 As System.Double

instance.GetExcitationDirectionValues(DVal1, DVal2, DVal3)
```

### C#

```csharp
void GetExcitationDirectionValues(
   out System.double DVal1,
   out System.double DVal2,
   out System.double DVal3
)
```

### C++/CLI

```cpp
void GetExcitationDirectionValues(
   [Out] System.double DVal1,
   [Out] System.double DVal2,
   [Out] System.double DVal3
)
```

### Parameters

- `DVal1`: Excitation along plane direction 1; valid only if BDir1 = 1 in [ICWBaseExcitation::GetExcitationDirections](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~GetExcitationDirections.html) (see **Remarks**)
- `DVal2`: Excitation along plane direction 2; valid only if BDir2 = 1 in [ICWBaseExcitation::GetExcitationDirections](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~GetExcitationDirections.html) (see **Remarks**)
- `DVal3`: Excitation along plane direction 3; valid only if BDir3 = 1 in [ICWBaseExcitation::GetExcitationDirections](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~GetExcitationDirections.html) (see **Remarks**)

## VBA Syntax

See [CWBaseExcitation::GetExcitationDirectionValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~GetExcitationDirectionValues.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## Remarks

For uniform base excitations, this method is valid only if you did not call [ICWBaseExcitation::SetDirectionEntityForUniformExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetDirectionEntityForUniformExcitation.html) to set the face, edge, or plane in whose direction the excitation is uniformly applied.

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)
[ICWBaseExcitation::SetExcitationDirectionValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~SetExcitationDirectionValues.html)
[ICWBaseExcitation::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~Unit.html)
[ICWBaseExcitation::GetExcitationReverseDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationReverseDirections.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
