---
title: "SetPosition Method (IBreakLine)"
project: "SOLIDWORKS API Help"
interface: "IBreakLine"
member: "SetPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~SetPosition.html"
---

# SetPosition Method (IBreakLine)

Sets the locations of the break lines in the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPosition( _
   ByVal Position1 As System.Double, _
   ByVal Position2 As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakLine
Dim Position1 As System.Double
Dim Position2 As System.Double
Dim value As System.Boolean

value = instance.SetPosition(Position1, Position2)
```

### C#

```csharp
System.bool SetPosition(
   System.double Position1,
   System.double Position2
)
```

### C++/CLI

```cpp
System.bool SetPosition(
   System.double Position1,
   System.double Position2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Position1`: Location of the first break line
- `Position2`: Location of the second break line

### Return Value

True if the break lines are positioned, false if not

## VBA Syntax

See [BreakLine::SetPosition](ms-its:sldworksapivb6.chm::/sldworks~BreakLine~SetPosition.html).

## Examples

[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)
[Create Break View (VB.NET)](Create_Broken_View_Example_VBNET.htm)
[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)

## Remarks

Call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) after calling this method.

## See Also

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.html)
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.html)
[IBreakline::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~GetPosition.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
