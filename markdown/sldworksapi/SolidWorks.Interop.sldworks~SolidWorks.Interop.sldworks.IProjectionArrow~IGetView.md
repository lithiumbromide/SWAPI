---
title: "IGetView Method (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "IGetView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetView.html"
---

# IGetView Method (IProjectionArrow)

Gets the base drawing view for this projection arrow.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetView() As View
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
Dim value As View

value = instance.IGetView()
```

### C#

```csharp
View IGetView()
```

### C++/CLI

```cpp
View^ IGetView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Base drawing [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) object from which this projection arrow is referenced

## VBA Syntax

See [ProjectionArrow::IGetView](ms-its:sldworksapivb6.chm::/sldworks~ProjectionArrow~IGetView.html).

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)
[IProjectionArrow::GetView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetView.html)
[IProjectionArrow::GetProjectedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetProjectedView.html)
[IProjectionArrow::IGetProjectedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetProjectedView.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
