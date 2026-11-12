---
title: "IGetBody2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IGetBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetBody2.html"
---

# IGetBody2 Method (IFeature)

Obsolete. Superseded by [IFeatures::GetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFaces.html), [IFeatures::IGetFaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFaces2.html), [IFace2::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetBody.html), and [IFace2::IGetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetBody.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBody2() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As Body2

value = instance.IGetBody2()
```

### C#

```csharp
Body2 IGetBody2()
```

### C++/CLI

```cpp
Body2^ IGetBody2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Feature::IGetBody2](ms-its:sldworksapivb6.chm::/sldworks~Feature~IGetBody2.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
