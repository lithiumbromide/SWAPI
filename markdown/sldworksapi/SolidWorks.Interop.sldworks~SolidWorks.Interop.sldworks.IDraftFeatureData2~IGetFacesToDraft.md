---
title: "IGetFacesToDraft Method (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "IGetFacesToDraft"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetFacesToDraft.html"
---

# IGetFacesToDraft Method (IDraftFeatureData2)

Gets the faces that define this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFacesToDraft( _
   ByVal Count As System.Short _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim Count As System.Short
Dim value As Face2

value = instance.IGetFacesToDraft(Count)
```

### C#

```csharp
Face2 IGetFacesToDraft(
   System.short Count
)
```

### C++/CLI

```cpp
Face2^ IGetFacesToDraft(
   System.short Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IDraftFeatureData2::GetFacesToDraftCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDraftFeatureData2~GetFacesToDraftCount.html) to determine the size of returned array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::ISetFacesToDraft Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetFacesToDraft.html)
[IDraftFeatureData2::FacesToDraft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~FacesToDraft.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
