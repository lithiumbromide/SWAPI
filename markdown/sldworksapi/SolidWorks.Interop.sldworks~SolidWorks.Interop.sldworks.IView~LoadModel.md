---
title: "LoadModel Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "LoadModel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~LoadModel.html"
---

# LoadModel Method (IView)

Loads the model if the model has not already been loaded for this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function LoadModel() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.LoadModel()
```

### C#

```csharp
System.int LoadModel()
```

### C++/CLI

```cpp
System.int LoadModel();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

0 if the model was loaded, -1 if not

## VBA Syntax

See [View::LoadModel](ms-its:sldworksapivb6.chm::/sldworks~View~LoadModel.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IsModelLoaded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelLoaded.html)
[IView::IsModelOutOfDate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelOutOfDate.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
