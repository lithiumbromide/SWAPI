---
title: "Set and Get Paths of Interface Files Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Set_and_Get_Paths_of_Interface_Files_Example_VBNET.htm"
---

# Set and Get Paths of Interface Files Example (VB.NET)

This example shows how to set and get the paths of interface files.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add a reference to System.Windows.Forms.
' 5. Start DraftSight.
' 6. Press F5.
'
' Postconditions:
' 1. Connects to DraftSight.
' 2. Sets different alias, custom icon, customization, and
'    menu file paths.
' 3. Gets different alias, custom icon, customization, and
'    menu file paths. Click OK to click each message box.
'
' NOTE: To verify, you can also click Tools > Options >
' File Locations and expand Interface. Then expand and
' examine Alias File Location, Custom Icon Location,
' Customization File, and Menu Files.
'--------------------------------------------------------------
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

        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand()

        Dim dsInterfaceFiles As InterfaceFiles = dsApp.GetInterfaceFiles()
        If dsInterfaceFiles Is Nothing Then
            MessageBox.Show("There are no valid interface files.")
            Return
        End If

        'Set and get different file paths
        dsInterfaceFiles.AliasFilePath = "C:\Program Files\Dassault Systemes\DraftSight\Default Files\Alias"

        dsInterfaceFiles.CustomIconPath = ""

        dsInterfaceFiles.CustomizationFilePath = ""

        dsInterfaceFiles.MenuFilesPath = "C:\Program Files\Dassault Systemes\DraftSight\Default Files\StartupMenu\english"

        MessageBox.Show("Alias file path: " + dsInterfaceFiles.AliasFilePath)
        MessageBox.Show("Custom icon path: " + dsInterfaceFiles.CustomIconPath)
        MessageBox.Show("Customization file path: " + dsInterfaceFiles.CustomizationFilePath)
        MessageBox.Show("Menu files path: " + dsInterfaceFiles.MenuFilesPath)

    End Sub
End Module
```
