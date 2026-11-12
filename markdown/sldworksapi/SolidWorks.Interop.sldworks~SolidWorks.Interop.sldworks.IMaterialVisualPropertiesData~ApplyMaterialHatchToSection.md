---
title: "ApplyMaterialHatchToSection Property (IMaterialVisualPropertiesData)"
project: "SOLIDWORKS API Help"
interface: "IMaterialVisualPropertiesData"
member: "ApplyMaterialHatchToSection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~ApplyMaterialHatchToSection.html"
---

# ApplyMaterialHatchToSection Property (IMaterialVisualPropertiesData)

Gets or sets whether the drawing section views use the material hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Property ApplyMaterialHatchToSection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMaterialVisualPropertiesData
Dim value As System.Boolean

instance.ApplyMaterialHatchToSection = value

value = instance.ApplyMaterialHatchToSection
```

### C#

```csharp
System.bool ApplyMaterialHatchToSection {get; set;}
```

### C++/CLI

```cpp
property System.bool ApplyMaterialHatchToSection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the [drawing section views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection.html) use the material hatch, false if not

## VBA Syntax

See [MaterialVisualPropertiesData::ApplyMaterialHatchToSection](ms-its:sldworksapivb6.chm::/sldworks~MaterialVisualPropertiesData~ApplyMaterialHatchToSection.html).

## Examples

See [IMaterialVisualPropertiesData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMaterialVisualPropertiesData.html) examples.

## See Also

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.html)
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Numbe 15.0
