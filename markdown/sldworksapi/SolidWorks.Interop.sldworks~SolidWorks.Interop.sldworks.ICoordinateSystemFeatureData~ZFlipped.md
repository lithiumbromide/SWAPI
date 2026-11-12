---
title: "ZFlipped Property (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "ZFlipped"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZFlipped.html"
---

# ZFlipped Property (ICoordinateSystemFeatureData)

Gets or sets whether to flip the z axis of this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ZFlipped As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Boolean

instance.ZFlipped = value

value = instance.ZFlipped
```

### C#

```csharp
System.bool ZFlipped {get; set;}
```

### C++/CLI

```cpp
property System.bool ZFlipped {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the z axis, false to not

## VBA Syntax

See [CoordinateSystemFeatureData::ZFlipped](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~ZFlipped.html).

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::GetZAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::IGetZAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntities.html)
[ICoordinateSystemFeatureData::ISetZAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetZAxisEntities.html)
[ICoordinateSystemFeatureData::ZAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZAxisEntities.html)
[ICoordinateSystemFeatureData::GetZAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetZAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntitiesTypes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
