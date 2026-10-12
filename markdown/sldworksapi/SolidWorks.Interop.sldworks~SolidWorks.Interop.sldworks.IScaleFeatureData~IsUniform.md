---
title: "IsUniform Property (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "IsUniform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IsUniform.html"
---

# IsUniform Property (IScaleFeatureData)

Gets or sets uniform scaling for this scale feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsUniform As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData
Dim value As System.Boolean

instance.IsUniform = value

value = instance.IsUniform
```

### C#

```csharp
System.bool IsUniform {get; set;}
```

### C++/CLI

```cpp
property System.bool IsUniform {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True for uniform scaling, false for non-uniform scaling

## VBA Syntax

See [ScaleFeatureData::IsUniform](ms-its:sldworksapivb6.chm::/sldworks~ScaleFeatureData~IsUniform.html).

## Examples

See [IScaleFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData.html) examples.

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html)
[IScaleFeatureData::GetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetScale.html)
[IScaleFeatureData::SetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~SetScale.html)
[IScaleFeatureData::ScaleUniform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleUniform.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
