---
title: "ApplyAppearance Property (IMaterialVisualPropertiesData)"
project: "SOLIDWORKS API Help"
interface: "IMaterialVisualPropertiesData"
member: "ApplyAppearance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~ApplyAppearance.html"
---

# ApplyAppearance Property (IMaterialVisualPropertiesData)

Gets or sets whether to apply the appearance of material.

## Syntax

### Visual Basic (Declaration)

```vb
Property ApplyAppearance As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMaterialVisualPropertiesData
Dim value As System.Boolean

instance.ApplyAppearance = value

value = instance.ApplyAppearance
```

### C#

```csharp
System.bool ApplyAppearance {get; set;}
```

### C++/CLI

```cpp
property System.bool ApplyAppearance {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to apply the appearance of material, false to not (see **Remarks**)

## VBA Syntax

See [MaterialVisualPropertiesData::ApplyAppearance](ms-its:sldworksapivb6.chm::/sldworks~MaterialVisualPropertiesData~ApplyAppearance.html).

## Examples

See [IMaterialVisualPropertiesData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMaterialVisualPropertiesData.html) examples.

## Remarks

| If this property is... | Then... |
| --- | --- |
| False | There is no change in the appearance of the body when material is changed. |
| True | The appearance of the body changes when material is changed. |

## See Also

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.html)
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
