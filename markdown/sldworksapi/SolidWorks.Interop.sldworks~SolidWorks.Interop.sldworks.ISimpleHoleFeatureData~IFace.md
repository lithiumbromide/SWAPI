---
title: "IFace Property (ISimpleHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData"
member: "IFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData~IFace.html"
---

# IFace Property (ISimpleHoleFeatureData)

Obsolete. Superseded by [ISimpleHoleFeatureData2::IFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2~IFace.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IFace As Face
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData
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

See [SimpleHoleFeatureData::IFace](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData~IFace.html).

## See Also

[ISimpleHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData.html)
[ISimpleHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData_members.html)
