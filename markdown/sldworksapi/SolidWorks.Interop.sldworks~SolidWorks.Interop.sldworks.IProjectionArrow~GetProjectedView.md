---
title: "GetProjectedView Method (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "GetProjectedView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetProjectedView.html"
---

# GetProjectedView Method (IProjectionArrow)

Gets the projected view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProjectedView() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
Dim value As System.Object

value = instance.GetProjectedView()
```

### C#

```csharp
System.object GetProjectedView()
```

### C++/CLI

```cpp
System.Object^ GetProjectedView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Projected [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) from which this projection arrow is referenced

## VBA Syntax

See [ProjectionArrow::GetProjectedView](ms-its:sldworksapivb6.chm::/sldworks~ProjectionArrow~GetProjectedView.html).

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)
[IProjectionArrow::IGetProjectedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetProjectedView.html)
[IProjectionArrow::GetView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetView.html)
[IProjectionArrow::IGetView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetView.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
