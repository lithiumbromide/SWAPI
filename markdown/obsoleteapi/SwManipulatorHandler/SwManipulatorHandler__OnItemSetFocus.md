---
title: "SwManipulatorHandler::OnItemSetFocus"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SwManipulatorHandler/SwManipulatorHandler__OnItemSetFocus.htm"
---

# SwManipulatorHandler::OnItemSetFocus

This method is obsolete and has been superseded by [SwManipulatorHandler2::OnItemSetFocus](sldworksAPI.chm::/SwManipulatorHandler2/SwManipulatorHandler2__OnItemSetFocus.htm).

Description

Not currently implemented for TriadManipulator.

Syntax (OLE Automation)

SwManipulatorHandler.OnItemSetFocus ( pManipulator, id)

| Input: | (LPDISPATCH) pManipulator | Dispatch pointer to the Manipulator object |
| --- | --- | --- |
| Input: | (int) id | ID of item on which to set focus |

Syntax (COM)

status = SwManipulatorHandler->OnItemSetFocus ( pManipulator, id)

| Input: | (LPDISPATCH) pManipulator | Dispatch pointer to the Manipulator object |
| --- | --- | --- |
| Input: | (int) id | ID of item on which to set focus |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
