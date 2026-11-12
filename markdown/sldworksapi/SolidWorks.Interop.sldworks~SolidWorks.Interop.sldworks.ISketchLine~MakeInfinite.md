---
title: "MakeInfinite Method (ISketchLine)"
project: "SOLIDWORKS API Help"
interface: "ISketchLine"
member: "MakeInfinite"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~MakeInfinite.html"
---

# MakeInfinite Method (ISketchLine)

Makes a line infinite.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeInfinite() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchLine
Dim value As System.Boolean

value = instance.MakeInfinite()
```

### C#

```csharp
System.bool MakeInfinite()
```

### C++/CLI

```cpp
System.bool MakeInfinite();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the line is changed to infinite, false if not

## VBA Syntax

See [SketchLine::MakeInfinite](ms-its:sldworksapivb6.chm::/sldworks~SketchLine~MakeInfinite.html).

## Examples

[Make Line Infinite (VBA)](Make_Line_Infinite_Example_VB.htm)

## Remarks

When you change a line from finite to infinite, you cannot change it back to finite.

## See Also

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.html)
[ISketchLine::Infinite Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~Infinite.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
