---
title: "IsModelLoaded Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IsModelLoaded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelLoaded.html"
---

# IsModelLoaded Method (IView)

Gets whether the model is loaded in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsModelLoaded() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.IsModelLoaded()
```

### C#

```csharp
System.bool IsModelLoaded()
```

### C++/CLI

```cpp
System.bool IsModelLoaded();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the model has been loaded, false if not

## VBA Syntax

See [View::IsModelLoaded](ms-its:sldworksapivb6.chm::/sldworks~View~IsModelLoaded.html).

## Remarks

If the drawing document was loaded as Detached, then the return value will be false. To load the model, use [IView::LoadModel](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~LoadModel.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IsModelOutOfDate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelOutOfDate.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
