---
title: "MinVal Property (IHingeMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHingeMateFeatureData"
member: "MinVal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~MinVal.html"
---

# MinVal Property (IHingeMateFeatureData)

Gets or sets the minimum angular rotation between the two components.

## Syntax

### Visual Basic (Declaration)

```vb
Property MinVal As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHingeMateFeatureData
Dim value As System.Double

instance.MinVal = value

value = instance.MinVal
```

### C#

```csharp
System.double MinVal {get; set;}
```

### C++/CLI

```cpp
property System.double MinVal {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Minimum angular rotation in radians

## VBA Syntax

See [HingeMateFeatureData::MinVal](ms-its:sldworksapivb6.chm::/sldworks~HingeMateFeatureData~MinVal.html).

## Examples

See the [IHingeMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.html) example.

## Remarks

This property is valid only if [IHingeMateFeatureData::AngleSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~AngleSelection.html) is set to true.

## See Also

[IHingeMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.html)
[IHingeMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData_members.html)
[IHingeMateFeatureData::MaxVal Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~MaxVal.html)
[IHingeMateFeatureData::Angle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~Angle.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
