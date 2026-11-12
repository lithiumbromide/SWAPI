---
title: "SetReversedCutDirection Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SetReversedCutDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetReversedCutDirection.html"
---

# SetReversedCutDirection Method (IDrSection)

Sets whether the section cut direction is reversed from the default.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReversedCutDirection( _
   ByVal Reversed As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim Reversed As System.Boolean

instance.SetReversedCutDirection(Reversed)
```

### C#

```csharp
void SetReversedCutDirection(
   System.bool Reversed
)
```

### C++/CLI

```cpp
void SetReversedCutDirection(
   System.bool Reversed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Reversed`: True reverses the section cut direction from the default, false does not

## VBA Syntax

See [DrSection::SetReversedCutDirection](ms-its:sldworksapivb6.chm::/sldworks~DrSection~SetReversedCutDirection.html).

## Examples

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## Remarks

Call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) after calling this method.

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetReversedCutDirection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetReversedCutDirection.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
