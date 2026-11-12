---
title: "SwManipulatorHandler::OnHandleSelected"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SwManipulatorHandler/SwManipulatorHandler__OnHandleSelected.htm"
---

# SwManipulatorHandler::OnHandleSelected

This method is obsolete and has been superseded by [SwManipulatorHandler2::OnHandleSelected](sldworksAPI.chm::/SwManipulatorHandler2/SwManipulatorHandler2__OnHandleSelected.htm).

Description

Not currently implemented for TriadManipulator.

Syntax (OLE Automation)

SwManipulatorHandler.OnHandleSelected ( pManipulator, handleIndex )

| Input: | (LPDISPATCH) pManipulator | Dispatch pointer to the Manipulator object |
| --- | --- | --- |
| Input: | (int) handleIndex | Control point's handle as defined by swTriadManipulatorControlPoints_e |

Syntax (COM)

status = SwManipulatorHandler->OnHandleSelected ( pManipulator, handleIndex )

| Input: | (LPDISPATCH) pManipulator | Dispatch pointer to the Manipulator object |
| --- | --- | --- |
| Input: | (int) handleIndex | Control point's handle as defined by swTriadManipulatorControlPoints_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
