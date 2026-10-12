---
title: "BlankRefGeom Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "BlankRefGeom"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~BlankRefGeom.html"
---

# BlankRefGeom Method (IModelDoc2)

Hides the selected reference geometry in the graphics window.

## Syntax

### Visual Basic (Declaration)

```vb
Sub BlankRefGeom()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.BlankRefGeom()
```

### C#

```csharp
void BlankRefGeom()
```

### C++/CLI

```cpp
void BlankRefGeom();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::BlankRefGeom](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~BlankRefGeom.html).

## Examples

[Create Replace Face Feature (C#)](Replace_Face_Example_CSharp.htm)
[Create Replace Face Feature (VB.NET)](Replace_Face_Example_VBNET.htm)
[Create Replace Face Feature (VBA)](Replace_Face_Example_VB.htm)

## Remarks

If you select a reference plane and then call this method, the plane is invisible in the graphics area. This method has the same effect as right-clicking an item and selecting **Hide** on the shortcut menu.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::UnBlankRefGeom Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~UnBlankRefGeom.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
