---
title: "SwManipulatorHandler::OnLmbSelected"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SwManipulatorHandler/SwManipulatorHandler__OnLmbSelected.htm"
---

# SwManipulatorHandler::OnLmbSelected

This method is obsolete and has been superseded by [SwManipulatorHandler2::OnLmbSelected](sldworksAPI.chm::/SwManipulatorHandler2/SwManipulatorHandler2__OnLmbSelected.htm).

Description

This method is called when a user clicks the left-mouse button.

Syntax (OLE Automation)

retVal = SwManipulatorHandler.OnLmbSelected ( pManipulator)

| Input: | (LPDISPATCH) pManipulator | Dispatch pointer to the Manipulator object |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retVal | Unknown |

Syntax (COM)

status = SwManipulatorHandler->OnLmbSelected ( pManipulator, &retVal)

| Input: | (LPDISPATCH) pManipulator | Dispatch pointer to the Manipulator object |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retVal | Unknown |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
