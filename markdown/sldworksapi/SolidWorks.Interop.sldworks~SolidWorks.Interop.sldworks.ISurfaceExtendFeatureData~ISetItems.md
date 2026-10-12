---
title: "ISetItems Method (ISurfaceExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceExtendFeatureData"
member: "ISetItems"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~ISetItems.html"
---

# ISetItems Method (ISurfaceExtendFeatureData)

Sets the extended faces and edges for this surface-extend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetItems( _
   ByVal Count As System.Integer, _
   ByRef ItemArr As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceExtendFeatureData
Dim Count As System.Integer
Dim ItemArr As System.Object

instance.ISetItems(Count, ItemArr)
```

### C#

```csharp
void ISetItems(
   System.int Count,
   ref System.object ItemArr
)
```

### C++/CLI

```cpp
void ISetItems(
   System.int Count,
   System.Object^% ItemArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of extended items
- `ItemArr`: - in-process, unmanaged C++: Pointer to an array extended items ([faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) and [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html)
[ISurfaceExtendFeatureData::GetItemsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~GetItemsCount.html)
[ISurfaceExtendFeatureData::IGetItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~IGetItems.html)
[ISurfaceExtendFeatureData::Items Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~Items.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
