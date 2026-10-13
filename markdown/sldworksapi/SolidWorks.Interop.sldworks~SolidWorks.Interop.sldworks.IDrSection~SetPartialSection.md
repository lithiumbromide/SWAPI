---
title: "SetPartialSection Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SetPartialSection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetPartialSection.html"
---

# SetPartialSection Method (IDrSection)

Sets whether this is a partial section cut.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPartialSection( _
   ByVal Partial As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim Partial As System.Boolean

instance.SetPartialSection(Partial)
```

### C#

```csharp
void SetPartialSection(
   System.bool Partial
)
```

### C++/CLI

```cpp
void SetPartialSection(
   System.bool Partial
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Partial`: True sets a partial section cut, false does not

## VBA Syntax

See [DrSection::SetPartialSection](ms-its:sldworksapivb6.chm::/sldworks~DrSection~SetPartialSection.html).

## Examples

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetPartialSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetPartialSection.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
