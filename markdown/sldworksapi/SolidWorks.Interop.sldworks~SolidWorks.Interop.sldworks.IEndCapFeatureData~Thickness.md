---
title: "Thickness Property (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "Thickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~Thickness.html"
---

# Thickness Property (IEndCapFeatureData)

Gets or sets the thickness for this end-cap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Thickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData
Dim value As System.Double

instance.Thickness = value

value = instance.Thickness
```

### C#

```csharp
System.double Thickness {get; set;}
```

### C++/CLI

```cpp
property System.double Thickness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thickness

## VBA Syntax

See [EndCapFeatureData::Thickness](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~Thickness.html).

## Examples

See the [IEndCapFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData.html) examples.

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)
[IEndCapFeatureData::ThicknessRatioForOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~ThicknessRatioForOffset.html)
[IEndCapFeatureData::UseThicknessRatioForOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~UseThicknessRatioForOffset.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
