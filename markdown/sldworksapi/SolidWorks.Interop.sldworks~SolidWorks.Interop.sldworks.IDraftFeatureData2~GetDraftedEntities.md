---
title: "GetDraftedEntities Method (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "GetDraftedEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetDraftedEntities.html"
---

# GetDraftedEntities Method (IDraftFeatureData2)

Gets the drafted entities (faces or edges) for this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDraftedEntities() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Object

value = instance.GetDraftedEntities()
```

### C#

```csharp
System.object GetDraftedEntities()
```

### C++/CLI

```cpp
System.Object^ GetDraftedEntities();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)

## VBA Syntax

See [DraftFeatureData2::GetDraftedEntities](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~GetDraftedEntities.html).

## Examples

[Get Faces Affected by Draft Feature (VBA)](Get_Faces_Affected_by_Draft_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::IGetDraftedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetDraftedEntities.html)
[IDraftFeatureData2::GetDraftedEntityCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetDraftedEntityCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
