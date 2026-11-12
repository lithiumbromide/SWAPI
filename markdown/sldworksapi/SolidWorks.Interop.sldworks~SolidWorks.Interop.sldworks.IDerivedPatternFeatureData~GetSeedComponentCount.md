---
title: "GetSeedComponentCount Method (IDerivedPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: "GetSeedComponentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~GetSeedComponentCount.html"
---

# GetSeedComponentCount Method (IDerivedPatternFeatureData)

Gets the number of seed component features for this derived pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSeedComponentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPatternFeatureData
Dim value As System.Integer

value = instance.GetSeedComponentCount()
```

### C#

```csharp
System.int GetSeedComponentCount()
```

### C++/CLI

```cpp
System.int GetSeedComponentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of seed component features on which the pattern is based

## VBA Syntax

See [DerivedPatternFeatureData::GetSeedComponentCount](ms-its:sldworksapivb6.chm::/sldworks~DerivedPatternFeatureData~GetSeedComponentCount.html).

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)
[IDerivedPatternFeatureData::IGetSeedComponentArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~IGetSeedComponentArray.html)
[IDerivedPatternFeatureData::ISetSeedComponentArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~ISetSeedComponentArray.html)
[IDerivedPatternFeatureData::SeedComponentArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~SeedComponentArray.html)

## Availability

SOLIDWORKS 2001 SP2, Revision 9.2
