---
title: "Get Messages Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Messages_Example_VB.htm"
---

# Get Messages Example (VBA)

This example shows how to get the number of messages (up to the last 20), including their text, resource IDs, and type, in the current SOLIDWORKS Design session.

```
'-----------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Open, edit, close, and save a part in the assembly,
'    but do not rebuild the part.
' 3. Close the assembly, but do not save changes
'    made to the assembly.
' 4. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'-----------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks

Dim vMsgs As Variant

Dim vMsgIds As Variant

Dim vMsgTypes As Variant
Dim count As Long

Dim i As Integer

Sub main()

Set swApp = Application.SldWorks

count = swApp.GetErrorMessages(vMsgs, vMsgIds, vMsgTypes)

Debug.Print "Number of messages = " & count

For i = 0 To (count - 1)

    Debug.Print " "

    Debug.Print "Message = " & vMsgs(i)

    Debug.Print "Resource ID of this message = " & vMsgIds(i)

    Debug.Print "Type of message = " & vMsgTypes(i)

    Debug.Print " "

Next i

End Sub
```
