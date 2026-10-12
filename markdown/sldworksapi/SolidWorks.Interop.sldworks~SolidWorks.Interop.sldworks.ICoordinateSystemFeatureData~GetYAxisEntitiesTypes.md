---
title: "GetYAxisEntitiesTypes Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "GetYAxisEntitiesTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesTypes.html"
---

# GetYAxisEntitiesTypes Method (ICoordinateSystemFeatureData)

Gets the y-axis type of entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetYAxisEntitiesTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Object

value = instance.GetYAxisEntitiesTypes()
```

### C#

```csharp
System.object GetYAxisEntitiesTypes()
```

### C++/CLI

```cpp
System.Object^ GetYAxisEntitiesTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) representing the y-axis type of entities as defined by [swSelectType_e](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesTypes.html)

## VBA Syntax

See [CoordinateSystemFeatureData::GetYAxisEntitiesTypes](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~GetYAxisEntitiesTypes.html).

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSsystemFeatureData::GetYAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesCount.html)
[ICoordinateSsystemFeatureData::IGetYAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntities.html)
[ICoordinateSsystemFeatureData::IGetYAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntitiesTypes.html)
[ICoordinateSsystemFeatureData::ISetYAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetYAxisEntities.html)
[ICoordinateSsystemFeatureData::YAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YAxisEntities.html)
[ICoordinateSsystemFeatureData::YFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YFlipped.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
