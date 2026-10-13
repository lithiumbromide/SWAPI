---
title: "GetUseDocTextFormat Method (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "GetUseDocTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetUseDocTextFormat.html"
---

# GetUseDocTextFormat Method (IProjectionArrow)

Gets whether the document default auxiliary text format is being used.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocTextFormat() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
Dim value As System.Boolean

value = instance.GetUseDocTextFormat()
```

### C#

```csharp
System.bool GetUseDocTextFormat()
```

### C++/CLI

```cpp
System.bool GetUseDocTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the documents auxiliary text formatting is used, false if not

## VBA Syntax

See [ProjectionArrow::GetUseDocTextFormat](ms-its:sldworksapivb6.chm::/sldworks~ProjectionArrow~GetUseDocTextFormat.html).

## Examples

[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)
[IProjectionArrow::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetTextFormat.html)
[IProjectionArrow::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetTextFormat.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
