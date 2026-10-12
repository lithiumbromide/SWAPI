---
title: "PropertyManagerPage2Handler4::OnKeystroke"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnKeystroke.htm"
---

# PropertyManagerPage2Handler4::OnKeystroke

This method is obsolete and has been superseded by [PropertyManagerPage2Handler5::OnKeystroke](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnKeystroke.htm).

Description

This method processes a keystroke that occurred on this PropertyManager page.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnKeystroke ( Wparam, Message, Lparam, Id)

| Input: | (long) Wparam | wparam argument from Windows processing; indicates the keystroke that occurred NOTE: From the standard set of virtual keys from Windows. Refer to the Virtual Key Code information from Microsoft documentation; for example, the Alt key is VK_MENU. |
| --- | --- | --- |
| Input: | (long) Message | Message being processed by Windows; one of these values: WM_KEYDOWN 0x0100 WM_KEYUP 0x0101 WM_CHAR 0x0102 WM_DEADCHAR 0x0103 WM_SYSKEYDOWN 0x0104 WM_SYSKEYUP 0x0105 WM_SYSCHAR 0x0106 WM_SYSDEADCHAR 0x0107 |
| Input: | (long) Lparam | lparam argument from Windows processing; bitmask containing various pieces of information; dependent on specific message |
| Input: | (long) Id | ID of the control that has focus when the keystroke was made; this is the ID specified when the control was created in PropertyManagerPage2:: AddControl or PropertyManagerPage2::AddGroupBox |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnKeystroke ( Wparam, Message, Lparam, Id)

| Input: | (long) Wparam | wparam argument from Windows processing; indicates the keystroke that occurred NOTE: From the standard set of virtual keys from Windows. Refer to the Virtual Key Code information from Microsoft documentation; for example, the Alt key is VK_MENU. |
| --- | --- | --- |
| Input: | (long) Message | Message being processed by Windows; one of these values: WM_KEYDOWN 0x0100 WM_KEYUP 0x0101 WM_CHAR 0x0102 WM_DEADCHAR 0x0103 WM_SYSKEYDOWN 0x0104 WM_SYSKEYUP 0x0105 WM_SYSCHAR 0x0106 WM_SYSDEADCHAR 0x0107 |
| Input: | (long) Lparam | lparam argument from Windows processing; bitmask containing various pieces of information; dependent on specific message |
| Input: | (long) Id | ID of the control that has focus when the keystroke was made; this is the ID specified when the control was created in PropertyManagerPage2:: AddControl or PropertyManagerPage2::AddGroupBox |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

After the add-in has finished processing the keystroke, the message continues on and is processed by Windows. Because processing must occur, nothing should be done to destroy the page nor any action performed that could disrupt normal Windows processing while the add-in is handling this keystroke.

To enable this functionality for this PropertyManager page, set the Options argument of SldWorks::CreatePropertyManagerPage to swPropertyManagerOptions_HandleKeystrokes. By default, this style is not enabled because most applications are not interested in processing keystrokes, and it is a potential performance bottleneck if lots of keystrokes are occurring.
