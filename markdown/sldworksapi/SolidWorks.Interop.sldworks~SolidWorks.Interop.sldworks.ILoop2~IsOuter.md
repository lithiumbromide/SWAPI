---
title: "IsOuter Method (ILoop2)"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: "IsOuter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~IsOuter.html"
---

# IsOuter Method (ILoop2)

Indicates whether the loop is the outermost loop on the face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsOuter() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
Dim value As System.Boolean

value = instance.IsOuter()
```

### C#

```csharp
System.bool IsOuter()
```

### C++/CLI

```cpp
System.bool IsOuter();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the loop is the outermost loop, false if not

## VBA Syntax

See [Loop2::IsOuter](ms-its:sldworksapivb6.chm::/sldworks~Loop2~IsOuter.html).

## Examples

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)
[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)
[Get Loops (VBA)](Get_Loops_Example_VB.htm)
[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)
[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)
[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## Remarks

Some situations exist where no clear outer loop is defined. For example, the cylindrical face of an extruded circle has two loops that could be considered outer loops.

## See Also

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
