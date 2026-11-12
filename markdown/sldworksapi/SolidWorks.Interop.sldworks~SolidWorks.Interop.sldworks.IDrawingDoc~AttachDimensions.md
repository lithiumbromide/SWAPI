---
title: "AttachDimensions Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "AttachDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AttachDimensions.html"
---

# AttachDimensions Method (IDrawingDoc)

Attaches unattached dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AttachDimensions()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.AttachDimensions()
```

### C#

```csharp
void AttachDimensions()
```

### C++/CLI

```cpp
void AttachDimensions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::AttachDimensions](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~AttachDimensions.html).

## Remarks

This method tries to reattach dimensions, for example, in an imported DXF file.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::Dimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Dimensions.html)
[IDrawingDoc::InsertBaseDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertBaseDim.html)
[IDrawingDoc::InsertModelAnnotations3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.html)
[IDrawingDoc::InsertModelDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelDimensions.html)
