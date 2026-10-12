---
title: "IGetRevisionClouds Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetRevisionClouds"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetRevisionClouds.html"
---

# IGetRevisionClouds Method (IView)

Gets all of the revision cloud annotations in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRevisionClouds( _
   ByVal NumRevClouds As System.Integer _
) As RevisionCloud
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumRevClouds As System.Integer
Dim value As RevisionCloud

value = instance.IGetRevisionClouds(NumRevClouds)
```

### C#

```csharp
RevisionCloud IGetRevisionClouds(
   System.int NumRevClouds
)
```

### C++/CLI

```cpp
RevisionCloud^ IGetRevisionClouds(
   System.int NumRevClouds
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumRevClouds`: Number of revision cloud annotations in this view (see **Remarks**)

### Return Value

- in-process, unmanaged C++: Pointer to an array of [revision cloud annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud.html)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IView::GetRevisionCloudCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetRevisionCloudCount.html) to populate NumRevClouds.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFirstRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstRevisionCloud.html)
[IView::GetRevisionClouds Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetRevisionClouds.html)
[IView::IGetFirstRevisionCloud Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstRevisionCloud.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
