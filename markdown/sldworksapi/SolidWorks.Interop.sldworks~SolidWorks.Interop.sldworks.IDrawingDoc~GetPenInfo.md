---
title: "GetPenInfo Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetPenInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetPenInfo.html"
---

# GetPenInfo Method (IDrawingDoc)

Gets information about the pens used in SOLIDWORKS.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPenInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Object

value = instance.GetPenInfo()
```

### C#

```csharp
System.object GetPenInfo()
```

### C++/CLI

```cpp
System.Object^ GetPenInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing an array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm) and see **Remarks**)

## VBA Syntax

See [DrawingDoc::GetPenInfo](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetPenInfo.html).

## Remarks

The return value is the following array: **[** `font, weight, color` **]**

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GetPenInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetPenInfo.html)
[IDrawingDoc::IGetPenInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetPenInfo.html)
