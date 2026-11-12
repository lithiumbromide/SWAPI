---
title: "ApplyMaterialColorToPart Property (IMaterialVisualPropertiesData)"
project: "SOLIDWORKS API Help"
interface: "IMaterialVisualPropertiesData"
member: "ApplyMaterialColorToPart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~ApplyMaterialColorToPart.html"
---

# ApplyMaterialColorToPart Property (IMaterialVisualPropertiesData)

Gets or sets whether the part color matches the material color.

## Syntax

### Visual Basic (Declaration)

```vb
Property ApplyMaterialColorToPart As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMaterialVisualPropertiesData
Dim value As System.Boolean

instance.ApplyMaterialColorToPart = value

value = instance.ApplyMaterialColorToPart
```

### C#

```csharp
System.bool ApplyMaterialColorToPart {get; set;}
```

### C++/CLI

```cpp
property System.bool ApplyMaterialColorToPart {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the part color matches the material color, false if not

## VBA Syntax

See [MaterialVisualPropertiesData::ApplyMaterialColorToPart](ms-its:sldworksapivb6.chm::/sldworks~MaterialVisualPropertiesData~ApplyMaterialColorToPart.html).

## Examples

See [IMaterialVisualPropertiesData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMaterialVisualPropertiesData.html) examples.

## See Also

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.html)
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
