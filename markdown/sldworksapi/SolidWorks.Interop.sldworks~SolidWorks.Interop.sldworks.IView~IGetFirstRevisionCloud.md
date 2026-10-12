---
title: "IGetFirstRevisionCloud Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetFirstRevisionCloud"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstRevisionCloud.html"
---

# IGetFirstRevisionCloud Method (IView)

Gets the first revision cloud annotation in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstRevisionCloud() As RevisionCloud
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As RevisionCloud

value = instance.IGetFirstRevisionCloud()
```

### C#

```csharp
RevisionCloud IGetFirstRevisionCloud()
```

### C++/CLI

```cpp
RevisionCloud^ IGetFirstRevisionCloud();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an

  [IRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFirstRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstRevisionCloud.html)
[IView::GetRevisionCloudCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionCloudCount.html)
[IView::GetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionClouds.html)
[IView::IGetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetRevisionClouds.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
