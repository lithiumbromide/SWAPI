---
title: "IGetFeature Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFeature.html"
---

# IGetFeature Method (IFace2)

Gets the feature that owns this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As Feature

value = instance.IGetFeature()
```

### C#

```csharp
Feature IGetFeature()
```

### C++/CLI

```cpp
Feature^ IGetFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the owning [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [Face2::IGetFeature](ms-its:sldworksapivb6.chm::/sldworks~Face2~IGetFeature.html).

## Remarks

In SOLIDWORKS, a face:

- is the result of evaluating a feature.
- can be owned by several features.

[IFeature::GetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFaces.html) or [IFeature::IGetFaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFaces2.html) returns all of the faces owned by a feature. This is different from the faces highlighted in the user interface when the feature is selected. The user interface filters out multiple feature faces. This filter is only for display purposes.

To filter out multiple feature faces using the SOLIDWORKS API, you must call [IFace2::GetFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetFeature.html) or IFace2::IGetFeature. Only the oldest feature from the face is returned, that is, the first owning feature in the FeatureManager design tree.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetFeatureId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFeatureId.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
