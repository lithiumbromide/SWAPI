---
title: "IFace Property (IDomeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData2"
member: "IFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~IFace.html"
---

# IFace Property (IDomeFeatureData2)

Obsolete. Superseded by [IDomeFeatureData2::Faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDomeFeatureData2~Faces.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IFace As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData2
Dim value As Face2

instance.IFace = value

value = instance.IFace
```

### C#

```csharp
Face2 IFace {get; set;}
```

### C++/CLI

```cpp
property Face2^ IFace {
   Face2^ get();
   void set (    Face2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DomeFeatureData2::IFace](ms-its:sldworksapivb6.chm::/sldworks~DomeFeatureData2~IFace.html).

## See Also

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html)
