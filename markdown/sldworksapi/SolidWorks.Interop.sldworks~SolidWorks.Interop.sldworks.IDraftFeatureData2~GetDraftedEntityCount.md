---
title: "GetDraftedEntityCount Method (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "GetDraftedEntityCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetDraftedEntityCount.html"
---

# GetDraftedEntityCount Method (IDraftFeatureData2)

Gets the number of drafted entities for this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDraftedEntityCount() As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Short

value = instance.GetDraftedEntityCount()
```

### C#

```csharp
System.short GetDraftedEntityCount()
```

### C++/CLI

```cpp
System.short GetDraftedEntityCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of drafted entities

## VBA Syntax

See [DraftFeatureData2::GetDraftedEntityCount](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~GetDraftedEntityCount.html).

## Remarks

Call this method before calling [IDraftFeatureData2::IGetDraftedEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDraftFeatureData2~IGetDraftedEntities.html) to determine the size of the array for that method.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::GetDraftedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetDraftedEntities.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
