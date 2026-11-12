---
title: "HideMagnifyingGlass Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "HideMagnifyingGlass"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HideMagnifyingGlass.html"
---

# HideMagnifyingGlass Method (IModelView)

Hides the Magnifying Glass tool.

## Syntax

### Visual Basic (Declaration)

```vb
Sub HideMagnifyingGlass()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView

instance.HideMagnifyingGlass()
```

### C#

```csharp
void HideMagnifyingGlass()
```

### C++/CLI

```cpp
void HideMagnifyingGlass();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelView::HideMagnifyingGlass](ms-its:sldworksapivb6.chm::/sldworks~ModelView~HideMagnifyingGlass.html).

## Examples

**Visual Basic for Applications (VBA)**

'----------------------------------------
'
' Preconditions: Model document is open.
'
' Postconditions: None
'
'----------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelView As SldWorks.ModelView
Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.**ActiveDoc**
Set swModelView = swModel.**ActiveView**

swModelView.**ShowMagnifyingGlass** -0.01928933522023, 0.004431675106825, -0.001816629754713, 2, True, True
swModelView.**MoveMagnifyingGlass** -0.01928933522023, 0.004431675106825, -0.004
swModelView.**MoveMagnifyingGlass** -0.01928933522023, 0.004431675106825, -0.016
swModelView.**HideMagnifyingGlass**

End Sub

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::MoveMagnifyingGlass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~MoveMagnifyingGlass.html)
[IModelView::ShowMagnifyingGlass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ShowMagnifyingGlass.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
