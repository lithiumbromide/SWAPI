---
title: "Get and Set Drawing Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Drawing_Properties_Example_VBA.htm"
---

# Get and Set Drawing Properties Example (VBA)

This example shows how to get and set standard and custom drawing properties.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Press F5.
'
' Postconditions:
' 1. Connects to DraftSight.
' 2. Gets the active document.
' 3. Gets and sets standard and custom drawing properties.
' 4. Displays a message box showing the total number of
'    drawing custom properties. Click OK to close the message
'    box.
' 5. Displays a message box showing the first custom property
'    in the list of custom properties. Click OK to close
'    the message box.
' 6. Displays a message box instructing you to
'    type DRAWINGPROPERTIES at the prompt in the
'    command window to open the drawing properties dialog.
'    Click OK to close the message box.
' 7. Examine the properties on both tabs of the drawing
'    properties dialog.
'----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Set dsDoc = dsApp.GetActiveDocument()
    If dsDoc Is Nothing Then
        MsgBox "There are no open documents."
    End If
```

```
    'Get drawing properties
    Dim dsDrawingProperties As DrawingProperties
    Set dsDrawingProperties = dsDoc.GetDrawingProperties
```

```
    If dsDrawingProperties Is Nothing Then
        MsgBox "There are no valid drawing properties."
    End If

    'Set drawing properties
    dsDrawingProperties.Author = "Me"
    dsDrawingProperties.Keywords = "test,sample"
    dsDrawingProperties.Comments = "Properties created by this DraftSight API application"
    dsDrawingProperties.Title = "Title"
    dsDrawingProperties.Subject = "Test"
```

```
    'Add key and value to the drawing custom properties
    Dim key As String
    Dim value As String
    key = "0123"
    value = "Test Value"
    dsDrawingProperties.AddCustomProperty key, value
```

```
    'Set another drawing custom property
    dsDrawingProperties.SetCustomProperty "9234", "234"
```

```
    'Remove previously added drawing custom property
    dsDrawingProperties.RemoveCustomProperty ("234")
```

```
    'Set drawing custom property with an index number
    dsDrawingProperties.SetCustomPropertyAt 1, "testvalue"
```

```
    'Get number of custom properties
    MsgBox ("Number of custom properties: " & dsDrawingProperties.GetCustomPropertyCount)
```

```
    Dim keyValue As String
    keyValue = ""
    If dsDrawingProperties.GetCustomPropertyCount >= 0 Then
        'Get first drawing custom property and key value in the list
        'of drawing custom properties
        Dim customProperty As String
        customProperty = dsDrawingProperties.GetCustomPropertyAt(0, keyValue)
        MsgBox ("Custom property: " + customProperty + ", Key: " + keyValue)
    End If
```

```
    'Type DRAWINGPROPERTIES at the prompt in the command window
    'to see the drawing properties
    MsgBox ("Type DRAWINGPROPERTIES at the prompt in the command window to open the drawing properties dialog. Examine the properties on both tabs.")
```

```
End Sub
```
