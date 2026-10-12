---
title: "IGetRadiatedEntities Method (ISurfaceRadiateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceRadiateFeatureData"
member: "IGetRadiatedEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~IGetRadiatedEntities.html"
---

# IGetRadiatedEntities Method (ISurfaceRadiateFeatureData)

Gets the radiated entities for this surface radiate feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRadiatedEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceRadiateFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetRadiatedEntities(Count)
```

### C#

```csharp
System.object IGetRadiatedEntities(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetRadiatedEntities(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of radiated entities

### Return Value

- in-process, unmanaged C++: Pointer to an array of radiated entities of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISurfaceRadiateFeatureData::GetRadiatedEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceRadiateFeatureData~GetRadiatedEntitiesCount.html) before calling this method to get the value of Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html)
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
