---
title: "MaxVal Property (IHingeMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHingeMateFeatureData"
member: "MaxVal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~MaxVal.html"
---

# MaxVal Property (IHingeMateFeatureData)

Gets or sets the maximum angular rotation between the two components.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaxVal As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHingeMateFeatureData
Dim value As System.Double

instance.MaxVal = value

value = instance.MaxVal
```

### C#

```csharp
System.double MaxVal {get; set;}
```

### C++/CLI

```cpp
property System.double MaxVal {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum angular rotation in radians

## VBA Syntax

See [HingeMateFeatureData::MaxVal](ms-its:sldworksapivb6.chm::/sldworks~HingeMateFeatureData~MaxVal.html).

## Examples

See the [IHingeMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.html) example.

## Remarks

This property is valid only if [IHingeMateFeatureData::AngleSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~AngleSelection.html) is set to true.

## See Also

[IHingeMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.html)
[IHingeMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData_members.html)
[IHingeMateFeatureData::MinVal Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~MinVal.html)
[IHingeMateFeatureData::Angle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~Angle.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
