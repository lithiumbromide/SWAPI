---
title: "UseChamferCorners Property (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "UseChamferCorners"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~UseChamferCorners.html"
---

# UseChamferCorners Property (IEndCapFeatureData)

Gets or sets whether to chamfer the corners of this end-cap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseChamferCorners As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData
Dim value As System.Boolean

instance.UseChamferCorners = value

value = instance.UseChamferCorners
```

### C#

```csharp
System.bool UseChamferCorners {get; set;}
```

### C++/CLI

```cpp
property System.bool UseChamferCorners {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to chamfer corners, false to fillet corners

## VBA Syntax

See [EndCapFeatureData::UseChamferCorners](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~UseChamferCorners.html).

## Examples

See the [IEndCapFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData.html) examples.

## Remarks

This property is valid only if [IEndCapFeatureData::UseCornerTreatment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData~UseCornerTreatment.html) is true.

Call [IEndCapFeatureData::ChamferDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData~ChamferDistance.html) to set the chamfer distance or fillet radius of the end cap corner.

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
