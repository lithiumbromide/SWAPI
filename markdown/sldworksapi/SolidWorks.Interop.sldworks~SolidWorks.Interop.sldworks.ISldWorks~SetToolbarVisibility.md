---
title: "SetToolbarVisibility Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetToolbarVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarVisibility.html"
---

# SetToolbarVisibility Method (ISldWorks)

Sets whether the specified toolbar is visible.

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
Dim instance As ISldWorks
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
- `Visibility`: True to show the toolbar, false to hide it

## VBA Syntax

See [SldWorks::SetToolbarVisibility](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetToolbarVisibility.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarVisibility.html)
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)
[ISldWorks::ShowToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowToolbar2.html)
[IModelDoc2::GetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetToolbarVisibility.html)
[IModelDoc2::SetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetToolbarVisibility.html)
[ISldWorks::AddToolbar5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.html)

## Availability

SOLIDWORKS 2009 SP03, Revision Number 17.3
