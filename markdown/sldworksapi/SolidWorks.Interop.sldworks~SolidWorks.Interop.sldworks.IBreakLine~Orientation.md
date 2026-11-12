---
title: "Orientation Property (IBreakLine)"
project: "SOLIDWORKS API Help"
interface: "IBreakLine"
member: "Orientation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Orientation.html"
---

# Orientation Property (IBreakLine)

Gets the orientation of this break line in the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Orientation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakLine
Dim value As System.Integer

value = instance.Orientation
```

### C#

```csharp
System.int Orientation {get;}
```

### C++/CLI

```cpp
property System.int Orientation {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Break orientation as defined in [swBreakLineOrientation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBreakLineOrientation_e.html)

## VBA Syntax

See [BreakLine::Orientation](ms-its:sldworksapivb6.chm::/sldworks~BreakLine~Orientation.html).

## Examples

[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)
[Create Break View (VB.NET)](Create_Broken_View_Example_VBNET.htm)
[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)

## See Also

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.html)
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.html)
[IBreakline::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~GetPosition.html)
[IBreakline::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~SetPosition.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
