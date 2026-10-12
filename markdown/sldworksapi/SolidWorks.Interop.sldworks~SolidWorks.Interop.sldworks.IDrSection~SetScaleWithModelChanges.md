---
title: "SetScaleWithModelChanges Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SetScaleWithModelChanges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetScaleWithModelChanges.html"
---

# SetScaleWithModelChanges Method (IDrSection)

Sets whether the section line scales with changes to the model.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetScaleWithModelChanges( _
   ByVal ScaleWithChanges As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim ScaleWithChanges As System.Boolean

instance.SetScaleWithModelChanges(ScaleWithChanges)
```

### C#

```csharp
void SetScaleWithModelChanges(
   System.bool ScaleWithChanges
)
```

### C++/CLI

```cpp
void SetScaleWithModelChanges(
   System.bool ScaleWithChanges
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ScaleWithChanges`: True scales the section line with changes to the model, false does not

## VBA Syntax

See [DrSection::SetScaleWithModelChanges](ms-its:sldworksapivb6.chm::/sldworks~DrSection~SetScaleWithModelChanges.html).

## Examples

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetScaleWithModelChanges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetScaleWithModelChanges.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
