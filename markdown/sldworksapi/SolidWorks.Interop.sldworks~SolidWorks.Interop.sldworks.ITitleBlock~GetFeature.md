---
title: "GetFeature Method (ITitleBlock)"
project: "SOLIDWORKS API Help"
interface: "ITitleBlock"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~GetFeature.html"
---

# GetFeature Method (ITitleBlock)

Gets the feature for this title block.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As ITitleBlock
Dim value As Feature

value = instance.GetFeature()
```

### C#

```csharp
Feature GetFeature()
```

### C++/CLI

```cpp
Feature^ GetFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [TitleBlock::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~TitleBlock~GetFeature.html).

## See Also

[ITitleBlock Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.html)
[ITitleBlock Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
