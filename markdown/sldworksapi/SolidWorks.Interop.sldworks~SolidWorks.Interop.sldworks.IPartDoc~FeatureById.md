---
title: "FeatureById Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "FeatureById"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureById.html"
---

# FeatureById Method (IPartDoc)

Gets the feature with the specified ID in the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureById( _
   ByVal ID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ID As System.Integer
Dim value As System.Object

value = instance.FeatureById(ID)
```

### C#

```csharp
System.object FeatureById(
   System.int ID
)
```

### C++/CLI

```cpp
System.Object^ FeatureById(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: ID of feature

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [PartDoc::FeatureById](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~FeatureById.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::IFeatureById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureById.html)
[IPartDoc::IFeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureByName.html)
[IPartDoc::FeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureByName.html)
