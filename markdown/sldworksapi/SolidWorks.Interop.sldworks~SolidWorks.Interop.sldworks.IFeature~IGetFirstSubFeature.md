---
title: "IGetFirstSubFeature Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IGetFirstSubFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFirstSubFeature.html"
---

# IGetFirstSubFeature Method (IFeature)

Gets the first sub-feature that belongs to this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstSubFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As Feature

value = instance.IGetFirstSubFeature()
```

### C#

```csharp
Feature IGetFirstSubFeature()
```

### C++/CLI

```cpp
Feature^ IGetFirstSubFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer the first sub-[feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) of this feature

## VBA Syntax

See [Feature::IGetFirstSubFeature](ms-its:sldworksapivb6.chm::/sldworks~Feature~IGetFirstSubFeature.html).

## Examples

[Get Sketches (C++)](Get_Sketches_Example_CPlusPlus_COM.htm)

## Remarks

If no sub-features exist for this feature, then this method returns NULL.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetFirstSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.html)
[IFeature::GetNextFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.html)
[IFeature::GetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.html)
[IFeature::IGetNextFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextFeature.html)
[IFeature::IGetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextSubFeature.html)
[IFeature::MakeSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MakeSubFeature.html)
[IComponent2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FirstFeature.html)
[IModelDoc2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.html)
[IModelDoc2::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFirstFeature.html)
[IPartDoc::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FirstFeature.html)
[IPartDoc::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFirstFeature.html)
