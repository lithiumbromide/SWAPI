---
title: "GetReverseDirections Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "GetReverseDirections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetReverseDirections.html"
---

# GetReverseDirections Method (ICWDynamicInitialCondition)

Obsolete. Superseded by [ICWDynamicInitialCondition::GetReverseDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetReverseDirections2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetReverseDirections( _
   ByRef BVal1 As System.Integer, _
   ByRef BVal2 As System.Integer, _
   ByRef BVal3 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim BVal1 As System.Integer
Dim BVal2 As System.Integer
Dim BVal3 As System.Integer

instance.GetReverseDirections(BVal1, BVal2, BVal3)
```

### C#

```csharp
void GetReverseDirections(
   out System.int BVal1,
   out System.int BVal2,
   out System.int BVal3
)
```

### C++/CLI

```cpp
void GetReverseDirections(
   [Out] System.int BVal1,
   [Out] System.int BVal2,
   [Out] System.int BVal3
)
```

### Parameters

- `BVal1`: 1 if BDir1 of [ICWDynamicInitialCondition::GetDirections](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetDirections.html) is reversed, 0 if not
- `BVal2`: 1 if BDir2 of ICWDynamicInitialCondition::GetDirections is reversed, 0 if not
- `BVal3`: 1 if BDir3 of ICWDynamicInitialCondition::GetDirections is reversed, 0 if not

## VBA Syntax

See [CWDynamicInitialCondition::GetReverseDirections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicInitialCondition~GetReverseDirections.html).

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)
[ICWDynamicInitialCondition::SetReverseDirections Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetReverseDirections.html)
[ICWDynamicInitialCondition::SetDirectionEntity Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirectionEntity.html)
[ICWDynamicInitialCondition::GetValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetValues.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
