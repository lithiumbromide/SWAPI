---
title: "Add Ordinate Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Ordinate_Dimension_Example_VB.htm"
---

# Add Ordinate Dimension Example (VBA)

This example shows how to add an ordinate dimension.

```vb
'------------------------------------------
' Preconditions:
'          1) Drawing document is open.
'          2) Two horizontal parallel edges are selected.
'
' Postconditions: Ordinate dimension added.
'-------------------------------------------
Option Explicit
Public Enum swAddOrdinateDims_e
    swOrdinate = 1
    swVerticalOrdinate = 2
    swHorizontalOrdinate = 3
End Enum
Public Enum swCreateOrdDimError_e
    swCreateOrdDimErr_Undefined = -1            '  If encountered, report as SPR.
    swCreateOrdDimErr_Success = 0
    swCreateOrdDimErr_GenFailure = 1            '  MSG_SDIM_BAD_DIM
    swCreateOrdDimErr_GenNoInternalDims = 2     '  MSG_NO_INTERNAL_DIMS_IN_DSKETCH
    swCreateOrdDimErr_GenBadSel = 3             '  MSG_DIM_REF_NOCREATE
    swCreateOrdDimErr_GenNeedModelLoaded = 4    '  MSG_CANNOT_DIM_GHOST_IN3D
    swCreateOrdDimErr_GenSamePartOnly = 5       '  MSG_DIM_EDIT_PART
    swCreateOrdDimErr_GenExtraSelection = 6     '  MSG_DIM_TOO_MANY_SELECT
    swCreateOrdDimErr_OrdFailure = 7            '  MSG_BAD_ORDINATE_DIM0
    swCreateOrdDimErr_OrdDupInGroup = 8         '  MSG_BAD_ORDINATE_DIM1
    swCreateOrdDimErr_OrdBadDir = 9             '  MSG_BAD_ORDINATE_DIM2
End Enum
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.modelDoc
    Dim swDraw                  As SldWorks.DrawingDoc
    Dim nRetval                 As Long

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel

    ' Horizontal ordinate ignores X placement
    nRetval = swDraw.AddOrdinateDimension2(swHorizontalOrdinate, -0.1, 0.02, 0#)

End Sub
```
