---
title: "GetRevisionClouds Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetRevisionClouds"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionClouds.html"
---

# GetRevisionClouds Method (IView)

Gets all of the revision cloud annotations in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRevisionClouds() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetRevisionClouds()
```

### C#

```csharp
System.object GetRevisionClouds()
```

### C++/CLI

```cpp
System.Object^ GetRevisionClouds();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud.html)s

## VBA Syntax

See [View::GetRevisionClouds](ms-its:sldworksapivb6.chm::/sldworks~View~GetRevisionClouds.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFirstRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstRevisionCloud.html)
[IView::GetRevisionCloudCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionCloudCount.html)
[IView::IGetFirstRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstRevisionCloud.html)
[IView::IGetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetRevisionClouds.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
