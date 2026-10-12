---
title: "GetPosition Method (IBreakLine)"
project: "SOLIDWORKS API Help"
interface: "IBreakLine"
member: "GetPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~GetPosition.html"
---

# GetPosition Method (IBreakLine)

Gets the location of this break line in the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPosition( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakLine
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetPosition(Index)
```

### C#

```csharp
System.double GetPosition(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetPosition(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Break line to work with (0 or 1)

### Return Value

Location of the break line (see **Remarks**)

## VBA Syntax

See [BreakLine::GetPosition](ms-its:sldworksapivb6.chm::/sldworks~BreakLine~GetPosition.html).

## Examples

[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)
[Create Break View (VB.NET)](Create_Broken_View_Example_VBNET.htm)
[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)

## Remarks

A drawing view break consists of a pair of lines. This method gets the break line at the location indicated by the Index argument.

| If the orientation of the break is... | Then the return value is... |
| --- | --- |
| Horizontal | Y value relative to the drawing view origin (center) that indicates where the break is along the Y axis |
| Vertical | X value relative to the drawing view origin (center) that indicates where the break is along the X axis |

To determine the orientation of the break line, use [IBreakLine::Orientation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBreakLine~Orientation.html) .

## See Also

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.html)
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.html)
[IBreakline::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~SetPosition.html)

## Availability

SOLIDWORKS 2003 FCS, Revision NUmber 11.0
