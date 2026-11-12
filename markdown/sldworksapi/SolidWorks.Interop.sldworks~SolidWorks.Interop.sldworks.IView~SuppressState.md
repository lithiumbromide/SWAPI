---
title: "SuppressState Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SuppressState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SuppressState.html"
---

# SuppressState Property (IView)

Gets or sets the view suppress state.

## Syntax

### Visual Basic (Declaration)

```vb
Property SuppressState As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

instance.SuppressState = value

value = instance.SuppressState
```

### C#

```csharp
System.int SuppressState {get; set;}
```

### C++/CLI

```cpp
property System.int SuppressState {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

- NO_SUPPRESS = 0
- HALF_SUPPRESS = 1
- FULL_SUPPRESS = 2

## VBA Syntax

See [View::SuppressState](ms-its:sldworksapivb6.chm::/sldworks~View~SuppressState.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IDrawingDoc::SuIppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SuppressView.html)
