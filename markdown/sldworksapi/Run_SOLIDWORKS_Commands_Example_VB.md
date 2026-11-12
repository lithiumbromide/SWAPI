---
title: "Run SOLIDWORKS Commands Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Run_SOLIDWORKS_Commands_Example_VB.htm"
---

# Run SOLIDWORKS Commands Example (VBA)

This example shows how to programmatically open a Fillet PropertyManager page titled **My Fillet**. The macro also programmatically changes the view orientation of the part to ***Front**.

```
'----------------------------------------------------------------
' Preconditions:
' 1. In IDE, click Tools > References, and click SOLIDWORKS
'    version Commands type library, and click OK.
' 2. Open a part in SOLIDWORKS Design.
' 3. Change the view orientation of the part to any view
'    except *Front.
' 4. Select the edges on the part to fillet.
'
' Postconditions:
' 1. Opens My Fillet PropertyManager page.
' 2. Click the OK button on the My Fillet PropertyManager to
'    fillet the selected edges.
' 3. Click Continue (F5) in the IDE.
' 4. Changes the view orientation *Front.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    'Open Fillet PropertyManager page
    'Title of page is My Fillet
    swModelDocExt.RunCommand swCommands_Fillet, "My Fillet"
```

```
    Stop
    'Click OK in the My Fillet PropertyManager page to
    'create the fillets
    'Click Continue (F5) in the IDE
```

```
    'Change the view orientation of the part to *Front
    swModelDocExt.RunCommand swCommands_Front, ""
```

```
End Sub
```
