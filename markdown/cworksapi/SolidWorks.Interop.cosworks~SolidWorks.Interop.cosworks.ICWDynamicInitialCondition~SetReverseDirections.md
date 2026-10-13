---
title: "SetReverseDirections Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "SetReverseDirections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetReverseDirections.html"
---

# SetReverseDirections Method (ICWDynamicInitialCondition)

Obsolete. Superseded by [ICWDynamicInitialCondition::SetReverseDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetReverseDirections.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReverseDirections( _
   ByVal BVal1 As System.Integer, _
   ByVal BVal2 As System.Integer, _
   ByVal BVal3 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim BVal1 As System.Integer
Dim BVal2 As System.Integer
Dim BVal3 As System.Integer

instance.SetReverseDirections(BVal1, BVal2, BVal3)
```

### C#

```csharp
void SetReverseDirections(
   System.int BVal1,
   System.int BVal2,
   System.int BVal3
)
```

### C++/CLI

```cpp
void SetReverseDirections(
   System.int BVal1,
   System.int BVal2,
   System.int BVal3
)
```

### Parameters

- `BVal1`: 1 to reverse BDir1 of [ICWDynamicInitialCondition::GetDirections](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetDirections.html), 0 to not
- `BVal2`: 1 to reverse BDir2 of ICWDynamicInitialCondition::GetDirections, 0 to not
- `BVal3`: 1 to reverse BDir3 of ICWDynamicInitialCondition::GetDirections, 0 to not

## VBA Syntax

See [CWDynamicInitialCondition::SetReverseDirections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicInitialCondition~SetReverseDirections.html).

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)
[ICWDynamicInitialCondition::GetReverseDirections Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetReverseDirections.html)
[ICWDynamicInitialCondition::SetDirectionEntity Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirectionEntity.html)
[ICWDynamicInitialCondition::SetDirections Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirections.html)
[ICWDynamicInitialCondition::SetValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetValues.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
