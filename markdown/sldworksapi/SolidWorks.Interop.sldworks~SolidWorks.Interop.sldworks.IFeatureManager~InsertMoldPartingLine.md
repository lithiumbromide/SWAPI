---
title: "InsertMoldPartingLine Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMoldPartingLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingLine.html"
---

# InsertMoldPartingLine Method (IFeatureManager)

Inserts a mold parting line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMoldPartingLine( _
   ByVal BFlipDir As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BFlipDir As System.Boolean
Dim value As Feature

value = instance.InsertMoldPartingLine(BFlipDir)
```

### C#

```csharp
Feature InsertMoldPartingLine(
   System.bool BFlipDir
)
```

### C++/CLI

```cpp
Feature^ InsertMoldPartingLine(
   System.bool BFlipDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BFlipDir`: True to flip the direction of the pull, false to not

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertMoldPartingLine](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMoldPartingLine.html).

## Remarks

Before calling this method, you must select the direction of pull and the edges for the parting line by calling [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with the following Marks:

| Selection | Mark |
| --- | --- |
| Direction of pull | 1 |
| Parting line edges | 4 |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)
[IFeatureManager::InsertMoldCoreCavitySolids Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldCoreCavitySolids.html)
[IFeatureManager::InsertMoldShutOffSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldShutOffSurface.html)
[IFeatureManager::InsertMoldCoreCavitySolids Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldCoreCavitySolids.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
