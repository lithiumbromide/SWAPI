---
title: "AutoBalloon2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "AutoBalloon2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon2.html"
---

# AutoBalloon2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::AutoBalloon3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~AutoBalloon3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AutoBalloon2( _
   ByVal Layout As System.Integer, _
   ByVal IgnoreMultiple As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Layout As System.Integer
Dim IgnoreMultiple As System.Boolean
Dim value As System.Object

value = instance.AutoBalloon2(Layout, IgnoreMultiple)
```

### C#

```csharp
System.object AutoBalloon2(
   System.int Layout,
   System.bool IgnoreMultiple
)
```

### C++/CLI

```cpp
System.Object^ AutoBalloon2(
   System.int Layout,
   System.bool IgnoreMultiple
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Layout`:
- `IgnoreMultiple`:

## VBA Syntax

See [DrawingDoc::AutoBalloon2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~AutoBalloon2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
