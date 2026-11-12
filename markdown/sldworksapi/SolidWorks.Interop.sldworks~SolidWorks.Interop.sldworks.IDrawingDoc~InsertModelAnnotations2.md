---
title: "InsertModelAnnotations2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertModelAnnotations2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations2.html"
---

# InsertModelAnnotations2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::InsertModelAnnotations3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertModelAnnotations2( _
   ByVal Option As System.Integer, _
   ByVal AllTypes As System.Boolean, _
   ByVal Types As System.Integer, _
   ByVal AllViews As System.Boolean, _
   ByVal DuplicateDims As System.Boolean, _
   ByVal HiddenFeatureDims As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Option As System.Integer
Dim AllTypes As System.Boolean
Dim Types As System.Integer
Dim AllViews As System.Boolean
Dim DuplicateDims As System.Boolean
Dim HiddenFeatureDims As System.Boolean
Dim value As System.Boolean

value = instance.InsertModelAnnotations2(Option, AllTypes, Types, AllViews, DuplicateDims, HiddenFeatureDims)
```

### C#

```csharp
System.bool InsertModelAnnotations2(
   System.int Option,
   System.bool AllTypes,
   System.int Types,
   System.bool AllViews,
   System.bool DuplicateDims,
   System.bool HiddenFeatureDims
)
```

### C++/CLI

```cpp
System.bool InsertModelAnnotations2(
   System.int Option,
   System.bool AllTypes,
   System.int Types,
   System.bool AllViews,
   System.bool DuplicateDims,
   System.bool HiddenFeatureDims
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Option`:
- `AllTypes`:
- `Types`:
- `AllViews`:
- `DuplicateDims`:
- `HiddenFeatureDims`:

## VBA Syntax

See [DrawingDoc::InsertModelAnnotations2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertModelAnnotations2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
