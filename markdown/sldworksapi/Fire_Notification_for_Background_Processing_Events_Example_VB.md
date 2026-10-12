---
title: "Fire Notifications for Background Processing Events Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_for_Background_Processing_Events_Example_VB.htm"
---

# Fire Notifications for Background Processing Events Example (VBA)

This example shows how to fire notifications when background processing events occur.

'---------------------------------------------------------------------------
' Preconditions:
' 1. Create a form, UserForm1, that contains the following controls:
' * CheckBox1 with caption **Enable background processing and open drawing**
' * CommandButton1 with caption **Close after background processing end event fires**
' 2. Copy [this code](#main) to the main module.
' 3. Copy [this code](#Class) to UserForm1.
' 4. Modify the path in UserForm1's code to point to a large drawing document
' containing many parts.
' 5. Open the Task Manager, click the Processes tab, and click the
' CPU column header to sort the processes in descending order.
' 6. Run this macro to show UserForm1.
' a. Select **Enable background processing and open drawing**.
' 1. Enables background processing for the application.
' 2. Opens the specified drawing document.
' 3. Fires background processing start event.
' b. In Task Manager, observe that several **sldbgproc.exe** processes
' are occupying most of the CPU.
' c. After several seconds, observe that the **sldbgproc.exe** processes stop,
' and the background processing end event fires.
' d. Click **Close after background processing end event fires**.
' UserForm1 unloads.
'
' Postconditions: Inspect the Immediate window for background processing
' event notifications.
'---------------------------------------------------------------------------

```vb
'Main module
Option Explicit
Sub main()
     UserForm1.Show vbModeless
End Sub
```

###### 'UserForm1 Code

```vb
Option Explicit
Private WithEvents swApp As SldWorks.SldWorks
Private Sub CheckBox1_Click()
    Set swApp = Application.SldWorks
     swApp.EnableBackgroundProcessing = CheckBox1.Value

    Dim filePath As String
     filePath = "path_to_large_drawing"
     Dim docSpecification  As DocumentSpecification
     Set docSpecification = swApp.GetOpenDocSpec(filePath)
     docSpecification.Silent = True

    Dim swmodelDoc As ModelDoc2
     Set swmodelDoc = swApp.OpenDoc7(docSpecification)
     Dim swDrawingDoc As DrawingDoc
     Set swDrawingDoc = swmodelDoc

    ' Set document background processing to application setting
      swDrawingDoc.BackgroundProcessingOption = 2
 End Sub
Private Function swApp_BackgroundProcessingStartNotify(ByVal filename As String) As Long
     Debug.Print "Background processing start event fired."
 End Function
Private Function swApp_BackgroundProcessingEndNotify(ByVal filename As String) As Long
     Debug.Print "Background processing end event fired."
     swApp.EnableBackgroundProcessing = False
 End Function
Private Sub CommandButton1_Click()
     Unload UserForm1
 End Sub
```
