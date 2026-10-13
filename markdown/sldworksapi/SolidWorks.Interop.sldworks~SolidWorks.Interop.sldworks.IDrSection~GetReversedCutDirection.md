---
title: "GetReversedCutDirection Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetReversedCutDirection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetReversedCutDirection.html"
---

# GetReversedCutDirection Method (IDrSection)

Gets whether the section cut direction is reversed from the default direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReversedCutDirection() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

value = instance.GetReversedCutDirection()
```

### C#

```csharp
System.bool GetReversedCutDirection()
```

### C++/CLI

```cpp
System.bool GetReversedCutDirection();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the section cut direction is reversed from the default, false if it is not

## VBA Syntax

See [DrSection::GetReversedCutDirection](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetReversedCutDirection.html).

## Examples

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::SetPartialSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetPartialSection.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
