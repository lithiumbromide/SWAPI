---
title: "IFace Property (IDomeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData"
member: "IFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData~IFace.html"
---

# IFace Property (IDomeFeatureData)

Obsolete. Superseded by [IDomeFeatureData2::IFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDomeFeatureData2~IFace.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IFace As Face
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData
Dim value As Face

instance.IFace = value

value = instance.IFace
```

### C#

```csharp
Face IFace {get; set;}
```

### C++/CLI

```cpp
property Face^ IFace {
   Face^ get();
   void set (    Face^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DomeFeatureData::IFace](ms-its:sldworksapivb6.chm::/sldworks~DomeFeatureData~IFace.html).

## See Also

[IDomeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData.html)
[IDomeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData_members.html)
