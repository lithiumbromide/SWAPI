---
title: "IFeatureById Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IFeatureById"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureById.html"
---

# IFeatureById Method (IPartDoc)

Gets the feature with the specified ID in the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureById( _
   ByVal ID As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ID As System.Integer
Dim value As Feature

value = instance.IFeatureById(ID)
```

### C#

```csharp
Feature IFeatureById(
   System.int ID
)
```

### C++/CLI

```cpp
Feature^ IFeatureById(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: ID of feature

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [PartDoc::IFeatureById](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~IFeatureById.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::FeatureById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureById.html)
[IPartDoc::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureByName.html)
[IPartDoc::IFeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureByName.html)
