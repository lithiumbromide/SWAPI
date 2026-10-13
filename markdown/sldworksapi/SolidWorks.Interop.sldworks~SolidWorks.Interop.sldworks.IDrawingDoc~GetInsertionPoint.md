---
title: "GetInsertionPoint Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetInsertionPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetInsertionPoint.html"
---

# GetInsertionPoint Method (IDrawingDoc)

Gets the current insertion (pick) point in a drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetInsertionPoint() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Object

value = instance.GetInsertionPoint()
```

### C#

```csharp
System.object GetInsertionPoint()
```

### C++/CLI

```cpp
System.Object^ GetInsertionPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 3 doubles (x,y,z)

## VBA Syntax

See [DrawingDoc::GetInsertionPoint](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetInsertionPoint.html).

## Remarks

You might want to use [ISelectionMgr::GetSelectionPointInSketchSpace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.html) to handle multiple selections.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::IGetInsertionPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetInsertionPoint.html)
