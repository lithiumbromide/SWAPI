---
title: "Get and Set Document Settings Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Document_Settings_Example_VBA.htm"
---

# Get and Set Document Settings Example (VBA)

This example shows how to get and set document settings.

```
'--------------------------------------------------------------
'Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a drawing.
' 5. Run the macro.
'
'Postconditions: Message boxes pop up verifying that
'document properties are reset. Read the text in each
'message box before clicking OK to close it.
'----------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsDocName As String
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Set dsDoc = dsApp.GetActiveDocument()
    If Not dsDoc Is Nothing Then
```

```
        'Get and set document settings
        GetSetDocSettings dsDoc
```

```
    Else
        MsgBox "There are no open documents in DraftSight."
    End If
```

```
End Sub
Sub GetSetDocSettings(dsDoc As DraftSight.Document)
```

```
    'Set and get dimension scale property of document
    TestDimensionScale dsDoc
```

```
    'Set and get angle unit expression for document
    TestAngleUnitExpression dsDoc
```

```
    'Set and get base angle for document
    TestBaseAngle dsDoc
```

```
    'Set and get length unit expression for document
    TestLengthUnitExpression dsDoc
```

```
    'Set and get scale unit of the document
    TestScaleUnit dsDoc
```

```
    'Check whether document is active
    If dsDoc.IsActive Then
        MsgBox dsDoc.GetPathName & " document is currently active in DraftSight."
    Else
        MsgBox dsDoc.GetPathName & " document is not currently active in DraftSight."
    End If
```

```
    'Check whether document is dirty
    If dsDoc.IsDirty Then
        MsgBox dsDoc.GetPathName & " document was modified since opened."
    Else
        MsgBox dsDoc.GetPathName & " document was not modified since opened."
    End If

   'Set document dirty
   dsDoc.SetDirty

   If dsDoc.IsDirty Then
	MsgBox dsDoc.GetPathName() & " document was successfully set dirty."
   Else
	MsgBox dsDoc.GetPathName() & " document was not set dirty."
   End If
```

```
End Sub
Sub TestDimensionScale(dsDoc As DraftSight.Document)
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
    If Abs(dimScale - dsDoc.DimensionScale) > precision Then
        MsgBox "Failed to set dimension scale property of document to " & dimScale
    End If
End Sub
Sub TestAngleUnitExpression(dsDoc As DraftSight.Document)
```

```
    Dim newAngType As DraftSight.dsAngleType_e
    Dim getAngType As DraftSight.dsAngleType_e
    Dim newUnitPrecision As DraftSight.dsUnitPrecision_e
    Dim getUnitPrecision As DraftSight.dsUnitPrecision_e
```

```
    'Set IDocument.SetAngleUnitExpression for document
    newAngType = dsAngleType_Radians
    newUnitPrecision = dsUnitPrecision_8
```

```
    dsDoc.SetAngleUnitExpression newAngType, newUnitPrecision
```

```
    'Get IDocument.GetAngleUnitExpression for document
    dsDoc.GetAngleUnitExpression getAngType, getUnitPrecision
```

```
    If getAngType = newAngType Then
        MsgBox "Set angle type property of document to " & newAngType & "."
    End If
```

```
    If getUnitPrecision = newUnitPrecision Then
        MsgBox "Set unit precision property of document to " & newUnitPrecision & "."
    End If
```

```
End Sub
Sub TestBaseAngle(dsDoc As DraftSight.Document)
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
    newBaseAngle = 0#
    newClockwise = True
```

```
    dsDoc.SetBaseAngle newBaseAngle, newClockwise
```

```
    'Get IDocument.GetBaseAngle for document
    dsDoc.GetBaseAngle baseAngle, clockwise
```

```
    If Abs(newBaseAngle - baseAngle) < precision Then
        MsgBox "Set base angle property of document to " & newBaseAngle & "."
    End If
```

```
    If newClockwise = clockwise Then
        MsgBox "Set clockwise property of document."
    End If
```

```
End Sub
Sub TestLengthUnitExpression(dsDoc As DraftSight.Document)
    Dim newLengthType As DraftSight.dsLengthType_e
    Dim newUnitPrecision As DraftSight.dsUnitPrecision_e
    Dim lengthType As DraftSight.dsLengthType_e
    Dim unitPrecision As DraftSight.dsUnitPrecision_e
```

```
    'Set IDocument.SetLengthUnitExpression for document
    newLengthType = dsLengthType_Engineering
    newUnitPrecision = dsUnitPrecision_5
    dsDoc.SetLengthUnitExpression newLengthType, newUnitPrecision
```

```
    'Get IDocument.GetLengthUnitExpression for document and
    'verify if a value is correct
    dsDoc.GetLengthUnitExpression lengthType, unitPrecision
```

```
    If newLengthType = lengthType Then
        MsgBox "Set length type property of document to " & newLengthType & "."
    End If
```

```
    If newUnitPrecision = unitPrecision Then
        MsgBox "Set unit precision property of document to " & newUnitPrecision & "."
    End If
End Sub
Sub TestScaleUnit(dsDoc As DraftSight.Document)
```

```
    Dim newScaleUnit As DraftSight.dsScaleUnit_e
    Dim scaleUnit As DraftSight.dsScaleUnit_e
```

```
    'Set IDocument.ScaleUnit property for document
    newScaleUnit = DraftSight.dsScaleUnit_e.dsScaleUnit_Yards
    dsDoc.scaleUnit = newScaleUnit
```

```
    'Get IDocument.ScaleUnit property for document and verify if a value is correct
    scaleUnit = dsDoc.scaleUnit
```

```
    If scaleUnit = newScaleUnit Then
        MsgBox "Set scale unit property of document to " & newScaleUnit & "."
    End If
```

```
End Sub
```
