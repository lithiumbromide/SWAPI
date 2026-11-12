---
title: "SetFacesOrFeaturesToExclude Method (ICutListSortOptions)"
project: "SOLIDWORKS API Help"
interface: "ICutListSortOptions"
member: "SetFacesOrFeaturesToExclude"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~SetFacesOrFeaturesToExclude.html"
---

# SetFacesOrFeaturesToExclude Method (ICutListSortOptions)

Sets the faces or features to exclude from cut list sorting.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFacesOrFeaturesToExclude( _
   ByVal Entities As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICutListSortOptions
Dim Entities As System.Object
Dim value As System.Integer

value = instance.SetFacesOrFeaturesToExclude(Entities)
```

### C#

```csharp
System.int SetFacesOrFeaturesToExclude(
   System.object Entities
)
```

### C++/CLI

```cpp
System.int SetFacesOrFeaturesToExclude(
   System.Object^ Entities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entities`: Array of [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) or [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) to exclude

### Return Value

Error code as defined in [swCutListExclusionStatus_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCutListExclusionStatus_e.html)

## VBA Syntax

See [CutListSortOptions::SetFacesOrFeaturesToExclude](ms-its:sldworksapivb6.chm::/sldworks~CutListSortOptions~SetFacesOrFeaturesToExclude.html).

## Remarks

In order to avoid cut list sorting issues using [IBodyFolder::SortCutList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SortCutList.html), the Entities array must contain entities of selection type BODYFEATURE or FACE.

Faces and features you cannot exclude:

- Chamfers that remove an entire face.
- Suppressed features.
- Features that create new bodies from sketches, such as boss-extrude, revolve, and sweep.
- Certain sheet metal features.

## See Also

[ICutListSortOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions.html)
[ICutListSortOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions_members.html)
[ICutListSortOptions::GetFacesOrFeaturesToExclude Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~GetFacesOrFeaturesToExclude.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
