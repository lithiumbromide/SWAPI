---
title: "SetLabel2 Method (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "SetLabel2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLabel2.html"
---

# SetLabel2 Method (IDrSection)

Sets the label for this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLabel2( _
   ByVal Label As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim Label As System.String
Dim value As System.Integer

value = instance.SetLabel2(Label)
```

### C#

```csharp
System.int SetLabel2(
   System.string Label
)
```

### C++/CLI

```cpp
System.int SetLabel2(
   System.String^ Label
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Label`: Label for this section view

### Return Value

Value as defined in [swSetSectionLabelStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetSectionLabelStatus_e.html)

## VBA Syntax

See [DrSection::SetLabel2](ms-its:sldworksapivb6.chm::/sldworks~DrSection~SetLabel2.html).

## Examples

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## Remarks

| If the return status... | Then the operation... |
| --- | --- |
| < 0 | Failed |
| = 0 | Succeeded |
| > 0 | Succeeded. However: If you attempt to set the section label to the same value as an existing section label and the drawing standard does allow duplicate section labels, then status = 1. That is, the label is changed, but the status indicates that the label is a duplicate, which is not allowed by the drawing standard. If the dimensioning standard allows duplicate section labels, then status = 0. |

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)
[IDrSection::GetLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetLabel.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
