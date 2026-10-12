---
title: "GetToolbarVisibility Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetToolbarVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarVisibility.html"
---

# GetToolbarVisibility Method (ISldWorks)

Gets whether this toolbar is visible.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetToolbarVisibility( _
   ByVal Toolbar As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Toolbar As System.Integer
Dim value As System.Boolean

value = instance.GetToolbarVisibility(Toolbar)
```

### C#

```csharp
System.bool GetToolbarVisibility(
   System.int Toolbar
)
```

### C++/CLI

```cpp
System.bool GetToolbarVisibility(
   System.int Toolbar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Toolbar`: Identifier of toolbar as defined in [swToolbar_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbar_e.html)

### Return Value

True if the toolbar is visible, false if it is hidden

## VBA Syntax

See [SldWorks::GetToolbarVisibility](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetToolbarVisibility.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::SetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarVisibility.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.html)
[IModelDoc2::GetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetToolbarVisibility.html)
[IModelDoc2::SetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetToolbarVisibility.html)
[ISldWorks::AddToolbar5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.html)

## Availability

SOLIDWORKS 2009 SP03, Revision Number 17.3
