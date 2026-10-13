---
title: "GetLastFeatureAdded Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetLastFeatureAdded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetLastFeatureAdded.html"
---

# GetLastFeatureAdded Method (IModelDocExtension)

Gets the last feature added to the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLastFeatureAdded() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As Feature

value = instance.GetLastFeatureAdded()
```

### C#

```csharp
Feature GetLastFeatureAdded()
```

### C++/CLI

```cpp
Feature^ GetLastFeatureAdded();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [ModelDocExtension::GetLastFeatureAdded](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetLastFeatureAdded.html).

## Remarks

This method can access subfeature types such as mates, drawing views, and so on. For example, if you just added the first coincident mate to MateGroup, then IModelDocExtension::GetLastFeatureAdded will return Coincident1. [IModelDoc2::FeatureByPositionReverse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureByPositionReverse.html) and [IModelDoc2::IFeatureByPositionReverse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IFeatureByPositionReverse.html) will return MateGroup.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
