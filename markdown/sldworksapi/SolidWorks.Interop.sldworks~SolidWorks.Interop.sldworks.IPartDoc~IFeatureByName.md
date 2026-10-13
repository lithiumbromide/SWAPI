---
title: "IFeatureByName Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IFeatureByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureByName.html"
---

# IFeatureByName Method (IPartDoc)

Gets the named feature in the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureByName( _
   ByVal Name As System.String _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Name As System.String
Dim value As Feature

value = instance.IFeatureByName(Name)
```

### C#

```csharp
Feature IFeatureByName(
   System.string Name
)
```

### C++/CLI

```cpp
Feature^ IFeatureByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of feature

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [PartDoc::IFeatureByName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~IFeatureByName.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::IFeatureById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureById.html)
[IPartDoc::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureByName.html)
[IPartDoc::FeatureById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureById.html)
