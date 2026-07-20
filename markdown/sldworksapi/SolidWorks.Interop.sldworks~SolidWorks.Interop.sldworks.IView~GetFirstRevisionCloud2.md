---
title: "GetFirstRevisionCloud2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstRevisionCloud2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstRevisionCloud2.html"
---

# GetFirstRevisionCloud2 Method (IView)

Gets the first revision cloud annotation in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstRevisionCloud2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstRevisionCloud2()
```

### C#

```csharp
System.object GetFirstRevisionCloud2()
```

### C++/CLI

```cpp
System.Object^ GetFirstRevisionCloud2();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

[IRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud.html)

## VBA Syntax

See

[View::GetFirstRevisionCloud2](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstRevisionCloud2.html)

.

## Remarks

This method obsoletes IView::GetFirstRevisionCloud by supporting inactive sheets.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetRevisionCloudCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionCloudCount.html)

[IView::GetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionClouds.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
