---
title: "Insert a Note Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_a_Note_Example_VBNET.htm"
---

# Insert a Note Example (VB.NET)

This example shows show to insert a geometric tolerance symbol in an active drawing document.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
 '
 ' Postconditions:
 ' 1. Inserts a a geometric tolerance symbol at the specified position.
 ' 2. Examine the graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
```

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Partial Class SolidWorksMacro

```vb
Sub main()
```

```vb
Dim Part As ModelDoc2
 Dim Annotation As Annotation
 Dim swSelobj2 As Object
 Dim swSelMgr As SelectionMgr
 Dim Note As Note
 Dim boolstatus As Boolean
 Dim longstatus As Integer

 Part = swApp.ActiveDoc
 swSelMgr = Part.SelectionManager
 boolstatus = Part.Extension.SelectByID2("", "EDGE", 0.166288048468037, 0.223859686746988, -0.000400000000013279,  False, 0, Nothing, 0)
 swSelobj2 = swSelMgr.GetSelectedObject6(1, -1)
 Note = Part.InsertNote("<MOD-CL>")
 If Not Note Is Nothing Then
```

```vb
Note.Angle = 0
 boolstatus = Note.SetBalloon(0, 0)
 Annotation = Note.GetAnnotation()
```

Dim AttEntArr(0) As Object
AttEntArr(0) = swSelobj2
Dim vAttEntArrIn As Object
vAttEntArrIn = AttEntArr
boolstatus = Annotation.**SetAttachedEntities**(vAttEntArrIn)
If Not Annotation Is Nothing Then

```vb
longstatus = Annotation.SetLeader3(1, 0,
```

True, True, False, False)
boolstatus = Annotation.**SetPosition2**(0.1038962799325, 0.135343450253, 0)

```vb
End If
```

```vb
End If
 Part.ClearSelection2(True)
 Part.WindowRedraw()
End Sub
Public swApp As SldWorks

 End  Class
```
