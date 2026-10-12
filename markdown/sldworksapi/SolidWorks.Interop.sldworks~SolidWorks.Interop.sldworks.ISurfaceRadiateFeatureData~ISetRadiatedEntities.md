---
title: "ISetRadiatedEntities Method (ISurfaceRadiateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceRadiateFeatureData"
member: "ISetRadiatedEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~ISetRadiatedEntities.html"
---

# ISetRadiatedEntities Method (ISurfaceRadiateFeatureData)

Sets the radiated entities for this surface radiate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetRadiatedEntities( _
   ByVal Count As System.Integer, _
   ByRef DispArr As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceRadiateFeatureData
Dim Count As System.Integer
Dim DispArr As System.Object

instance.ISetRadiatedEntities(Count, DispArr)
```

### C#

```csharp
void ISetRadiatedEntities(
   System.int Count,
   ref System.object DispArr
)
```

### C++/CLI

```cpp
void ISetRadiatedEntities(
   System.int Count,
   System.Object^% DispArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of radiated entities
- `DispArr`: - in-process, unmanaged C++: Pointer to an array of radiated entities of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html)
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.html)
[ISurfaceRadiateFeatureData::GetRadiatedEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~GetRadiatedEntitiesCount.html)
[ISurfaceRadiateFeatureData::IGetRadiatedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~IGetRadiatedEntities.html)
[ISurfaceRadiateFeatureData::RadiatedEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~RadiatedEntities.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
