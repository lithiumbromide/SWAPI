---
title: "GetOriginEntityType Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "GetOriginEntityType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetOriginEntityType.html"
---

# GetOriginEntityType Method (ICoordinateSystemFeatureData)

Gets the type of entity of the origin.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOriginEntityType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Integer

value = instance.GetOriginEntityType()
```

### C#

```csharp
System.int GetOriginEntityType()
```

### C++/CLI

```cpp
System.int GetOriginEntityType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of entity of the origin as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [CoordinateSystemFeatureData::GetOriginEntityType](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~GetOriginEntityType.html).

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData:IGetOriginEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetOriginEntity.html)
[ICoordinateSystemFeatureData:IGetOriginEntityType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetOriginEntityType.html)
[ICoordinateSystemFeatureData:ISetOriginEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetOriginEntity.html)
[ICoordinateSystemFeatureData::OriginEntity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~OriginEntity.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
