---
title: "Record Macros Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Record_Macros_Example_VB.htm"
---

# Record Macros Example (VBA)

This example shows how to add two lines to one or more macro recording sessions.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Add a reference to SolidWorks version Commands type library.
' 2. Copy Macro to the main module.
' 3. Click Insert > Class Module and copy Class1 to that module.
'
' Postconditions:
' 1. Displays a message box informing you that
'    macro recording has started. Click OK.
' 2. Displays the Save as dialog.
' 3. Type Macro2 in File name and select the languages
'    to which to save macros in Save as type.
' 4. Writes two lines of text to the macros in the languages
'    corresponding to languages that you selected.
' 5. Displays a message box informing you that
'    macro recording has ended. Click OK.
' 6. Run the just-recorded macros to verify.
'----------------------------------------------------------------------------
'Macro
```

```
Sub main()
```

```
Dim swApp As SldWorks.SldWorks
Dim swAppEvents As New Class1
```

```
Set swApp = Application.SldWorks
```

```
' Set up events
Set swAppEvents.swApp = swApp
```

```
' Start macro recording
swApp.RunCommand swCommands_RecordPauseMacro, ""
```

```
' Write to VBA macro
swApp.RecordLine "' Test"
swApp.RecordLine "MsgBox(" & Chr(34) & "C:\Test\" & Chr(34) & ")"
```

```
' Write to C# macro
swApp.RecordLineCSharp "// Test"
swApp.RecordLineCSharp "System.Windows.Forms.MessageBox.Show(" + Chr(34) + "C:\\Test\\" + Chr(34) + ");"
```

```
' Write to VB.NET macro
swApp.RecordLineVBnet "' Test"
swApp.RecordLineVBnet "MsgBox(" & Chr(34) & "C:\Test\" & Chr(34) & ")"
```

```
' Stop macro recording
swApp.RunCommand swCommands_StopMacro, ""
```

```
End Sub
```

###### 'Class1

```
Option Explicit
```

```
Public WithEvents swApp As SldWorks.SldWorks
```

```
Private Function swApp_BeginRecordNotify() As Long
    'Send message when the macro recording starts
    MsgBox "Macro recording starting."
End Function
```

```
Private Function swApp_EndRecordNotify() As Long
    'Send message when macro recording ends
    MsgBox "Macro recording ended."
End Function
```
