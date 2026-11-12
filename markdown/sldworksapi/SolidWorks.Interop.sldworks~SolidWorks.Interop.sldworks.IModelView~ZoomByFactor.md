---
title: "ZoomByFactor Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "ZoomByFactor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ZoomByFactor.html"
---

# ZoomByFactor Method (IModelView)

Modifies the zoom factor for the model view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ZoomByFactor( _
   ByVal Factor As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim Factor As System.Double

instance.ZoomByFactor(Factor)
```

### C#

```csharp
void ZoomByFactor(
   System.double Factor
)
```

### C++/CLI

```cpp
void ZoomByFactor(
   System.double Factor
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Factor`: Zoom factor

## VBA Syntax

See [ModelView::ZoomByFactor](ms-its:sldworksapivb6.chm::/sldworks~ModelView~ZoomByFactor.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)

## Remarks

The zoom factor should be in the range 0.0 < factor < 2.0. For factor greater than 1, the model view is zoomed in, for factor less than 1 the model view is zoomed out.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
