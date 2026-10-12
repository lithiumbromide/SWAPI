---
title: "OnKeystroke Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnKeystroke"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnKeystroke.html"
---

# OnKeystroke Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnKeystroke](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnKeystroke.html).

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
Dim instance As IPropertyManagerPage2Handler5
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

  - WM_KEYDOWN 0x0100
  - WM_KEYUP 0x0101
  - WM_CHAR 0x0102
  - WM_DEADCHAR 0x0103
  - WM_SYSKEYDOWN 0x0104
  - WM_SYSKEYUP 0x0105
  - WM_SYSCHAR 0x0106
  - WM_SYSDEADCHAR 0x0107
- `Lparam`: lparam argument from Windows processing; bitmask containing various pieces of information; dependent on specific message
- `Id`: ID of the control that has focus when the keystroke was made; this is the ID specified when the control was created in [IPropertyManagerPage2::AddControl](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddControl.html) or [IPropertyManagerPage2::IAddControl](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddControl.html) or [IPropertyManagerPage2::AddGroupBox](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.html) or [IPropertyManagerPage2::IAddGroupBox](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~IAddGroupBox.html).

### Return Value

True indicates that the keystroke has been handled by the add-in and SOLIDWORKS should not continue to try to process it, false indicates that the keystroke has not been handled by the add-in and SOLIDWORKS will continue to try to process it

## VBA Syntax

See [PropertyManagerPage2Handler5::OnKeystroke](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnKeystroke.html).

## Remarks

After the add-in has finished processing the keystroke, the message continues on and is processed by Windows. Because processing must occur, nothing should be done to destroy the page nor any action performed that could disrupt normal Windows processing while the add-in is handling this keystroke.

To enable this functionality for this PropertyManager page, set the Options argument of [ISldWorks::CreatePropertyManagerPage](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CreatePropertyManagerPage.html) or [ISldWorks::ICreatePropertyManagerPage](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ICreatePropertyManagerPage.html) to swPropertyManagerOptions_HandleKeystrokes. By default, this style is not enabled because most applications are not interested in processing keystrokes, and it is a potential performance bottleneck if lots of keystrokes are occurring.

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
