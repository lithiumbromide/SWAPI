---
title: "Get and Set Command Options Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Command_Options_Example_VBNET.htm"
---

# Get and Set Command Options Example (VB.NET)

This example shows how to get and set command options.

```
'------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Open the Immediate window.
' 5. Start DraftSight and open a document.
' 6. Run the macro.
'
' Postconditions: Specified command option values are returned, set, and
' printed to the Immediate window. Results of setting specified command
' option values are also printed to the Immediate window.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation
Module Module1
    Sub Main()
```

```
        Dim dsApp As Application
        Dim dsDoc As Document
```

```
        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands
```

```
        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then
            Dim boolCommand As Boolean
            Dim doubleCommand As Double
            Dim int16Command As Integer
            Dim int32Command As Long
            Dim int8Command As Long
            Dim xint2DCommand As Integer
            Dim yint2DCommand As Integer
            Dim xint3DCommand As Integer
            Dim yint3DCommand As Integer
            Dim zint3DCommand As Integer
            Dim valueStringCommand As String = ""
            Dim getResult As dsGetCommandOptionResult_e
            Dim setResult As dsSetCommandOptionResult_e
```

```
            'Boolean
            'Get and set whether to enable drawing boundary
            'Tools > Options > Drawing Settings > Behavior > Drawing Boundary > Enable drawing boundary
            dsDoc.GetCommandOptionBool(dsCommandOptionBool_e.dsCommandOptionBool_EnblDlDm, boolCommand, getResult)
            Debug.Print("Get drawing boundary value: " & boolCommand)
            boolCommand = True
            dsDoc.SetCommandOptionBool(dsCommandOptionBool_e.dsCommandOptionBool_EnblDlDm, boolCommand, setResult)
            Debug.Print("Set drawing boundary value: " & boolCommand)
            Debug.Print("Set result: " & setResult)
            Debug.Print(" ")
```

```
            'Double
            'Get and set dimension tolerance precision
            'Tools > Options > Drafting Styles > Dimension > Tolerance > Tolerance settings > Precision
            dsDoc.GetCommandOptionDouble(dsCommandOptionDouble_e.dsCommandOptionDouble_SetTDmMin, doubleCommand, getResult)
            Debug.Print("Get dimension tolerance precision: " & doubleCommand)
            doubleCommand = 2.0#
            dsDoc.SetCommandOptionDouble(dsCommandOptionDouble_e.dsCommandOptionDouble_SetTDmMin, doubleCommand, setResult)
            Debug.Print("Set dimension tolerance precision: " & doubleCommand)
            Debug.Print("Set result: " & setResult)
            Debug.Print(" ")
```

```
            'Int16
            'Get and set units for inserting entities
            'Tools > Options > System Options > Drawing File Defaults > Block insertion units > Units for inserting entities
            dsDoc.GetCommandOptionInt16(dsCommandOptionInt16_e.dsCommandOptionInt16_SetActBlkInsUnt, int16Command, getResult)
            Debug.Print("Get units for inserting entities: " & int16Command)
            int16Command = 4
            dsDoc.SetCommandOptionInt16(dsCommandOptionInt16_e.dsCommandOptionInt16_SetActBlkInsUnt, int16Command, setResult)
            Debug.Print("Set units for inserting entities: " & int16Command)
            Debug.Print("Set result: " & setResult)
            Debug.Print(" ")
```

```
            'Int32
            'Get and set the elapsed time between saving and backing up documents
            'Tools > Options > System Options > Auto-save & Backup > Auto-save/backups > Save document every nn minutes
            dsDoc.GetCommandOptionInt32(dsCommandOptionInt32_e.dsCommandOptionInt32_SetSvTm, int32Command, getResult)
            Debug.Print("Get elapsed time between saving and backing up documents: " & int32Command)
            int32Command = 15
            dsDoc.SetCommandOptionInt32(dsCommandOptionInt32_e.dsCommandOptionInt32_SetSvTm, int32Command, setResult)
            Debug.Print("Set elapsed time between saving and backing up documents: " & int32Command)
            Debug.Print("Set result: " & setResult)
            Debug.Print(" ")
```

```
            'Int8
            'Get and set whether dual dimensions display leading zeros, trailing zeros, 0', and 0"
            'Tools > Options > Drafting Styles > Dimension > Dual Dimension > Zeroes display
            dsDoc.GetCommandOptionInt8(dsCommandOptionInt8_e.dsCommandOptionInt8_SetDlDmZroDsp, int8Command, getResult)
            Debug.Print("Get whether dual dimensions display leading zeros, trailing zeros, 0 feet, and 0 inches: " & int8Command)
            int8Command = 0
            dsDoc.SetCommandOptionInt8(dsCommandOptionInt8_e.dsCommandOptionInt8_SetDlDmZroDsp, int8Command, setResult)
            Debug.Print("Set whether dual dimensions display leading zeros, trailing zeros, 0 feet, and 0 inches: " & int8Command)
            Debug.Print("Set result: " & setResult)
            Debug.Print(" ")
```

```
            '2D Point
            'Get and set horizontal and vertical snap spacing for the pointer device
            'Tools > Options > User Preferences > Drafting Options > Pointer Control > Snap Settings > Spacing > Horizontal Snap spacing and Vertical Snap spacing
            dsDoc.GetCommandOptionPoint2D(dsCommandOptionPoint2d_e.dsCommandOptionPoint2d_SetSnpSpc, xint2DCommand, yint2DCommand, getResult)
            Debug.Print("Get pointer's horizontal and vertical snap values: " & xint2DCommand & ", " & yint2DCommand)
            xint2DCommand = 15.0#
            yint2DCommand = 15.0#
            dsDoc.SetCommandOptionPoint2D(dsCommandOptionPoint2d_e.dsCommandOptionPoint2d_SetSnpSpc, xint2DCommand, yint2DCommand, setResult)
            Debug.Print("Set pointer's horizontal and vertical snap values: " & xint2DCommand & ", " & yint2DCommand)
            Debug.Print("Set result: " & setResult)
            Debug.Print(" ")
```

```
            '3D Point
            'Get and set the base point for inserting a drawing
            dsDoc.GetCommandOptionPoint3D(dsCommandOptionPoint3d_e.dsCommandOptionPoint3d_SetBase, xint3DCommand, yint3DCommand, zint3DCommand, getResult)
            Debug.Print("Get base point for inserting a drawing: " & xint3DCommand & ", " & yint3DCommand & ", " & zint3DCommand)
            xint3DCommand = 1.0#
            yint3DCommand = 0.0#
            zint3DCommand = 0.0#
            dsDoc.SetCommandOptionPoint3D(dsCommandOptionPoint3d_e.dsCommandOptionPoint3d_SetBase, xint3DCommand, yint3DCommand, zint3DCommand, setResult)
            Debug.Print("Set base point for inserting a drawing: " & xint3DCommand & ", " & yint3DCommand & ", " & zint3DCommand)
            Debug.Print("Set result: " & setResult)
            Debug.Print(" ")
```

```
            'String
            'Get and set name of project
            dsDoc.GetCommandOptionString(dsCommandOptionString_e.dsCommandOptionString_LgcyPROJECTNAME, valueStringCommand, getResult)
            Debug.Print("Get project name: " & valueStringCommand)
            valueStringCommand = "New project name"
            dsDoc.SetCommandOptionString(dsCommandOptionString_e.dsCommandOptionString_LgcyPROJECTNAME, valueStringCommand, setResult)
            Debug.Print("Set project name: " & valueStringCommand)
            Debug.Print("Set result: " & setResult)
            Debug.Print(" ")
        Else
            Debug.Print("There are no open documents in DraftSight.")
        End If
    End Sub
End Module
```
