---
title: "CoordinateSystem Property (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "CoordinateSystem"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~CoordinateSystem.html"
---

# CoordinateSystem Property (IScaleFeatureData)

Gets or sets the coordinate system of the scale feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CoordinateSystem As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData
Dim value As System.Object

instance.CoordinateSystem = value

value = instance.CoordinateSystem
```

### C#

```csharp
System.object CoordinateSystem {get; set;}
```

### C++/CLI

```cpp
property System.Object^ CoordinateSystem {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the coordinate system [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [ScaleFeatureData::CoordinateSystem](ms-its:sldworksapivb6.chm::/sldworks~ScaleFeatureData~CoordinateSystem.html).

## Examples

See [IScaleFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html)

## Availability

SoldWorks 2001Plus FCS, Revision Number 10.0
