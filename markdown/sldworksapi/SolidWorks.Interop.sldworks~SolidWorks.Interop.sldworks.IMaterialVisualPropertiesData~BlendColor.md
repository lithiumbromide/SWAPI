---
title: "BlendColor Property (IMaterialVisualPropertiesData)"
project: "SOLIDWORKS API Help"
interface: "IMaterialVisualPropertiesData"
member: "BlendColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~BlendColor.html"
---

# BlendColor Property (IMaterialVisualPropertiesData)

Gets or sets whether to blend the part color with the texture.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlendColor As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMaterialVisualPropertiesData
Dim value As System.Boolean

instance.BlendColor = value

value = instance.BlendColor
```

### C#

```csharp
System.bool BlendColor {get; set;}
```

### C++/CLI

```cpp
property System.bool BlendColor {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to blend the color with the texture, false to not

## VBA Syntax

See [MaterialVisualPropertiesData::BlendColor](ms-its:sldworksapivb6.chm::/sldworks~MaterialVisualPropertiesData~BlendColor.html).

## Examples

See [IMaterialVisualPropertiesData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMaterialVisualPropertiesData.html) examples.

## Remarks

This property on applies to SOLIDWORKS standard textures.

## See Also

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.html)
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
