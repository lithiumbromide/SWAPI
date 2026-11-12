---
title: "GetEntitiesCount Method (ISurfaceKnitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceKnitFeatureData"
member: "GetEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~GetEntitiesCount.html"
---

# GetEntitiesCount Method (ISurfaceKnitFeatureData)

Gets the number of knit faces and surfaces for this Surface-Knit feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntitiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceKnitFeatureData
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

Number of knit entities

## VBA Syntax

See [SurfaceKnitFeatureData::GetEntitiesCount](ms-its:sldworksapivb6.chm::/sldworks~SurfaceKnitFeatureData~GetEntitiesCount.html).

## Examples

[Get Knit Surface (VBA)](Get_Knit_Surface_Data_Example_VB.htm)

## Remarks

Call this method before calling [ISurfaceKnitFeatureData::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceKnitFeatureData~IGetEntities.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.html)
[ISurfaceKnitFeatureData::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~ISetEntities.html)
[ISurfaceKnitFeatureData::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~Entities.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
