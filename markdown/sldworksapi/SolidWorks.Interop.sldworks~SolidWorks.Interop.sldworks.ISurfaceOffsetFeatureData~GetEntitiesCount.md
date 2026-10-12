---
title: "GetEntitiesCount Method (ISurfaceOffsetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceOffsetFeatureData"
member: "GetEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~GetEntitiesCount.html"
---

# GetEntitiesCount Method (ISurfaceOffsetFeatureData)

Gets the number of offset surfaces and faces for this surface offset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntitiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceOffsetFeatureData
Dim value As System.Integer

value = instance.GetEntitiesCount()
```

### C#

```csharp
System.int GetEntitiesCount()
```

### C++/CLI

```cpp
System.int GetEntitiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of offset surfaces and faces

## VBA Syntax

See [SurfaceOffsetFeatureData::GetEntitiesCount](ms-its:sldworksapivb6.chm::/sldworks~SurfaceOffsetFeatureData~GetEntitiesCount.html).

## Examples

[Get Offset Surface Data (VBA)](Get_Offset_Surface_Data_Example_VB.htm)
[Get Offset Surface Data (VB.NET)](Get_Offset_Surface_Data_Example_VBNET.htm)
[Get Offset Surface Data (C#)](Get_Offset_Surface_Data_Example_CSharp.htm)

## See Also

[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.html)
[ISurfaceOffsetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.html)
[ISurfaceOffsetFeatureData::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~ISetEntities.html)
[ISurfaceOffsetFeatureData::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Entities.html)
[ISurfaceOffsetFeatureData::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~IGetEntities.html)

## Availability

SOLIDWORKS 2012 SP04, Revision Number 20.4
