---
title: "Record Macros Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Record_Macros_Example_VBNET.htm"
---

# Record Macros Example (VB.NET)

This example shows how to add two lines to one or more macro recording sessions.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions: Add a reference to SolidWorks.Interop.swcommands.dll.
 '
 ' Postconditions:
 ' 1. Displays a message box informing you that
 '    macro recording has started. Click OK.
 ' 2. Displays the Save as dialog.
 ' 3. Type Macro2 in File name and select the languages
 '    to which to save macros in Save as type.
 ' 4. Writes two lines of text to the macros in the languages
 '    corresponding to the Save as type that you selected.
 ' 5. Displays a message box informing you that
 '    macro recording has ended. Click OK.
 ' 6. Displays a message box asking you if you
 '    want to stop debugging. Click Yes.
 ' 7. Run the just-recorded macros to verify.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swcommands
 Imports System

 Partial  Class SolidWorksMacro

     Public  WithEvents swAppEvents  As SldWorks

     Public  Sub Main()

         ' Set up events
         swAppEvents = swApp
         AttachEventHandlers()

         ' Start macro recording
         swApp.RunCommand(swCommands_e.swCommands_RecordPauseMacro, "")

         ' Write to VBA macro
         swApp.RecordLine("' Test")
         swApp.RecordLine("MsgBox(" & Chr(34) & "C:\Test\" & Chr(34) & ")")

         ' Write to C# macro
         swApp.RecordLineCSharp("// Test")
         swApp.RecordLineCSharp("System.Windows.Forms.MessageBox.Show(" + Chr(34) + "C:\\Test\\" + Chr(34) + ");")

         ' Write to VB.NET macro
         swApp.RecordLineVBnet("' Test")
         swApp.RecordLineVBnet("MsgBox(" & Chr(34) & "C:\Test\" & Chr(34) & ")")

         ' Stop macro recording
         swApp.RunCommand(swCommands_e.swCommands_StopMacro, "")

     End  Sub

     Sub AttachEventHandlers()
         AttachSWEvents()
     End  Sub

     Sub AttachSWEvents()
         AddHandler swAppEvents.BeginRecordNotify, AddressOf Me.SwAppEvents_BeginRecordNotify
         AddHandler swAppEvents.EndRecordNotify, AddressOf Me.swAppEvents_EndRecordNotify
     End  Sub

     Private Function swAppEvents_BeginRecordNotify() As  Integer
         'Send message when the macro recording starts
         MsgBox("Macro recording starting.")
     End  Function

     Private Function swAppEvents_EndRecordNotify() As  Integer
         'Send message when macro recording ends
         MsgBox("Macro recording ended.")
     End  Function

     '''  <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     '''  </summary>
     Public swApp As SldWorks

 End  Class
```
