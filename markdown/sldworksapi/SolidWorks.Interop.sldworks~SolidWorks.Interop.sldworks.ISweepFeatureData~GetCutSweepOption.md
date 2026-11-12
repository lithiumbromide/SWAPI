---
title: "GetCutSweepOption Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "GetCutSweepOption"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetCutSweepOption.html"
---

# GetCutSweepOption Method (ISweepFeatureData)

Gets the type of this cut sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCutSweepOption() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Integer

value = instance.GetCutSweepOption()
```

### C#

```csharp
System.int GetCutSweepOption()
```

### C++/CLI

```cpp
System.int GetCutSweepOption();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Cut sweep type as defined in [swCutSweepOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCutSweepOption_e.html)

## VBA Syntax

See [SweepFeatureData::GetCutSweepOption](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~GetCutSweepOption.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::CircularProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfile.html)
[ISweepFeatureData::Profile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Profile.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
