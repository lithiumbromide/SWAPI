---
title: "GetExcitationDirections2 Method (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "GetExcitationDirections2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~GetExcitationDirections2.html"
---

# GetExcitationDirections2 Method (ICWBaseExcitation)

Gets the directions in which this excitation is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetExcitationDirections2( _
   ByRef BDir1 As System.Boolean, _
   ByRef BDir2 As System.Boolean, _
   ByRef BDir3 As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim BDir1 As System.Boolean
Dim BDir2 As System.Boolean
Dim BDir3 As System.Boolean

instance.GetExcitationDirections2(BDir1, BDir2, BDir3)
```

### C#

```csharp
void GetExcitationDirections2(
   out System.bool BDir1,
   out System.bool BDir2,
   out System.bool BDir3
)
```

### C++/CLI

```cpp
void GetExcitationDirections2(
   [Out] System.bool BDir1,
   [Out] System.bool BDir2,
   [Out] System.bool BDir3
)
```

### Parameters

- `BDir1`: -1 or true to get excitation along plane direction 1, 0 or false to not (see **Remarks**)
- `BDir2`: -1 or true to get excitation along plane direction 2, 0 or false to not (see **Remarks**)
- `BDir3`: -1 or true to get excitation along plane direction 3, 0 or false to not (see **Remarks**)

## Examples

See the [ICWBaseExcitation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html) examples.

## Remarks

For uniform base excitations, this method is valid only if you did not call [ICWBaseExcitation::SetDirectionEntityForUniformExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation~SetDirectionEntityForUniformExcitation.html) to set the face, edge, or plane in whose direction the excitation is uniformly applied.

This method returns booleans or integers in out parameters BDir1, BDir2, and BDir3, depending on their prior declarations.

If out parameters BDir1, BDir2, and BDir3 are cast as:

- Booleans, true or false is returned in each out parameter.
- Longs or integers, -1 (=true) or 0 (=false) is returned in each out parameter.

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
