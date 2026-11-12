---
title: "Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and Property Manager Pages"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm"
---

# Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and Property Manager Pages

## Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages

### Problem

The following VB.NET code displays a modeless dialog, but the Tab and Enter keys are not captured by SOLIDWORKS.

```vb
Public Sub OnSampleCallback()
    Dim myForm As New Form1()
    myForm.Show()
End Sub
```

You could add event handlers to capture the missing keystrokes, but the dialog will still not behave as intended. Therefore, try using the following code.

### Solution

To display a modeless dialog that captures Tab and Enter keys from a VB.NET add-in, you could code the add-in's menu callback code as follows:

```vb
Public Sub OnSampleCallback()
    Dim myForm As New Form1()
    Application.Run(myForm)
End Sub
```

By calling Application.Run, you create a new application message loop for the dialog, which is separate from the SOLIDWORKS message loop. The dialog remains a child process to SOLIDWORKS, and the events are handled as expected. This solution also applies to C#.

However, because an add-in runs in the same process as SOLIDWORKS, the SOLIDWORKS message loop will get usurped by the one your add-in just started. If that is a problem, then another solution is to add hooks to the SOLIDWORKS message loop for the modeless dialog or PropertyManager page instead of replacing the SOLIDWORKS message loop with one of your own. The following examples show how to do this.

- VB.NET: [Connect to SOLIDWORKS Message Pump to Handle Keystrokes and Accelerator Keys](Connect_to_SolidWorks_Message_Pump_Example_VB.NET.htm)
- C#: [Connect to SOLIDWORKS Message Pump to Handle Keystrokes and Accelerator Keys](Connect_to_SolidWorks_Message_Pump_Example_CSharp.htm)
