---
title: "ScaleUniform Property (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "ScaleUniform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleUniform.html"
---

# ScaleUniform Property (IScaleFeatureData)

Gets or sets the uniform scaling factor for this scale feature when uniform scaling is enabled.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleUniform As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData
Dim value As System.Double

instance.ScaleUniform = value

value = instance.ScaleUniform
```

### C#

```csharp
System.double ScaleUniform {get; set;}
```

### C++/CLI

```cpp
property System.double ScaleUniform {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value for the uniform scaling factor

## VBA Syntax

See [ScaleFeatureData::ScaleUniform](ms-its:sldworksapivb6.chm::/sldworks~ScaleFeatureData~ScaleUniform.html).

## Examples

See [IScaleFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData.html) examples.

## Remarks

You can use:

- [IScaleFeatureData::IsUniform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~IsUniform.html) to enable or disable uniform scaling.

  - or -
- [IScaleFeatureData::GetScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~GetScale.html) or [IScaleFeatureData::SetScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~SetScale.html) to get or set all of the scaling-related values, including uniform scaling, in the same call.

NOTE: If uniform scaling is disabled, then use these properties to get or set the individual scaling values:

- [IScaleFeatureData::ScaleX](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~ScaleX.html)
- [IScaleFeatureData::ScaleY](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~ScaleY.html)
- [IScaleFeatureData::ScaleZ](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~ScaleZ.html)

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
