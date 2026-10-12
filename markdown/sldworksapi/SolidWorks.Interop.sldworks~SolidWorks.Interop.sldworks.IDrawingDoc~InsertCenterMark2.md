---
title: "InsertCenterMark2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertCenterMark2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCenterMark2.html"
---

# InsertCenterMark2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::InsertCenterMark3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertCenterMark3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCenterMark2( _
   ByVal Style As System.Integer, _
   ByVal Propagate As System.Boolean _
) As CenterMark
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Style As System.Integer
Dim Propagate As System.Boolean
Dim value As CenterMark

value = instance.InsertCenterMark2(Style, Propagate)
```

### C#

```csharp
CenterMark InsertCenterMark2(
   System.int Style,
   System.bool Propagate
)
```

### C++/CLI

```cpp
CenterMark^ InsertCenterMark2(
   System.int Style,
   System.bool Propagate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Style`: Style as defined in [swCenterMarkStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkStyle_e.html)
- `Propagate`: True if the center mark should propagate throughout the pattern, false if not

### Return Value

Pointer to the [centermark](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark.html) object

## VBA Syntax

See [DrawingDoc::InsertCenterMark2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertCenterMark2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
