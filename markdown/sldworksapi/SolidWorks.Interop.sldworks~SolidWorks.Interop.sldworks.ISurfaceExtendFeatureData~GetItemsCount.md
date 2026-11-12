---
title: "GetItemsCount Method (ISurfaceExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceExtendFeatureData"
member: "GetItemsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~GetItemsCount.html"
---

# GetItemsCount Method (ISurfaceExtendFeatureData)

Gets the number of extended faces and edges for this surface-extend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetItemsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceExtendFeatureData
Dim value As System.Integer

value = instance.GetItemsCount()
```

### C#

```csharp
System.int GetItemsCount()
```

### C++/CLI

```cpp
System.int GetItemsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of extended items

## VBA Syntax

See [SurfaceExtendFeatureData::GetItemsCount](ms-its:sldworksapivb6.chm::/sldworks~SurfaceExtendFeatureData~GetItemsCount.html).

## Remarks

Call this method before calling [ISurfaceExtendFeatureData::IGetItems](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceExtendFeatureData~IGetItems.html).

## See Also

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html)
[ISurfaceExtendFeatureData::ISetItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~ISetItems.html)
[ISurfaceExtendFeatureData::Items Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~Items.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
