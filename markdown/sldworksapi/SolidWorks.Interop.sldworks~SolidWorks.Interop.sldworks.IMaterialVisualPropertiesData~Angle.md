---
title: "Angle Property (IMaterialVisualPropertiesData)"
project: "SOLIDWORKS API Help"
interface: "IMaterialVisualPropertiesData"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~Angle.html"
---

# Angle Property (IMaterialVisualPropertiesData)

Gets or sets the angle of the texture.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMaterialVisualPropertiesData
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle in radians

## VBA Syntax

See [MaterialVisualPropertiesData::Angle](ms-its:sldworksapivb6.chm::/sldworks~MaterialVisualPropertiesData~Angle.html).

## Examples

See [IMaterialVisualPropertiesData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMaterialVisualPropertiesData.html) examples.

## Remarks

This property only applies to SOLIDWORKS standard textures.

## See Also

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.html)
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
