---
title: "XFlipped Property (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "XFlipped"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~XFlipped.html"
---

# XFlipped Property (ICoordinateSystemFeatureData)

Gets or sets whether to flip the x axis of this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property XFlipped As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Boolean

instance.XFlipped = value

value = instance.XFlipped
```

### C#

```csharp
System.bool XFlipped {get; set;}
```

### C++/CLI

```cpp
property System.bool XFlipped {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the x axis, false to not

## VBA Syntax

See [CoordinateSystemFeatureData::XFlipped](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~XFlipped.html).

## Examples

[Insert Coordinate System Feature at Center of Mass (VBA)](Insert_Coordinate_System_Feature_at_Center_of_Mass_Example_VB.htm)
[Create Coordinate System Feature (VBA)](Create_Coordinate_System_Feature_Example_VB.htm)

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::GetXAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::IGetXAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetXAxisEntities.html)
[ICoordinateSystemFeatureData::ISetXAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetXAxisEntities.html)
[ICoordinateSystemFeatureData::XAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~XAxisEntities.html)
[ICoordinateSystemFeatureData::GetXAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetXAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetXAxisEntitiesTypes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
