---
title: "InsertCenterLine2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertCenterLine2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCenterLine2.html"
---

# InsertCenterLine2 Method (IDrawingDoc)

Inserts a centerline on the selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCenterLine2() As Centerline
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As Centerline

value = instance.InsertCenterLine2()
```

### C#

```csharp
Centerline InsertCenterLine2()
```

### C++/CLI

```cpp
Centerline^ InsertCenterLine2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [ICenterLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterLine.html) object

## VBA Syntax

See [DrawingDoc::InsertCenterLine2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertCenterLine2.html).

## Examples

[Get Centerlines in Drawing (C#)](Get_Centerlines_in_Drawing_Example_CSharp.htm)
[Get Centerlines in Drawing (VB.NET)](Get_Centerlines_in_Drawing_Example_VBNET.htm)
[Get Centerlines in Drawing (VBA)](Get_Centerlines_in_Drawing_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
