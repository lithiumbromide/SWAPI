---
title: "SetInfiniteLifeSettings2 Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "SetInfiniteLifeSettings2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~SetInfiniteLifeSettings2.html"
---

# SetInfiniteLifeSettings2 Method (ICWFatigueStudyOptions)

Sets the infinite life settings of the fatigue study.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetInfiniteLifeSettings2( _
   ByVal BChecked As System.Boolean, _
   ByVal DCycles As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim BChecked As System.Boolean
Dim DCycles As System.Double

instance.SetInfiniteLifeSettings2(BChecked, DCycles)
```

### C#

```csharp
void SetInfiniteLifeSettings2(
   System.bool BChecked,
   System.double DCycles
)
```

### C++/CLI

```cpp
void SetInfiniteLifeSettings2(
   System.bool BChecked,
   System.double DCycles
)
```

### Parameters

- `BChecked`: -1 or true to use DCyles number of cycles; 0 or false to use the number of cycles associated with the last point of an S-N curve
- `DCycles`: Number of cycles to be used when the corrected alternating stress is less than the endurance limit; valid only if BChecked is -1

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
