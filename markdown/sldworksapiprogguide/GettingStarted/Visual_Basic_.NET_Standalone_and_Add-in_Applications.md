---
title: "Visual Basic .NET Standalone and Add-in Applications"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Visual_Basic_.NET_Standalone_and_Add-in_Applications.htm"
---

# Visual Basic .NET Standalone and Add-in Applications

### Standalone Applications (.exe files)

To create an instance of SOLIDWORKS, your project should contain lines of code similar to the following:

```vb
Sub Main
    Dim swApp As SldWorks.SldWorks
    swApp = New SldWorks.SldWorks()
    swApp.ExitApp
    swApp = Nothing
End Sub
```

Additionally, you must have added [references to the SOLIDWORKS type libraries](../Overview/Type_Libraries.htm).

### Add-in Applications (.dll files)

You can create a Visual Basic .NET DLL add-in using the SOLIDWORKS VB.NET Add-in Template included in the [SOLIDWORKS API SDK](SolidWorks_API_Getting_Started_Overview.htm). See [SOLIDWORKS VB.NET Add-in Template](../Overview/Using_SolidWorks_VB.NET_Add-In_Wizard_to_Create_VB.NET_Add-In.htm) for details.
