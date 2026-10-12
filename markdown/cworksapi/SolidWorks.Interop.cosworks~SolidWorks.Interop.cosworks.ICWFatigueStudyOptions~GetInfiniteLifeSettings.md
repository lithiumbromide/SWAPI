---
title: "GetInfiniteLifeSettings Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "GetInfiniteLifeSettings"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetInfiniteLifeSettings.html"
---

# GetInfiniteLifeSettings Method (ICWFatigueStudyOptions)

Obsolete. Superseded by [ICWFatigueStudyOptions::GetInfiniteLifeSettings2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetInfiniteLifeSettings2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetInfiniteLifeSettings( _
   ByRef BChecked As System.Integer, _
   ByRef DCycles As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim BChecked As System.Integer
Dim DCycles As System.Double

instance.GetInfiniteLifeSettings(BChecked, DCycles)
```

### C#

```csharp
void GetInfiniteLifeSettings(
   out System.int BChecked,
   out System.double DCycles
)
```

### C++/CLI

```cpp
void GetInfiniteLifeSettings(
   [Out] System.int BChecked,
   [Out] System.double DCycles
)
```

### Parameters

- `BChecked`: 1 to use DCyles number of cycles; 0 to use the number of cycles associated with the last point of an S-N curve
- `DCycles`: Number of cycles to use when the corrected alternating stress is less than the endurance limit; valid only if BChecked is 1

## VBA Syntax

See [CWFatigueStudyOptions::GetInfiniteLifeSettings](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFatigueStudyOptions~GetInfiniteLifeSettings.html).

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)
[ICWFatigueStudyOptions::SetInfiniteLifeSettings Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~SetInfiniteLifeSettings.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
