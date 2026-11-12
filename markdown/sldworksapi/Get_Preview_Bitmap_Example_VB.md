---
title: "Get Preview Bitmap Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Preview_Bitmap_Example_VB.htm"
---

# Get Preview Bitmap Example (VBA)

This example shows how to get the preview bitmap in a SOLIDWORKS Design document.

```
'----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document exists.
' 2. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'----------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Dim p As stdole.StdPicture  'See MSDN for details about the StdPicture object
    Dim fileName As String
```

```
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\centerlink.sldprt"
    Set p = swApp.GetPreviewBitmap(fileName, "Default")
    Debug.Print "Handle: " & p.Handle
    Debug.Print "Height: " & p.Height
    Debug.Print "Width: " & p.Width
    Debug.Print "Type (1 = bitmap): " & p.Type
```

```
End Sub
```
