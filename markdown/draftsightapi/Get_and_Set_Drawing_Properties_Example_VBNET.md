---
title: "Get and Set Drawing Properties Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_and_Set_Drawing_Properties_Example_VBNET.htm"
---

# Get and Set Drawing Properties Example (VB.NET)

This example shows how to get and set standard and custom drawing properties.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add a reference to System.Windows.Forms.
' 5. Start DraftSight and open a document.
' 6. Press F5.
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

Imports System
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms

Module Module1

    Sub Main()

        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connect to DraftSight application
        dsApp = GetObject(, "DraftSight.Application")

        If dsApp Is Nothing Then
            Return
        End If

        'Abort any command currently running in DraftSight to avoid nested commands
        dsApp.AbortRunningCommand()

        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        'Get drawing properties
        Dim dsDrawingProperties As DrawingProperties = dsDoc.GetDrawingProperties()

        If dsDrawingProperties Is Nothing Then
            MessageBox.Show("There are no valid drawing properties.")
            Return
        End If

        'Set drawing properties
        dsDrawingProperties.Author = "Me"
        dsDrawingProperties.Keywords = "test,sample"
        dsDrawingProperties.Comments = "Properties created by this DraftSight API application"
        dsDrawingProperties.Title = "Title"
        dsDrawingProperties.Subject = "Test"

        'Add key and value to the drawing custom properties
        Dim key As String = "0123"
        Dim value As String = "Test Value"
        dsDrawingProperties.AddCustomProperty(key, value)

        'Set another drawing custom property
        dsDrawingProperties.SetCustomProperty("9234", "234")

        'Remove previously added drawing custom property
        dsDrawingProperties.RemoveCustomProperty("234")

        'Set drawing custom property with an index number
        dsDrawingProperties.SetCustomPropertyAt(1, "testvalue")

        'Get number of custom properties
        Dim nbrCustomProperties As Integer = 0
        Dim nbrCustomPropertiesStr As String = ""
        nbrCustomProperties = dsDrawingProperties.GetCustomPropertyCount
        nbrCustomPropertiesStr = nbrCustomProperties.ToString()
        MessageBox.Show("Number of custom properties: " + nbrCustomPropertiesStr)

        Dim keyValue As String = ""
        If nbrCustomProperties >= 0 Then
            'Get first drawing custom property and key value in the list of drawing custom properties
            Dim customProperty As String = dsDrawingProperties.GetCustomPropertyAt(0, keyValue)
            MessageBox.Show("Custom property: " + customProperty + ", Key: " + keyValue)
        End If

        'Type DRAWINGPROPERTIES at the prompt in the command window
        'to see the drawing properties
        MessageBox.Show("Type DRAWINGPROPERTIES at the prompt in the command window to open the drawing properties dialog. Examine the properties on both tabs.")

    End Sub

End Module
```
