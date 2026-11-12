---
title: "UseDefaultBendRadius Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "UseDefaultBendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UseDefaultBendRadius.html"
---

# UseDefaultBendRadius Property (IMiterFlangeFeatureData)

Gets or sets whether to use the default bend radius for this miter flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
Dim value As System.Boolean

instance.UseDefaultBendRadius = value

value = instance.UseDefaultBendRadius
```

### C#

```csharp
System.bool UseDefaultBendRadius {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDefaultBendRadius {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the default bend radius, false to use specified bend radius

## VBA Syntax

See [MiterFlangeFeatureData::UseDefaultBendRadius](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~UseDefaultBendRadius.html).

## Examples

See [IMiterFlangeFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMiterFlangeFeatureData.html) examples.

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)
[IMiterFlangeFeatureData::BendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~BendRadius.html)

## Availability

SOLIDWORKS 2001 SP2, Revision number 9.2
