---
title: "Close Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Close_Document_Example_VB.htm"
---

# Close Document Example (VBA)

This example shows how to create new parts and close the parts by name.

```
'---------------------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document titled Part1 and gets its title.
' 2. Opens another new part document titled Part2 and gets
'    its title.
' 3. Release the pointer to Part2 and closes Part2.
' 4. Activates Part1.
'---------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part1 As SldWorks.PartDoc
Dim Part2 As SldWorks.PartDoc
Dim partTitle1 As String
Dim partTitle2 As String
Dim errors As Long
```

```
Sub main()
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    ' Open a new part
    Set Part1 = swApp.NewPart
```

```
    ' Get the part's title
    partTitle1 = Part1.GetTitle
    Debug.Print "Part1's title: " & partTitle1
```

```
    ' Open another new part
    Set Part2 = swApp.NewPart
```

```
    ' Get the part's title
    partTitle2 = Part2.GetTitle
    Debug.Print "Part2's title: " & partTitle2
```

```
    ' Release the pointer to Part2
    Set Part2 = Nothing
```

```
    ' Close the Part2
    swApp.CloseDoc partTitle2
```

```
    ' Activate Part1
    Set Part1 = swApp.ActivateDoc2(partTitle1, True, errors)
    If ((errors <> 0) Or (Part1 Is Nothing)) Then
        swApp.SendMsgToUser "Error activating Part1 document"
    End If
```

```
End Sub
```
