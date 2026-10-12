---
title: "ISetFacesToDraft Method (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "ISetFacesToDraft"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetFacesToDraft.html"
---

# ISetFacesToDraft Method (IDraftFeatureData2)

Sets the faces to which to apply the draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFacesToDraft( _
   ByVal Count As System.Short, _
   ByRef FaceArray As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim Count As System.Short
Dim FaceArray As Face2

instance.ISetFacesToDraft(Count, FaceArray)
```

### C#

```csharp
void ISetFacesToDraft(
   System.short Count,
   ref Face2 FaceArray
)
```

### C++/CLI

```cpp
void ISetFacesToDraft(
   System.short Count,
   Face2^% FaceArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces
- `FaceArray`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::GetFacesToDraftCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetFacesToDraftCount.html)
[IDraftFeatureData2::IGetFacesToDraft Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetFacesToDraft.html)
[IDraftFeatureData2::FacesToDraft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~FacesToDraft.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
