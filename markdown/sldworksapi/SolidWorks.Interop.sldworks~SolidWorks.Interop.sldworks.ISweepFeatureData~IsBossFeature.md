---
title: "IsBossFeature Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "IsBossFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsBossFeature.html"
---

# IsBossFeature Method (ISweepFeatureData)

Gets whether the sweep feature is a boss feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBossFeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Boolean

value = instance.IsBossFeature()
```

### C#

```csharp
System.bool IsBossFeature()
```

### C++/CLI

```cpp
System.bool IsBossFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a boss feature, false if not

## VBA Syntax

See [SweepFeatureData::IsBossFeature](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~IsBossFeature.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsThinFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
