---
title: "GetRadiatedEntitiesCount Method (ISurfaceRadiateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceRadiateFeatureData"
member: "GetRadiatedEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~GetRadiatedEntitiesCount.html"
---

# GetRadiatedEntitiesCount Method (ISurfaceRadiateFeatureData)

Gets the number of radiated entities for this surface radiate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRadiatedEntitiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceRadiateFeatureData
Dim value As System.Integer

value = instance.GetRadiatedEntitiesCount()
```

### C#

```csharp
System.int GetRadiatedEntitiesCount()
```

### C++/CLI

```cpp
System.int GetRadiatedEntitiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of radiated entities

## VBA Syntax

See [SurfaceRadiateFeatureData::GetRadiatedEntitiesCount](ms-its:sldworksapivb6.chm::/sldworks~SurfaceRadiateFeatureData~GetRadiatedEntitiesCount.html).

## Examples

See the [ISurfaceRadiateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html) examples.

## Remarks

Call this method before calling [ISurfaceRadiateFeatureData::IGetRadiatedEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceRadiateFeatureData~IGetRadiatedEntities.html) to get the size of the array for that method.

## See Also

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html)
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.html)
[ISurfaceRadiateFeatureData::ISetRadiatedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~ISetRadiatedEntities.html)
[ISurfaceRadiateFeatureData::RadiatedEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~RadiatedEntities.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
