---
title: "Thickness Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "Thickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Thickness.html"
---

# Thickness Property (ISweptFlangeFeatureData)

Gets or sets the sheet metal thickness of this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Thickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
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

Sheet metal thickness

## VBA Syntax

See [SweptFlangeFeatureData::Thickness](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~Thickness.html).

## Remarks

This property is valid only when not creating the swept flange on an existing sheet metal feature.

The setter of this property is valid only if [ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~OverrideDefaultSheetMetalParameters.html) is true.

This property gets:

- Default thickness if ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters is false.

- Custom thickness if ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters is true.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
