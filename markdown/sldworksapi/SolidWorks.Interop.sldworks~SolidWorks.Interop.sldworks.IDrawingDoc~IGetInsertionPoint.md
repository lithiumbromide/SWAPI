---
title: "IGetInsertionPoint Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IGetInsertionPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetInsertionPoint.html"
---

# IGetInsertionPoint Method (IDrawingDoc)

Gets the current insertion (pick) point in a drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetInsertionPoint() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Double

value = instance.IGetInsertionPoint()
```

### C#

```csharp
System.double IGetInsertionPoint()
```

### C++/CLI

```cpp
System.double IGetInsertionPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of 3 doubles (x,y,z)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Examples

You might want to use [ISelectionMgr::IGetSelectionPointInSketchSpace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.html) to handle multiple selections.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GetInsertionPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetInsertionPoint.html)
