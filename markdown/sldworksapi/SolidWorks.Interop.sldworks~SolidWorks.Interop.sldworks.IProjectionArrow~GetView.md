---
title: "GetView Method (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "GetView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetView.html"
---

# GetView Method (IProjectionArrow)

Gets the base drawing view for this projection arrow.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetView() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
Dim value As System.Object

value = instance.GetView()
```

### C#

```csharp
System.object GetView()
```

### C++/CLI

```cpp
System.Object^ GetView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Base drawing [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) object from which this projection arrow is referenced

## VBA Syntax

See [ProjectionArrow::GetView](ms-its:sldworksapivb6.chm::/sldworks~ProjectionArrow~GetView.html).

## Examples

[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)
[IProjectionArrow::IGetView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetView.html)
[IProjectionArrow::GetProjectedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetProjectedView.html)
[IProjectionArrow::IGetProjectedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetProjectedView.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
