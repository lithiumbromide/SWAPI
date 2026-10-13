---
title: "ScaleY Property (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "ScaleY"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleY.html"
---

# ScaleY Property (IScaleFeatureData)

Gets or sets the scaling factor in the Y direction when uniform scaling is disabled.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleY As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData
Dim value As System.Double

instance.ScaleY = value

value = instance.ScaleY
```

### C#

```csharp
System.double ScaleY {get; set;}
```

### C++/CLI

```cpp
property System.double ScaleY {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Y-direction scale factor

## VBA Syntax

See [ScaleFeatureData::ScaleY](ms-its:sldworksapivb6.chm::/sldworks~ScaleFeatureData~ScaleY.html).

## Examples

See [IScaleFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData.html) examples.

## Remarks

| To get or set... | Use... |
| --- | --- |
| Uniform scaling | IScaleFeatureData::IsUniform |
| All scale-related values in the same call | IScaleFeatureData::GetScale or IScaleFeatureData::SetScale |

NOTE: To get or set the scaling factor when uniform scaling is enabled, use [IScaleFeatureData::ScaleUniform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~ScaleUniform.html).

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html)
[IScaleFeatureData::ScaleX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleX.html)
[IScaleFeatureData::ScaleZ Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleZ.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
