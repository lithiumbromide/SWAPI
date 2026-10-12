---
title: "SetAutoHatch Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SetAutoHatch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetAutoHatch.html"
---

# SetAutoHatch Method (IDrSection)

Sets whether auto hatching is enabled for the section view resulting from this section cut.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAutoHatch( _
   ByVal AutoHatch As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim AutoHatch As System.Boolean

instance.SetAutoHatch(AutoHatch)
```

### C#

```csharp
void SetAutoHatch(
   System.bool AutoHatch
)
```

### C++/CLI

```cpp
void SetAutoHatch(
   System.bool AutoHatch
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AutoHatch`: True enables auto hatching for the section view, false disables it

## VBA Syntax

See [DrSection::SetAutoHatch](ms-its:sldworksapivb6.chm::/sldworks~DrSection~SetAutoHatch.html).

## Examples

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## Remarks

Automatic hatching applies only to assembly section views. For section views of parts, this method has no effect.

When the auto hatching setting is changed, regenerate the section view to see the results of this change in the user interface.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetAutoHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetAutoHatch.html)
[IDrSection::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ScaleHatchPattern.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
