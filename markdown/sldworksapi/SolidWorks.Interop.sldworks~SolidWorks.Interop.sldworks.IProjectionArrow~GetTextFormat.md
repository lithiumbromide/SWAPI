---
title: "GetTextFormat Method (IProjectionArrow)"
project: "SOLIDWORKS API Help"
interface: "IProjectionArrow"
member: "GetTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetTextFormat.html"
---

# GetTextFormat Method (IProjectionArrow)

Gets the format of the text for this projection arrow.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTextFormat() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionArrow
Dim value As System.Object

value = instance.GetTextFormat()
```

### C#

```csharp
System.object GetTextFormat()
```

### C++/CLI

```cpp
System.Object^ GetTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Text format](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html)

## VBA Syntax

See [ProjectionArrow::GetTextFormat](ms-its:sldworksapivb6.chm::/sldworks~ProjectionArrow~GetTextFormat.html).

## Examples

[Get Arrow in Projected View (C#)](Get_Arrow_in_Projected_View_Example_CSharp.htm)
[Get Arrow in Projected View (VB.NET)](Get_Arrow_in_Projected_View_Example_VBNET.htm)
[Get Arrow in Projected View (VBA)](Get_Arrow_in_Projected_View_Example_VB.htm)

## See Also

[IProjectionArrow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow.html)
[IProjectionArrow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html)
[IProjectionArrow::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~IGetTextFormat.html)
[IProjectionArrow::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow~GetUseDocTextFormat.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
