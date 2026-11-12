---
title: "ModelDoc::DragTo"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DragTo.htm"
---

# ModelDoc::DragTo

This method is obsolete and has been superseded by [ModelDoc2::DragTo](sldworksAPI.chm::/ModelDoc2/ModelDoc2__DragTo.htm).

Description

This method drags the specified end point.

Syntax (OLE Automation)

void ModelDoc.DragTo ( flags, x, y, z)

| Input: | (long) flags | The flags represent the mouse event flags that come from the operating system as defined by the operating system. They can be combined to indicate the selection state. For example: Left-mouse button is pressed: 0x0001 Right-mouse button is pressed: 0x0002 Shift key is pressed: 0x0004 Ctrl key is pressed: 0x0008 Middle-mouse button is pressed: 0x0010 |
| --- | --- | --- |
| Input: | (double) x | X coordinate of end point |
| Input: | (double) y | Y coordinate of end point |
| Input: | (double) z | Z coordinate of end point |

Syntax (COM)

status = ModelDoc->DragTo ( flags, x, y, z )

| Input: | (long) flags | The flags represent the mouse event flags that come from the operating system as defined by the operating system. They can be combined to indicate the selection state. For example: Left-mouse button is pressed: 0x0001 Right-mouse button is pressed: 0x0002 Shift key is pressed: 0x0004 Ctrl key is pressed: 0x0008 Middle-mouse button is pressed: 0x0010 |
| --- | --- | --- |
| Input: | (double) x | X coordinate of end point |
| Input: | (double) y | Y coordinate of end point |
| Input: | (double) z | Z coordinate of end point |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
