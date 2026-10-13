---
title: "GetBody Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetBody.html"
---

# GetBody Method (IFeature)

Obsolete. Superseded by [IFeatures::GetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFaces.html), [IFeatures::IGetFaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFaces2.html), [IFace2::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetBody.html), and [IFace2::IGetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetBody.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBody() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Object

value = instance.GetBody()
```

### C#

```csharp
System.object GetBody()
```

### C++/CLI

```cpp
System.Object^ GetBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html

## VBA Syntax

See [Feature::GetBody](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetBody.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
