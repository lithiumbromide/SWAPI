---
title: "Get Names of Available Printers Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Names_of_Available_Printers_Example_VBNET.htm"
---

# Get Names of Available Printers Example (VB.NET)

This example shows how to get the names of the printers available to your computer to which you can print.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create VB.NET Windows console project.
' 2. Copy and paste this project into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.
' 4. Start DraftSight.
' 5. Open the Immediate window.
' 6. Run the macro.
'
' Postconditions: The names of available printers are written
' to the Immediate window.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation

Module Module1

    Sub Main()

        Dim dsApp As Application

        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")

        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand()

        'Get list of available printers
        Dim dsPrintMgr As PrintManager
        dsPrintMgr = dsApp.GetPrintManager()
        Dim printArray() As String
        Dim i As Integer
        printArray = dsPrintMgr.GetAvailablePrinters()
        'Print names of available printers
        If printArray IsNot Nothing Then
            Debug.Print("Available printers:")
            For i = LBound(printArray) To UBound(printArray)
                Debug.Print("  " & printArray(i))
            Next i
        End If
```

```
    End Sub

End Module
```
