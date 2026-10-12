---
title: "Get Component State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_State_Example_VB.htm"
---

# Get Component State Example (VBA)

This example shows how to find out if the selected component is resolved or suppressed, hidden or visible, and whether or not it's a rigid or flexible subassembly. This example also gets the persistent ID of the selected component.

```
'---------------------------------------------------
' Preconditions:
' 1. Ensure that the specified assembly document
'    to open exists.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions:
' 1. Opens the assembly document.
' 2. Selects the subassembly.
' 3. Prints to the Immediate window:
'    * Paths to the assembly and subassembly documents
'    * Whether the component is hidden, fixed,
'      or suppressed
'    * Component's persistent ID
'    * Component's solving state
' 4. Examine the Immediate window.
'----------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swModelDocExt               As SldWorks.ModelDocExtension
    Dim swAssy                      As SldWorks.AssemblyDoc
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swComp                      As SldWorks.Component2
    Dim fileName                    As String
    Dim status                      As Boolean
    Dim errors                      As Long
    Dim warnings                    As Long
```

```
    Set swApp = Application.SldWorks

    ' Open assembly document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\98food processor.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    ' Select subassembly
    status = swModelDocExt.SelectByID2("blade shaft-1@98food processor", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swAssy = swModel
    Set swComp = swSelMgr.GetSelectedObjectsComponent3(1, 0)
```

```
    ' Print to the Immediate window the path and state of the
    ' selected component
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Component   = " & swComp.Name2
    Debug.Print "    Path           = " & swComp.GetPathName
    Debug.Print "    IsHidden       = " & swComp.IsHidden(True)
    Debug.Print "    IsFixed        = " & swComp.IsFixed
    Debug.Print "    GetSuppression = " & swComp.GetSuppression
    Debug.Print "    ID             = " & swComp.GetID
    ' 0 =  if subassembly is rigid
    ' 1 =  if subassembly is flexible
    ' -1 = selected component is a part component
    Debug.Print "    Solving        = " & swComp.Solving
```

```
End Sub
```
