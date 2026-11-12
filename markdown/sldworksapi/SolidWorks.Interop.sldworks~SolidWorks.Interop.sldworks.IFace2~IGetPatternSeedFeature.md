---
title: "IGetPatternSeedFeature Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetPatternSeedFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetPatternSeedFeature.html"
---

# IGetPatternSeedFeature Method (IFace2)

Gets the seed feature of a pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPatternSeedFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As Feature

value = instance.IGetPatternSeedFeature()
```

### C#

```csharp
Feature IGetPatternSeedFeature()
```

### C++/CLI

```cpp
Feature^ IGetPatternSeedFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Seed feature of the current face; if the face does not belong to a pattern, this method returns NULL

## VBA Syntax

See [Face2::IGetPatternSeedFeature](ms-its:sldworksapivb6.chm::/sldworks~Face2~IGetPatternSeedFeature.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetPatternSeedFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetPatternSeedFeature.html)
[IModelDoc2::EditSeedFeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSeedFeat.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
