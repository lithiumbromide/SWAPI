---
title: "GetPartialSection Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "GetPartialSection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetPartialSection.html"
---

# GetPartialSection Method (IDrSection)

Gets whether this is a partial section cut.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartialSection() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

value = instance.GetPartialSection()
```

### C#

```csharp
System.bool GetPartialSection()
```

### C++/CLI

```cpp
System.bool GetPartialSection();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this is a partial section cut, false if it is not

## VBA Syntax

See [DrSection::GetPartialSection](ms-its:sldworksapivb6.chm::/sldworks~DrSection~GetPartialSection.html).

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
