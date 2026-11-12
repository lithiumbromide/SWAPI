---
title: "SwManipulatorHandler::OnEndNoDrag"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SwManipulatorHandler/SwManipulatorHandler__OnEndNoDrag.htm"
---

# SwManipulatorHandler::OnEndNoDrag

This topic is obsolete and has been superseded by [SwManipulatorHandler2::OnEndNoDrag](sldworksAPI.chm::/SwManipulatorHandler2/SwManipulatorHandler2__OnEndNoDrag.htm).

Description

This method is called when a user releases a mouse button and has not dragged the pointer.

Syntax (OLE Automation)

SwManipulatorHandler.OnEndNoDrag ( pManipulator, handleIndex)

| Input: | (LPDISPATCH) pManipulator | Dispatch pointer to the Manipulator object |
| --- | --- | --- |
| Input: | (int) handleIndex | Control point's handle as defined by swTriadManipulatorControlPoints_e |

Syntax (COM)

status = SwManipulatorHandler->OnEndNoDrag ( pManipulator, handleIndex)

| Input: | (LPDISPATCH) pManipulator | Dispatch pointer to the Manipulator object |
| --- | --- | --- |
| Input: | (int) handleIndex | Control point's handle as defined by swTriadManipulatorControlPoints_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
