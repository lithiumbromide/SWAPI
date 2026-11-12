---
title: "SetInfiniteLifeSettings Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "SetInfiniteLifeSettings"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~SetInfiniteLifeSettings.html"
---

# SetInfiniteLifeSettings Method (ICWFatigueStudyOptions)

Obsolete. Superseded by [ICWFatigueStudyOptions::SetInfiniteLifeSettings2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~SetInfiniteLifeSettings2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetInfiniteLifeSettings( _
   ByVal BChecked As System.Integer, _
   ByVal DCycles As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim BChecked As System.Integer
Dim DCycles As System.Double

instance.SetInfiniteLifeSettings(BChecked, DCycles)
```

### C#

```csharp
void SetInfiniteLifeSettings(
   System.int BChecked,
   System.double DCycles
)
```

### C++/CLI

```cpp
void SetInfiniteLifeSettings(
   System.int BChecked,
   System.double DCycles
)
```

### Parameters

- `BChecked`: 1 to use DCyles number of cycles; 0 to use the number of cycles associated with the last point of an S-N curve
- `DCycles`: Number of cycles to be used when the corrected alternating stress is less than the endurance limit; valid only if BChecked is 1

## VBA Syntax

See [CWFatigueStudyOptions::SetInfiniteLifeSettings](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~SetInfiniteLifeSettings.html).

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::GetInfiniteLifeSettings Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetInfiniteLifeSettings.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
