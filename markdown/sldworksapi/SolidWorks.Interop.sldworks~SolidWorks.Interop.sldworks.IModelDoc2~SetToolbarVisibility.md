---
title: "SetToolbarVisibility Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetToolbarVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetToolbarVisibility.html"
---

# SetToolbarVisibility Method (IModelDoc2)

Sets the visibility of a toolbar.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetToolbarVisibility( _
   ByVal Toolbar As System.Integer, _
   ByVal Visibility As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Toolbar As System.Integer
Dim Visibility As System.Boolean

instance.SetToolbarVisibility(Toolbar, Visibility)
```

### C#

```csharp
void SetToolbarVisibility(
   System.int Toolbar,
   System.bool Visibility
)
```

### C++/CLI

```cpp
void SetToolbarVisibility(
   System.int Toolbar,
   System.bool Visibility
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Toolbar`: Identifier of toolbar as defined in [swToolbar_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbar_e.html)
- `Visibility`: True if the toolbar is visible, false if hidden

## VBA Syntax

See [ModelDoc2::SetToolbarVisibility](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetToolbarVisibility.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetToolbarVisibility.html)
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html)
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.html)
[ISldWorks::GetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.html)
[ISldWorks::SetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.html)
[ISldWorks::ShowToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowToolbar2.html)
[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
