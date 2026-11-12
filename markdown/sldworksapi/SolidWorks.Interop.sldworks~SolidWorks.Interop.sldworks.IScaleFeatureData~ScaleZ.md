---
title: "ScaleZ Property (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "ScaleZ"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleZ.html"
---

# ScaleZ Property (IScaleFeatureData)

Gets or sets the scaling factor in the Z direction when uniform scaling is disabled.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleZ As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData
Dim value As System.Double

instance.ScaleZ = value

value = instance.ScaleZ
```

### C#

```csharp
System.double ScaleZ {get; set;}
```

### C++/CLI

```cpp
property System.double ScaleZ {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Z-direction scale factor

## VBA Syntax

See [ScaleFeatureData::ScaleZ](ms-its:sldworksapivb6.chm::/sldworks~ScaleFeatureData~ScaleZ.html).

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
[IScaleFeatureData::ScaleY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleY.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
