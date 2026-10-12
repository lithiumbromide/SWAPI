---
title: "OnKeystroke Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnKeystroke"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnKeystroke.html"
---

# OnKeystroke Method (IPropertyManagerPage2Handler9)

Processes a keystroke that occurred on this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function OnKeystroke( _
   ByVal Wparam As System.Integer, _
   ByVal Message As System.Integer, _
   ByVal Lparam As System.Integer, _
   ByVal Id As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Wparam As System.Integer
Dim Message As System.Integer
Dim Lparam As System.Integer
Dim Id As System.Integer
Dim value As System.Boolean

value = instance.OnKeystroke(Wparam, Message, Lparam, Id)
```

### C#

```csharp
System.bool OnKeystroke(
   System.int Wparam,
   System.int Message,
   System.int Lparam,
   System.int Id
)
```

### C++/CLI

```cpp
System.bool OnKeystroke(
   System.int Wparam,
   System.int Message,
   System.int Lparam,
   System.int Id
)
```

### Parameters

- `Wparam`: wparam argument from Windows processing; indicates the keystroke that occurred

  NOTE: From the standard set of virtual keys from Windows. Refer to the Virtual Key Code information from Microsoft documentation; for example, the Alt key is VK_MENU.
- `Message`: Message being processed by Windows; one of these values:

  - WM_KEYDOWN 256 or 0x100
  - WM_KEYUP 257 or 0x101
  - WM_CHAR 258 or 0x102
  - WM_DEADCHAR 259 or 0x103
  - WM_SYSKEYDOWN 260 or 0x104
  - WM_SYSKEYUP 261 or 0x105
  - WM_SYSCHAR 262 or 0x106
  - WM_SYSDEADCHAR 263 or 0x107
- `Lparam`: lparam argument from Windows processing; bitmask containing various pieces of information; dependent on specific message
- `Id`: ID of the control that has focus when the keystroke was made; this is the ID specified when the control was created in [IPropertyManagerPage2::AddControl](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) or [IPropertyManagerPage2::IAddControl](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html) or [IPropertyManagerPage2::AddGroupBox](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.html) or [IPropertyManagerPage2::IAddGroupBox](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.html).

### Return Value

True indicates that the keystroke has been handled by the add-in and SOLIDWORKS should not continue to try to process it, false indicates that the keystroke has not been handled by the add-in and SOLIDWORKS will continue to try to process it

## VBA Syntax

See [PropertyManagerPage2Handler9::OnKeystroke](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnKeystroke.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
