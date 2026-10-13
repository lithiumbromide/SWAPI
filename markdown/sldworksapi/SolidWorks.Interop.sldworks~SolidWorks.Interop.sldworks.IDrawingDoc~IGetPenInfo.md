---
title: "IGetPenInfo Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IGetPenInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetPenInfo.html"
---

# IGetPenInfo Method (IDrawingDoc)

Gets information about the pens used in SOLIDWORKS.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPenInfo() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Integer

value = instance.IGetPenInfo()
```

### C#

```csharp
System.int IGetPenInfo()
```

### C++/CLI

```cpp
System.int IGetPenInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-porcess, unmanaged C++: Pointer to an array of longs (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value is the following array of longs: **[** `font, weight, color` **]**

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GetPenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetPenCount.html)
[IDrawingDoc::GetPenInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetPenInfo.html)
