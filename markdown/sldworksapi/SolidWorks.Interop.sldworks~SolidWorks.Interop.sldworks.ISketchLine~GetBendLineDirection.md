---
title: "GetBendLineDirection Method (ISketchLine)"
project: "SOLIDWORKS API Help"
interface: "ISketchLine"
member: "GetBendLineDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~GetBendLineDirection.html"
---

# GetBendLineDirection Method (ISketchLine)

Gets whether the sketch line is a bendline, and, if it is, the direction of the bendline.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBendLineDirection() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchLine
Dim value As System.Integer

value = instance.GetBendLineDirection()
```

### C#

```csharp
System.int GetBendLineDirection()
```

### C++/CLI

```cpp
System.int GetBendLineDirection();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Bendline direction as defined in [swBendLineDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendLineDirection_e.html)

## VBA Syntax

See [SketchLine::GetBendLineDirection](ms-its:sldworksapivb6.chm::/sldworks~SketchLine~GetBendLineDirection.html).

## Examples

[Get Direction of Bendline (C#)](Get_Direction_of_Bendline_Example_CSharp.htm)
[Get Direction of Bendline (VB.NET)](Get_Direction_of_Bendline_Example_VBNET.htm)
[Get Direction of Bendline (VBA)](Get_Direction_of_Bendline_Example_VB.htm)

## See Also

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
