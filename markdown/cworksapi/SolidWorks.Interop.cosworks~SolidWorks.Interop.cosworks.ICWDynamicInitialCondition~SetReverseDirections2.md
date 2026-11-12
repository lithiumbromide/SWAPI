---
title: "SetReverseDirections2 Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "SetReverseDirections2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetReverseDirections2.html"
---

# SetReverseDirections2 Method (ICWDynamicInitialCondition)

Sets whether the directions of this initial condition are reversed.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReverseDirections2( _
   ByVal BVal1 As System.Boolean, _
   ByVal BVal2 As System.Boolean, _
   ByVal BVal3 As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim BVal1 As System.Boolean
Dim BVal2 As System.Boolean
Dim BVal3 As System.Boolean

instance.SetReverseDirections2(BVal1, BVal2, BVal3)
```

### C#

```csharp
void SetReverseDirections2(
   System.bool BVal1,
   System.bool BVal2,
   System.bool BVal3
)
```

### C++/CLI

```cpp
void SetReverseDirections2(
   System.bool BVal1,
   System.bool BVal2,
   System.bool BVal3
)
```

### Parameters

- `BVal1`: -1 or true to reverse BDir1 of [ICWDynamicInitialCondition::GetDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetDirections2.html), 0 or false to not
- `BVal2`: -1 or true to reverse BDir2 of ICWDynamicInitialCondition::GetDirections2, 0 or false to not
- `BVal3`: -1 or true to reverse BDir3 of ICWDynamicInitialCondition::GetDirections2, 0 or false to not

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
