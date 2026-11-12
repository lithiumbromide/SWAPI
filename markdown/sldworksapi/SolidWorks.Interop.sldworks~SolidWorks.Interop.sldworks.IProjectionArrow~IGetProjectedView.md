---
title: "IGetProjectedView Method (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "IGetProjectedView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetProjectedView.html"
---

# IGetProjectedView Method (IProjectionArrow)

Gets the projected view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetProjectedView() As View
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
Dim value As View

value = instance.IGetProjectedView()
```

### C#

```csharp
View IGetProjectedView()
```

### C++/CLI

```cpp
View^ IGetProjectedView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Projected [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) from which this projection arrow is referenced

## VBA Syntax

See [ProjectionArrow::IGetProjectedView](ms-its:sldworksapivb6.chm::/sldworks~ProjectionArrow~IGetProjectedView.html).

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)
[IProjectionArrow::GetProjectedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetProjectedView.html)
[IProjectionArrow::GetView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetView.html)
[IProjectionArrow::IGetView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetView.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
