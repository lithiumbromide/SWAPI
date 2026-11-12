---
title: "GetProfileType Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "GetProfileType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetProfileType.html"
---

# GetProfileType Method (ISweepFeatureData)

Gets the profile type of this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProfileType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Integer

value = instance.GetProfileType()
```

### C#

```csharp
System.int GetProfileType()
```

### C++/CLI

```cpp
System.int GetProfileType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Sweep profile type as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [SweepFeatureData::GetProfileType](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~GetProfileType.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::Profile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Profile.html)
[ISweepFeatureData::CircularProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfile.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
