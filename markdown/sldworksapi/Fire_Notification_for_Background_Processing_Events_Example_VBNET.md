---
title: "Fire Notifications for Background Processing Events Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_for_Background_Processing_Events_Example_VBNET.htm"
---

# Fire Notifications for Background Processing Events Example (VB.NET)

This example shows how to fire notifications when background processing events occur.

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Create a VSTA VB.NET macro.
'     a. Copy and paste SolidWorksMacro.vb's code in the macro.
'     b. Create a form, Form1, that contains the following
'        controls:
'        * CheckBox1 with caption Enable background processing and open
'          drawing.
'        * Button1 with caption Close after background processing end event
'          fires.
'     c. Copy and paste Form1.vb's code in your form's code window.
'     d. Modify the path in Form1.vb to open a huge drawing document that
'        contains many parts.
'  2. Press F5 to start and close the debugger.
'  3. Click Build > Build macro_name to build a DLL for the macro.
'  4. Save and close the macro.
'
' Postconditions:
'  1. Open the Windows Task manager, click the Processes tab, and click the CPU column
'    header to sort the processes in descending order.
'  2. In SOLIDWORKS, click Tools > Macro > Run.
'     a. Locate your macro's \SwMacro\bin folder.
'     b. Select macro_name.dll.
'     c. Click Open to open the form.
'  3. Select the Enable background processing and open drawing checkbox on the form.
'  4. Displays a checkmark in the check box.
'  5. Click OK to close the Background processing enabled message box.
'  6. Opens the specified drawing.
'  7. Fires the background processing start events.
'  8. Click OK to close the Background processing start event fired message box.
'  9. In the Windows Task Manager, observe that several sldbgproc.exe processes are
'     occupying most of the CPU.
' 10. Click OK to close the Background processing end event fired message box.
' 11. Click Close after background processing end event fires button on the form.
' 12. Unloads Form1.
'----------------------------------------------------------------------------------

'SolidWorksMacro.vb
```

```
Imports SolidWorks.Interop.sldworks
Imports System.Runtime.InteropServices
Imports System

Partial Public Class SolidWorksMacro

    Public swApp As SldWorks

    Public Sub Main()

        'Create and show an instance of the form
        Dim myForm As New Form1
        myForm.Show()

    End Sub

End Class
```

```
'Form1
```

```
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Windows.Forms
Imports System.Diagnostics
Imports System.Collections
Imports System.Runtime.InteropServices

Public Class Form1

    Public WithEvents swApp As SldWorks
    Public checkBoxClicked As Boolean

    Private Sub CheckBox1_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles CheckBox1.CheckedChanged

        Try
            swApp = CType(System.Runtime.InteropServices.Marshal.GetActiveObject("SldWorks.Application"), SldWorks)
        Catch ex As Exception
            MsgBox(ex.Message)
            Exit Sub
        End Try

        Dim swModelDoc As ModelDoc2
        Dim swDrawingDoc As DrawingDoc

        Dim filePath As String
        filePath = "Path_and_filename_of_huge_drawing"

        Dim docSpecification As DocumentSpecification

        ' Set up events
        AttachEventHandlers()

        ' Enable background processing
        swApp.EnableBackgroundProcessing = True
        MsgBox("Background processing enabled")

        ' Open huge drawing
        docSpecification = swApp.GetOpenDocSpec(filePath)
        docSpecification.Silent = True
        swModelDoc = swApp.OpenDoc7(docSpecification)

        swDrawingDoc = swModelDoc

        ' Set document background processing to application setting
        swDrawingDoc.BackgroundProcessingOption = swBackgroundProcessOption_e.swBackgroundProcessing_DeferToApplication

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swApp.BackgroundProcessingStartNotify, AddressOf Me.mySwApp_BackgroundProcessingStartNotify
        AddHandler swApp.BackgroundProcessingEndNotify, AddressOf Me.mySwApp_BackgroundProcessingEndNotify
    End Sub

    Private Function mySwApp_BackgroundProcessingStartNotify(ByVal filename As String) As Integer
        MsgBox("Background processing start event fired")
    End Function
    Private Function mySwApp_BackgroundProcessingEndNotify(ByVal filename As String) As Integer
        MsgBox("Background processing end event fired")
        swApp.EnableBackgroundProcessing = False
    End Function
    Public Sub CheckBox1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles CheckBox1.Click
        checkBoxClicked = True
    End Sub
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Close()
    End Sub
End Class
```
