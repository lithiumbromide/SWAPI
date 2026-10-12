---
title: "MakeSubFeature Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "MakeSubFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MakeSubFeature.html"
---

# MakeSubFeature Method (IFeature)

Makes a feature become a subfeature of this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeSubFeature( _
   ByVal SubFeature As Feature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim SubFeature As Feature
Dim value As System.Boolean

value = instance.MakeSubFeature(SubFeature)
```

### C#

```csharp
System.bool MakeSubFeature(
   Feature SubFeature
)
```

### C++/CLI

```cpp
System.bool MakeSubFeature(
   Feature^ SubFeature
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SubFeature`: Pointer to the [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) to become a subfeature

### Return Value

True if the feature becomes a subfeature, false if not

## VBA Syntax

See [Feature::MakeSubFeature](ms-its:sldworksapivb6.chm::/sldworks~Feature~MakeSubFeature.html).

## Examples

[Create Macro Feature Subfeature (VBA)](Create_Macro_Feature_Subfeature_Example_VB.htm)

## Remarks

- This method is not supported in assembly documents.
- This method can only be used to make subfeatures to a macro feature.
- The feature and subfeature must have a parent-child relationship. If the subfeature is a reference plane, then the feature and subfeatures of the feature are the only parents of the subfeature to be inserted.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetFirstSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.html)
[IFeature::GetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.html)
[IFeature::IGetFirstSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFirstSubFeature.html)
[IFeature::IGetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextSubFeature.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
