---
title: "SetToolbarDock2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetToolbarDock2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.html"
---

# SetToolbarDock2 Method (ISldWorks)

Sets the docking state of the toolbar.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetToolbarDock2( _
   ByVal Cookie As System.Integer, _
   ByVal ToolbarId As System.Integer, _
   ByVal DockingState As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim ToolbarId As System.Integer
Dim DockingState As System.Integer
Dim value As System.Boolean

value = instance.SetToolbarDock2(Cookie, ToolbarId, DockingState)
```

### C#

```csharp
System.bool SetToolbarDock2(
   System.int Cookie,
   System.int ToolbarId,
   System.int DockingState
)
```

### C++/CLI

```cpp
System.bool SetToolbarDock2(
   System.int Cookie,
   System.int ToolbarId,
   System.int DockingState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Identifier of toolbar; this is the same cookie you specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `ToolbarId`: ID of the toolbar as defined in [swToolbar_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbar_e.html)
- `DockingState`: Docking state of the toolbar as defined in [swToolbarDockStatePosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbarDockStatePosition_e.html)

### Return Value

True if the docking state of the toolbar is set, false if not

## VBA Syntax

See [SldWorks::SetToolbarDock2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetToolbarDock2.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html)
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.html)
[ISldWorks::GetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.html)
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)
[ISldWorks::DragToolbarButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
