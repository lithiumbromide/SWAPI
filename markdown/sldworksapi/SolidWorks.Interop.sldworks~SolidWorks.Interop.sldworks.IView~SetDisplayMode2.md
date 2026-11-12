---
title: "SetDisplayMode2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SetDisplayMode2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode2.html"
---

# SetDisplayMode2 Method (IView)

Obsolete. Superseded by [IView::SetDisplayMode3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~SetDisplayMode3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDisplayMode2( _
   ByVal Mode As System.Integer, _
   ByVal Facetted As System.Boolean, _
   ByVal Edges As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Mode As System.Integer
Dim Facetted As System.Boolean
Dim Edges As System.Boolean
Dim value As System.Boolean

value = instance.SetDisplayMode2(Mode, Facetted, Edges)
```

### C#

```csharp
System.bool SetDisplayMode2(
   System.int Mode,
   System.bool Facetted,
   System.bool Edges
)
```

### C++/CLI

```cpp
System.bool SetDisplayMode2(
   System.int Mode,
   System.bool Facetted,
   System.bool Edges
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Mode`:
- `Facetted`:
- `Edges`:

## VBA Syntax

See [View::SetDisplayMode2](ms-its:sldworksapivb6.chm::/sldworks~View~SetDisplayMode2.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
