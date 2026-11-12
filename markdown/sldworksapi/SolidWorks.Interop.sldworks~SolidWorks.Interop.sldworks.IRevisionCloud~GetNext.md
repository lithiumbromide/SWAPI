---
title: "GetNext Method (IRevisionCloud)"
project: "SOLIDWORKS API Help"
interface: "IRevisionCloud"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetNext.html"
---

# GetNext Method (IRevisionCloud)

Gets the next revision cloud in a drawing view or sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionCloud
Dim value As System.Object

value = instance.GetNext()
```

### C#

```csharp
System.object GetNext()
```

### C++/CLI

```cpp
System.Object^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud.html)

## VBA Syntax

See [RevisionCloud::GetNext](ms-its:sldworksapivb6.chm::/sldworks~RevisionCloud~GetNext.html).

## Remarks

You can traverse the revision cloud annotations in a drawing view as follows:

1. Call [IView::GetFirstRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstRevisionCloud.html) to get the first revision cloud.
2. Call this method [IView::GetRevisionCloudCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetRevisionCloudCount.html) times to access the other revision clouds.

## See Also

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.html)
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.html)
[IView::GetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionClouds.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
