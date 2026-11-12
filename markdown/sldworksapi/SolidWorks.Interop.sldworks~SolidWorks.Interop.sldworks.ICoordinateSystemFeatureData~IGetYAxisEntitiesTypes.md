---
title: "IGetYAxisEntitiesTypes Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "IGetYAxisEntitiesTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntitiesTypes.html"
---

# IGetYAxisEntitiesTypes Method (ICoordinateSystemFeatureData)

Gets the y-axis type of entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetYAxisEntitiesTypes() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Integer

value = instance.IGetYAxisEntitiesTypes()
```

### C#

```csharp
System.int IGetYAxisEntitiesTypes()
```

### C++/CLI

```cpp
System.int IGetYAxisEntitiesTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of longs representing the y-axis type of entities as defined by [swSelectType_e](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesTypes.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [CoordinateSystemFeatureData::IGetYAxisEntitiesTypes](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~IGetYAxisEntitiesTypes.html).

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::GetYAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::GetYAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetYAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntities.html)
[ICoordinateSystemFeatureData::ISetYAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetYAxisEntities.html)
[ICoordinateSystemFeatureData::YAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YAxisEntities.html)
[ICoordinateSystemFeatureData::YFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YFlipped.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
