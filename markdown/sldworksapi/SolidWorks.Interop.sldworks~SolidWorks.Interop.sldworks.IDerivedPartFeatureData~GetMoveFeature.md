---
title: "GetMoveFeature Method (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "GetMoveFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~GetMoveFeature.html"
---

# GetMoveFeature Method (IDerivedPartFeatureData)

Gets the move/copy feature belonging to this derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMoveFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As Feature

value = instance.GetMoveFeature()
```

### C#

```csharp
Feature GetMoveFeature()
```

### C++/CLI

```cpp
Feature^ GetMoveFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Move/copy [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [DerivedPartFeatureData::GetMoveFeature](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~GetMoveFeature.html).

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)
[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
