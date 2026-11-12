---
title: "Ignore Feature Colors Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Ignore_Feature_Colors_Example_VB.htm"
---

# Ignore Feature Colors Example (VBA)

This example shows how to change a user preference option so that feature colors are ignored in parts. This option setting, swIgnoreFeatureColors, can be true or false and can be different for each document. It is not a system-level setting; it is a document-level setting. Therefore, you must set this value for each document.

By default, when a document is created, swIgnoreFeatureColors is false.

```
'----------------------------------------------------------------
' Preconditions: Open a part document.
'
' Postconditions:
' 1. Gets current setting for swIgnoreFeatureColors and
'    pops up a message box. Click OK to close the message
'    box.
' 2. Pops up a message box prior to setting swIgnoreFeatureColors
'    to true. Click OK to close the message box.
' 3. Sets swIgnoreFeatureColors to true and pops up a message
'    box indicating setting swIgnoreFeatureColors to true
'    is successful. Click OK to close the message box.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim res, val As Boolean
Dim msg1 As String
```

```
Sub main()
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set Part = swApp.ActiveDoc
```

```
    ' Exit if no model is active
    If Part Is Nothing Then
        swApp.SendMsgToUser "Open a model document and run the macro again."
        Exit Sub
    End If
```

```
    ' Get current setting
    val = Part.GetUserPreferenceToggle(swIgnoreFeatureColors)
```

```
    ' Create message
    msg1 = "swIgnoreFeatureColors is currently set to " & val & "."
```

```
    ' Send message to user
    swApp.SendMsgToUser msg1
```

```
    ' Change setting to true, which indicates to ignore feature colors
    swApp.SendMsgToUser "Setting swIgnoreFeatureColors to True."
    res = Part.SetUserPreferenceToggle(swIgnoreFeatureColors, True)
```

```
    ' Verify if successful    If (res = True) Then
        swApp.SendMsgToUser "Setting swIgnoreFeatureColors to True successful."
    Else
        swApp.SendMsgToUser "Error! Setting swIgnoreFeatureColors to True not successful."
    End If
```

```
End Sub
```
