---
title: "IsDetailingMode Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IsDetailingMode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IsDetailingMode.html"
---

# IsDetailingMode Method (IDrawingDoc)

Gets whether this drawing is in detailing mode.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDetailingMode() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Boolean

value = instance.IsDetailingMode()
```

### C#

```csharp
System.bool IsDetailingMode()
```

### C++/CLI

```cpp
System.bool IsDetailingMode();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if drawing is in detailing mode, false if not

## VBA Syntax

See [DrawingDoc::IsDetailingMode](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IsDetailingMode.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
