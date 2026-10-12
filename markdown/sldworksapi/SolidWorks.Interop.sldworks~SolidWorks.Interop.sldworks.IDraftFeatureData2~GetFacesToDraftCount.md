---
title: "GetFacesToDraftCount Method (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "GetFacesToDraftCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetFacesToDraftCount.html"
---

# GetFacesToDraftCount Method (IDraftFeatureData2)

Gets the number of faces that define the draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacesToDraftCount() As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Short

value = instance.GetFacesToDraftCount()
```

### C#

```csharp
System.short GetFacesToDraftCount()
```

### C++/CLI

```cpp
System.short GetFacesToDraftCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces that define the draft feature

## VBA Syntax

See [DraftFeatureData2::GetFacesToDraftCount](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~GetFacesToDraftCount.html).

## Remarks

Call this method before calling [IDraftFeatureData2::IGetFacesToDraft](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDraftFeatureData2~ISetFacesToDraft.html) to determine the size of the array for that method.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::FacesToDraft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~FacesToDraft.html)
[IDraftFeatureData2::ISetFacesToDraft Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetFacesToDraft.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
