---
title: "GetLabel Method (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "GetLabel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetLabel.html"
---

# GetLabel Method (IProjectionArrow)

Gets the label for this view's projection arrow.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLabel() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
Dim value As System.String

value = instance.GetLabel()
```

### C#

```csharp
System.string GetLabel()
```

### C++/CLI

```cpp
System.String^ GetLabel();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Label for this projection arrow

## VBA Syntax

See [ProjectionArrow::GetLabel](ms-its:sldworksapivb6.chm::/sldworks~ProjectionArrow~GetLabel.html).

## Examples

[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)
[IProjectionArrow::SetLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~SetLabel.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
