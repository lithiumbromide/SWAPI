---
title: "GetRevisionCloudCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetRevisionCloudCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionCloudCount.html"
---

# GetRevisionCloudCount Method (IView)

Gets the number of revision cloud annotations in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRevisionCloudCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetRevisionCloudCount()
```

### C#

```csharp
System.int GetRevisionCloudCount()
```

### C++/CLI

```cpp
System.int GetRevisionCloudCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of revision cloud annotations in this view

## VBA Syntax

See [View::GetRevisionCloudCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetRevisionCloudCount.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFirstRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstRevisionCloud.html)
[IView::IGetFirstRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstRevisionCloud.html)
[IView::GetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionClouds.html)
[IView::IGetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetRevisionClouds.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
