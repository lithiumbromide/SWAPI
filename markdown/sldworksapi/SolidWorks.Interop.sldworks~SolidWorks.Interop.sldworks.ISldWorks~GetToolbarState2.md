---
title: "GetToolbarState2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetToolbarState2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.html"
---

# GetToolbarState2 Method (ISldWorks)

Gets the state of the toolbar.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetToolbarState2( _
   ByVal Cookie As System.Integer, _
   ByVal ToolbarId As System.Integer, _
   ByVal ToolbarState As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim ToolbarId As System.Integer
Dim ToolbarState As System.Integer
Dim value As System.Boolean

value = instance.GetToolbarState2(Cookie, ToolbarId, ToolbarState)
```

### C#

```csharp
System.bool GetToolbarState2(
   System.int Cookie,
   System.int ToolbarId,
   System.int ToolbarState
)
```

### C++/CLI

```cpp
System.bool GetToolbarState2(
   System.int Cookie,
   System.int ToolbarId,
   System.int ToolbarState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Identifier of toolbar; this is the same Cookie you specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `ToolbarId`: ID of the toolbar as defined in [swToolbar_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbar_e.html)
- `ToolbarState`: Toolbar state to query as defined in [swToolbarStates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbarStates_e.html)

### Return Value

True or false based on the value specified in ToolbarState

## VBA Syntax

See [SldWorks::GetToolbarState2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetToolbarState2.html).

## Remarks

For information about using this method with the [ISwAddin](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin.html) object, see [Using ISwAddin to Create a SOLIDWORKS Add-in](sldworksAPIProgGuide.chm::/OVERVIEW/Using_SwAddin_to_Create_a_SOLIDWORKS_Addin.htm).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html)
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.html)
[ISldWorks::DragToolbarButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.html)
[ISldWorks::GetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.html)
[ISldWorks::SetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
