---
title: "IGetBody Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IGetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBody.html"
---

# IGetBody Method (IFeature)

Obsolete. Superseded by [IFeatures::GetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFaces.html), [IFeatures::IGetFaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFaces2.html), [IFace2::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetBody.html), and [IFace2::IGetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetBody.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBody() As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As Body

value = instance.IGetBody()
```

### C#

```csharp
Body IGetBody()
```

### C++/CLI

```cpp
Body^ IGetBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Feature::IGetBody](ms-its:sldworksapivb6.chm::/sldworks~Feature~IGetBody.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
