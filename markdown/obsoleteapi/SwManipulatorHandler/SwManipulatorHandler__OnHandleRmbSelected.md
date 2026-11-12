---
title: "SwManipulatorHandler::OnHandleRmbSelected"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SwManipulatorHandler/SwManipulatorHandler__OnHandleRmbSelected.htm"
---

# SwManipulatorHandler::OnHandleRmbSelected

This method is obsolete and has been superseded by [SwManipulatorHandler2::OnHandleRmbSelected](sldworksAPI.chm::/SwManipulatorHandler2/SwManipulatorHandler2__OnHandleRmbSelected.htm).

Description

This method is called when a user clicks the right-mouse.

Syntax (OLE Automation)

void = SwManipulatorHandler.OnHandleRmbSelected ( pManipulator, handleIndex )

| Input: | (LPDISPATCH) pManipulator | Dispatch pointer to the Manipulator object |
| --- | --- | --- |
| Input: | (int) handleIndex | Control point's handle as defined by swTriadManipulatorControlPoints_e |

Syntax (COM)

status = SwManipulatorHandler->OnHandleRmbSelected ( pManipulator, handleIndex)

| Input: | (LPDISPATCH) pManipulator | Dispatch pointer to the Manipulator object |
| --- | --- | --- |
| Input: | (int) handleIndex | Control point's handle as defined by swTriadManipulatorControlPoints_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
