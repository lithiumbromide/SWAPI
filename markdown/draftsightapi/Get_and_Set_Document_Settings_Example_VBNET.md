---
title: "Get and Set Document Settings Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Document_Settings_Example_VBNET.htm"
---

# Get and Set Document Settings Example (VB.NET)

This example shows how to get and set document settings.

```
'--------------------------------------------------------------
'Preconditions:
' 1. Create a Visual Basic Console App (.NET Framework) in Visual Studio.
' 2. Copy and paste this code into the program file.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.
' 4. Start DraftSight and open a drawing.
' 5. Start debugging the project.
'
'Postconditions: Message boxes pop up verifying that
'document properties are reset. Read the text in each
'message box before clicking OK to close it.
'----------------------------------------------------------------
```

```
Imports System.IO
Imports DraftSight.Interop.dsAutomation
```

```
Module Module1
```

```
    Dim dsApp As Application
    Dim dsDoc As Document
    Dim dsDocName As String
```

```
    Sub Main()
        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands
```

```
        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then
```

```
            'Get and set document settings
            GetSetDocSettings(dsDoc)
```

```
        Else
            MsgBox("There are no open documents in DraftSight.")
        End If
```

```
    End Sub
    Sub GetSetDocSettings(ByVal dsDoc As Document)
```

```
        'Set and get dimension scale property of document
        TestDimensionScale(dsDoc)
```

```
        'Set and get angle unit expression for document
        TestAngleUnitExpression(dsDoc)
```

```
        'Set and get base angle for document
        TestBaseAngle(dsDoc)
```

```
        'Set and get length unit expression for document
        TestLengthUnitExpression(dsDoc)
```

```
        'Set and get scale unit of the document
        TestScaleUnit(dsDoc)
```

```
        'Check whether document is active
        If dsDoc.IsActive Then
            MsgBox(dsDoc.GetPathName & " document is currently active in DraftSight.")
        Else
            MsgBox(dsDoc.GetPathName & " document is not currently active in DraftSight.")
        End If
```

```
        'Check whether document is dirty
        If dsDoc.IsDirty Then
            MsgBox(dsDoc.GetPathName & " document was modified since opened.")
        Else
            MsgBox(dsDoc.GetPathName & " document was not modified since opened.")
        End If

       'Set document dirty
       dsDoc.SetDirty

       If dsDoc.IsDirty Then
	    MsgBox(dsDoc.GetPathName & " document was successfully set dirty.")
       Else
	    MsgBox(dsDoc.GetPathName & " document was not set dirty.")
       End If
```

```
    End Sub
    Sub TestDimensionScale(ByVal dsDoc As Document)
        Dim dimScale As Double
        Dim precision As Double
```

```
        precision = 0.000000001
```

```
        'Set IDocument.DimensionScale property
        dimScale = 0.1
        dsDoc.DimensionScale = dimScale
```

```
        If Math.Abs(dimScale - dsDoc.DimensionScale) > precision Then
            MsgBox("Failed to set dimension scale property of document to " & dimScale)
        End If
    End Sub
    Sub TestAngleUnitExpression(ByVal dsDoc As Document)
```

```
        Dim newAngType As dsAngleType_e
        Dim getAngType As dsAngleType_e
        Dim newUnitPrecision As dsUnitPrecision_e
        Dim getUnitPrecision As dsUnitPrecision_e
```

```
        'Set IDocument.SetAngleUnitExpression for document
        newAngType = dsAngleType_e.dsAngleType_Radians
        newUnitPrecision = dsUnitPrecision_e.dsUnitPrecision_8
```

```
        dsDoc.SetAngleUnitExpression(newAngType, newUnitPrecision)
```

```
        'Get IDocument.GetAngleUnitExpression for document
        dsDoc.GetAngleUnitExpression(getAngType, getUnitPrecision)
```

```
        If getAngType = newAngType Then
            MsgBox("Set angle type property of document to " & newAngType & ".")
        End If
```

```
        If getUnitPrecision = newUnitPrecision Then
            MsgBox("Set unit precision property of document to " & newUnitPrecision & ".")
        End If
```

```
    End Sub
    Sub TestBaseAngle(ByVal dsDoc As Document)
        Dim newBaseAngle As Double
        Dim newClockwise As Boolean
        Dim baseAngle As Double
        Dim clockwise As Boolean
        Dim precision As Double
```

```
        precision = 0.000000001
```

```
        'Set IDocument.SetBaseAngle property for document
        newBaseAngle = 0.0#
        newClockwise = True
```

```
        dsDoc.SetBaseAngle(newBaseAngle, newClockwise)
```

```
        'Get IDocument.GetBaseAngle for document
        dsDoc.GetBaseAngle(baseAngle, clockwise)
```

```
        If Math.Abs(newBaseAngle - baseAngle) < precision Then
            MsgBox("Set base angle property of document to " & newBaseAngle & ".")
        End If
```

```
        If newClockwise = clockwise Then
            MsgBox("Set clockwise property of document.")
        End If
```

```
    End Sub
    Sub TestLengthUnitExpression(ByVal dsDoc As Document)
        Dim newLengthType As dsLengthType_e
        Dim newUnitPrecision As dsUnitPrecision_e
        Dim lengthType As dsLengthType_e
        Dim unitPrecision As dsUnitPrecision_e
```

```
        'Set IDocument.SetLengthUnitExpression for document
        newLengthType = dsLengthType_e.dsLengthType_Engineering
        newUnitPrecision = dsUnitPrecision_e.dsUnitPrecision_5
        dsDoc.SetLengthUnitExpression(newLengthType, newUnitPrecision)
```

```
        'Get IDocument.GetLengthUnitExpression for document and
        'verify if a value is correct
        dsDoc.GetLengthUnitExpression(lengthType, unitPrecision)
```

```
        If newLengthType = lengthType Then
            MsgBox("Set length type property of document to " & newLengthType & ".")
        End If
```

```
        If newUnitPrecision = unitPrecision Then
            MsgBox("Set unit precision property of document to " & newUnitPrecision & ".")
        End If
    End Sub
    Sub TestScaleUnit(ByVal dsDoc As Document)
```

```
        Dim newScaleUnit As dsScaleUnit_e
        Dim scaleUnit As dsScaleUnit_e
```

```
        'Set IDocument.ScaleUnit property for document
        newScaleUnit = dsScaleUnit_e.dsScaleUnit_Yards
        dsDoc.scaleUnit = newScaleUnit
```

```
        'Get IDocument.ScaleUnit property for document and verify if a value is correct
        scaleUnit = dsDoc.scaleUnit
```

```
        If scaleUnit = newScaleUnit Then
            MsgBox("Set scale unit property of document to " & newScaleUnit & ".")
        End If
    End Sub
```

```
End Module
```
