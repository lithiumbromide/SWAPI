---
title: "GetPolyLineCount2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetPolyLineCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolyLineCount2.html"
---

# GetPolyLineCount2 Method (IView)

Obsolete. Superseded by [IView::GetPolyLineCount5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetPolyLineCount5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPolyLineCount2( _
   ByRef PointCount As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim PointCount As System.Integer
Dim value As System.Integer

value = instance.GetPolyLineCount2(PointCount)
```

### C#

```csharp
System.int GetPolyLineCount2(
   out System.int PointCount
)
```

### C++/CLI

```cpp
System.int GetPolyLineCount2(
   [Out] System.int PointCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointCount`:

## VBA Syntax

See [View::GetPolyLineCount2](ms-its:sldworksapivb6.chm::/sldworks~View~GetPolyLineCount2.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
