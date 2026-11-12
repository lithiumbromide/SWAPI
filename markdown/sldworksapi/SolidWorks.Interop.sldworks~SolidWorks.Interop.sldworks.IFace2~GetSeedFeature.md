---
title: "GetSeedFeature Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetSeedFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSeedFeature.html"
---

# GetSeedFeature Method (IFace2)

Gets the seed feature of a patterned, mirrored, or copied body for this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSeedFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As Feature

value = instance.GetSeedFeature()
```

### C#

```csharp
Feature GetSeedFeature()
```

### C++/CLI

```cpp
Feature^ GetSeedFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Seed [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) of a patterned, mirrored, or copied body

## VBA Syntax

See [Face2::GetSeedFeature](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetSeedFeature.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetPatternSeedFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetPatternSeedFeature.html)

## Availability

SOLIDWORKS 2008 SP4, Revision Number 16.4
