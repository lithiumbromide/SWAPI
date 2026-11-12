---
title: "Get Names of Available Printers Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Names_of_Available_Printers_Example_VBA.htm"
---

# Get Names of Available Printers Example (VBA)

This example shows how to get the names of the printers available to your computer to which you can print.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight.
' 5. Open the Immediate window.
' 6. Run the macro.
'
' Postcondition: The names of the available printers are written
' to the Immediate window.
'----------------------------------------------------------------
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get list of available printers
    Dim dsPrintMgr As DraftSight.PrintManager
    Set dsPrintMgr = dsApp.GetPrintManager
    Dim printArray() As String
    Dim i As Long
    printArray = dsPrintMgr.GetAvailablePrinters
```

```
   'Print names of available printers
    If Not IsEmpty(printArray) Then
       	Debug.Print ("Available printers:")
       	For i = LBound(printArray) To UBound(printArray)
		Debug.Print ("  " & printArray(i))
       	Next i
    End If
```

```
End Sub
```
