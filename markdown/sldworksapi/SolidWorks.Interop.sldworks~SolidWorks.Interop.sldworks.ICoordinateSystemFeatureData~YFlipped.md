---
title: "YFlipped Property (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "YFlipped"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YFlipped.html"
---

# YFlipped Property (ICoordinateSystemFeatureData)

Gets or sets whether to flip the y axis of this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property YFlipped As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Boolean

instance.YFlipped = value

value = instance.YFlipped
```

### C#

```csharp
System.bool YFlipped {get; set;}
```

### C++/CLI

```cpp
property System.bool YFlipped {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the y axis, false to not

## VBA Syntax

See [CoordinateSystemFeatureData::YFlipped](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~YFlipped.html).

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::GetYAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::IGetYAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntities.html)
[ICoordinateSystemFeatureData::ISetYAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetYAxisEntities.html)
[ICoordinateSystemFeatureData::YAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YAxisEntities.html)
[ICoordinateSystemFeatureData::GetYAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetYAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntitiesTypes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
