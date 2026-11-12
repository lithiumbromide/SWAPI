---
title: "GetInfiniteLifeSettings2 Method (ICWFatigueStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions"
member: "GetInfiniteLifeSettings2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions~GetInfiniteLifeSettings2.html"
---

# GetInfiniteLifeSettings2 Method (ICWFatigueStudyOptions)

Gets the infinite life settings of the fatigue study.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetInfiniteLifeSettings2( _
   ByRef BChecked As System.Boolean, _
   ByRef DCycles As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFatigueStudyOptions
Dim BChecked As System.Boolean
Dim DCycles As System.Double

instance.GetInfiniteLifeSettings2(BChecked, DCycles)
```

### C#

```csharp
void GetInfiniteLifeSettings2(
   out System.bool BChecked,
   out System.double DCycles
)
```

### C++/CLI

```cpp
void GetInfiniteLifeSettings2(
   [Out] System.bool BChecked,
   [Out] System.double DCycles
)
```

### Parameters

- `BChecked`: -1 or true to use DCyles number of cycles; 0 or false to use the number of cycles associated with the last point of an S-N curve
- `DCycles`: Number of cycles to use when the corrected alternating stress is less than the endurance limit; valid only if BChecked is -1

## Examples

See the [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html) examples.

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[ICWFatigueStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
