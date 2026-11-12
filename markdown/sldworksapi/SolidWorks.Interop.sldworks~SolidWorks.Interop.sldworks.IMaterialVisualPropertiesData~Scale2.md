---
title: "Scale2 Property (IMaterialVisualPropertiesData)"
project: "SOLIDWORKS API Help"
interface: "IMaterialVisualPropertiesData"
member: "Scale2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~Scale2.html"
---

# Scale2 Property (IMaterialVisualPropertiesData)

Gets or sets the scale factor for the standard texture.

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMaterialVisualPropertiesData
Dim value As System.Double

instance.Scale2 = value

value = instance.Scale2
```

### C#

```csharp
System.double Scale2 {get; set;}
```

### C++/CLI

```cpp
property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value by which to scale the texture

## VBA Syntax

See [MaterialVisualPropertiesData::Scale2](ms-its:sldworksapivb6.chm::/sldworks~MaterialVisualPropertiesData~Scale2.html).

## Examples

See [IMaterialVisualPropertiesData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMaterialVisualPropertiesData.html) examples.

## Remarks

This property only applies to SOLIDWORKS standard textures.

## See Also

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.html)
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
