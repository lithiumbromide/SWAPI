---
title: "GetReverseDirections2 Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "GetReverseDirections2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetReverseDirections2.html"
---

# GetReverseDirections2 Method (ICWDynamicInitialCondition)

Gets whether the directions of this initial condition are reversed.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetReverseDirections2( _
   ByRef BVal1 As System.Boolean, _
   ByRef BVal2 As System.Boolean, _
   ByRef BVal3 As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim BVal1 As System.Boolean
Dim BVal2 As System.Boolean
Dim BVal3 As System.Boolean

instance.GetReverseDirections2(BVal1, BVal2, BVal3)
```

### C#

```csharp
void GetReverseDirections2(
   out System.bool BVal1,
   out System.bool BVal2,
   out System.bool BVal3
)
```

### C++/CLI

```cpp
void GetReverseDirections2(
   [Out] System.bool BVal1,
   [Out] System.bool BVal2,
   [Out] System.bool BVal3
)
```

### Parameters

- `BVal1`: -1 or true if BDir1 of [ICWDynamicInitialCondition::GetDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetDirections2.html) is reversed, 0 or false if not
- `BVal2`: -1 or true if BDir2 of ICWDynamicInitialCondition::GetDirections2 is reversed, 0 or false if not
- `BVal3`: -1 or true if BDir3 of ICWDynamicInitialCondition::GetDirections2 is reversed, 0 or false if not

## Examples

See the [ICWDynamicInitialCondition](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html) examples.

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
