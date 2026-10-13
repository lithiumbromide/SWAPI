---
title: "InsertModelAnnotations Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertModelAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelAnnotations.html"
---

# InsertModelAnnotations Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::InsertModelAnnotations3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertModelAnnotations3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertModelAnnotations( _
   ByVal Option As System.Integer, _
   ByVal AllTypes As System.Boolean, _
   ByVal Types As System.Integer, _
   ByVal AllViews As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Option As System.Integer
Dim AllTypes As System.Boolean
Dim Types As System.Integer
Dim AllViews As System.Boolean
Dim value As System.Boolean

value = instance.InsertModelAnnotations(Option, AllTypes, Types, AllViews)
```

### C#

```csharp
System.bool InsertModelAnnotations(
   System.int Option,
   System.bool AllTypes,
   System.int Types,
   System.bool AllViews
)
```

### C++/CLI

```cpp
System.bool InsertModelAnnotations(
   System.int Option,
   System.bool AllTypes,
   System.int Types,
   System.bool AllViews
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Option`:
- `AllTypes`:
- `Types`:
- `AllViews`:

## VBA Syntax

See [DrawingDoc::InsertModelAnnotations](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertModelAnnotations.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
