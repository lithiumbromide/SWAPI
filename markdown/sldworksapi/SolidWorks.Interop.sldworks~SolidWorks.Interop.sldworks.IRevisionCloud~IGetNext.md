---
title: "IGetNext Method (IRevisionCloud)"
project: "SOLIDWORKS API Help"
interface: "IRevisionCloud"
member: "IGetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~IGetNext.html"
---

# IGetNext Method (IRevisionCloud)

Gets the next revision cloud in a drawing view or sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNext() As RevisionCloud
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionCloud
Dim value As RevisionCloud

value = instance.IGetNext()
```

### C#

```csharp
RevisionCloud IGetNext()
```

### C++/CLI

```cpp
RevisionCloud^ IGetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an [IRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

You can traverse the revision cloud annotations in a drawing view as follows:

1. Call [IView::IGetFirstRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetFirstRevisionCloud.html) to get the first revision cloud.
2. Call this method [IView::GetRevisionCloudCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetRevisionCloudCount.html) times to access the other revision clouds.

## See Also

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.html)
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.html)
[IView::IGetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetRevisionClouds.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
