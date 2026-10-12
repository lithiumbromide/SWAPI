---
title: "Toolbars Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "Toolbars"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Toolbars.html"
---

# Toolbars Method (IModelDoc2)

Turns the specified SOLIDWORKS toolbars on and off.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Toolbars( _
   ByVal M As System.Boolean, _
   ByVal Vw As System.Boolean, _
   ByVal SkMain As System.Boolean, _
   ByVal Sk As System.Boolean, _
   ByVal Feat As System.Boolean, _
   ByVal Constr As System.Boolean, _
   ByVal Macro As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim M As System.Boolean
Dim Vw As System.Boolean
Dim SkMain As System.Boolean
Dim Sk As System.Boolean
Dim Feat As System.Boolean
Dim Constr As System.Boolean
Dim Macro As System.Boolean

instance.Toolbars(M, Vw, SkMain, Sk, Feat, Constr, Macro)
```

### C#

```csharp
void Toolbars(
   System.bool M,
   System.bool Vw,
   System.bool SkMain,
   System.bool Sk,
   System.bool Feat,
   System.bool Constr,
   System.bool Macro
)
```

### C++/CLI

```cpp
void Toolbars(
   System.bool M,
   System.bool Vw,
   System.bool SkMain,
   System.bool Sk,
   System.bool Feat,
   System.bool Constr,
   System.bool Macro
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `M`: True for main toolbar on, false for off
- `Vw`: True for view manipulation toolbar on, false for off
- `SkMain`: RUE for main sketch toolbar on, false for off
- `Sk`: True for sketch entity toolbar on, false for off
- `Feat`: True for feature toolbar on, false for off
- `Constr`: True for relationships toolbar on, false for off
- `Macro`: True for macro toolbar on, false for off

## VBA Syntax

See [ModelDoc2::Toolbars](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~Toolbars.html).

## Remarks

See [IModelDoc2::SetToolbarVisibility](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetToolbarVisibility.html) for control of all SOLIDWORKS toolbars.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetToolbarVisibility.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.html)
[ISldWorks::ShowToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowToolbar2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
