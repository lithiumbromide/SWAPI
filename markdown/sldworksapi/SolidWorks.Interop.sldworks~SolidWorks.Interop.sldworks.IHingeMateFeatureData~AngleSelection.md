---
title: "AngleSelection Property (IHingeMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHingeMateFeatureData"
member: "AngleSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~AngleSelection.html"
---

# AngleSelection Property (IHingeMateFeatureData)

Gets or sets whether to specify angle limits.

## Syntax

### Visual Basic (Declaration)

```vb
Property AngleSelection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHingeMateFeatureData
Dim value As System.Boolean

instance.AngleSelection = value

value = instance.AngleSelection
```

### C#

```csharp
System.bool AngleSelection {get; set;}
```

### C++/CLI

```cpp
property System.bool AngleSelection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to specify angle limits, false to not

## VBA Syntax

See [HingeMateFeatureData::AngleSelection](ms-its:sldworksapivb6.chm::/sldworks~HingeMateFeatureData~AngleSelection.html).

## Examples

See the [IHingeMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.html) example.

## Remarks

After setting this property to true, also set:

- [IHingeMateFeatureData::Angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~Angle.html)
- [IHingeMateFeatureData::MaxVal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~MaxVal.html)
- [IHingeMateFeatureData::MinVal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~MinVal.html)

## See Also

[IHingeMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.html)
[IHingeMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
