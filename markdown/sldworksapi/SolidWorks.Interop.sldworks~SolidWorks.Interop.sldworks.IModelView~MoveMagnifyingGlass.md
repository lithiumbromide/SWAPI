---
title: "MoveMagnifyingGlass Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "MoveMagnifyingGlass"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~MoveMagnifyingGlass.html"
---

# MoveMagnifyingGlass Method (IModelView)

Moves Magnifying Glass tool to the specified coordinates.

## Syntax

### Visual Basic (Declaration)

```vb
Sub MoveMagnifyingGlass( _
   ByVal Ptx As System.Double, _
   ByVal Pty As System.Double, _
   ByVal Ptz As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim Ptx As System.Double
Dim Pty As System.Double
Dim Ptz As System.Double

instance.MoveMagnifyingGlass(Ptx, Pty, Ptz)
```

### C#

```csharp
void MoveMagnifyingGlass(
   System.double Ptx,
   System.double Pty,
   System.double Ptz
)
```

### C++/CLI

```cpp
void MoveMagnifyingGlass(
   System.double Ptx,
   System.double Pty,
   System.double Ptz
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ptx`: x coordinate
- `Pty`: y coordinate
- `Ptz`: z coordinate

## VBA Syntax

See [ModelView::MoveMagnifyingGlass](ms-its:sldworksapivb6.chm::/sldworks~ModelView~MoveMagnifyingGlass.html).

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
[IModelView::HideMagnifyingGlass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HideMagnifyingGlass.html)
[IModelView::ShowMagnifyingGlass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ShowMagnifyingGlass.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
