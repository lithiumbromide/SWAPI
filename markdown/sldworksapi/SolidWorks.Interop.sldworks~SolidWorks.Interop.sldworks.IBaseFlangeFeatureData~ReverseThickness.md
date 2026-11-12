---
title: "ReverseThickness Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "ReverseThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReverseThickness.html"
---

# ReverseThickness Property (IBaseFlangeFeatureData)

Gets or sets the direction in which to thicken the sketch for the base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseThickness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

instance.ReverseThickness = value

value = instance.ReverseThickness
```

### C#

```csharp
System.bool ReverseThickness {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseThickness {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True reverses the direction in which to thicken the sketch, false does not

## VBA Syntax

See [BaseFlangeFeatureData::ReverseThickness](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~ReverseThickness.html).

## Remarks

The setter of this property is valid only if [IBaseFlangeFeatureData::OverrideDefaultSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideDefaultSheetMetalParameters.html) is true and [IBaseFlangeFeatureData::UseMaterialSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseMaterialSheetMetalParameters.html) is false.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Thickness.html)

## Availability

SOLIDWORKS 2001 SP2, Revision 9.2
