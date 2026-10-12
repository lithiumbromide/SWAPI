---
title: "Get Material Property Values Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Material_Property_Values_Example_VB.htm"
---

# Get Material Property Values Example (VBA)

This example shows how to get the color, a material property value, applied to each body in a part.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a part to which color is applied
'    to one or more bodies.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the color on each body in a part.
' 2. Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Public Enum swBodyType_e
    swSolidBody = 0
    swSheetBody = 1
    swWireBody = 2
    swMinimumBody = 3
    swGeneralBody = 4
    swEmptyBody = 5
End Enum
```

```
Sub ProcessBodyArray(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, vBodyArr As Variant)
    Dim vBody As Variant
    Dim swBody As SldWorks.Body2
    Dim vMatProp As Variant
```

```
    For Each vBody In vBodyArr
        Set swBody = vBody
        vMatProp = swBody.MaterialPropertyValues2
        If IsEmpty(vMatProp) Then
            Debug.Print "    No color information."
        Else
            Debug.Print "    RGB            = [" & vMatProp(0) * 255# & ", " & vMatProp(1) * 255# & ", " & vMatProp(2) * 255# & "]"
            Debug.Print "    Ambient        = " & vMatProp(3)
            Debug.Print "    Diffuse        = " & vMatProp(4)
            Debug.Print "    Specular       = " & vMatProp(5)
            Debug.Print "    Shininess      = " & vMatProp(6)
            Debug.Print "    Transparency   = " & vMatProp(7)
            Debug.Print "    Emission       = " & vMatProp(8)
            Debug.Print ""
        End If
    Next
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim vBodyArr As Variant
    Dim i  As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    For i = 0 To 5
        vBodyArr = swPart.GetBodies2(i, False)
        If Not IsEmpty(vBodyArr) Then
            Debug.Print "  Body[" & i & "] = " & UBound(vBodyArr) + 1
            ProcessBodyArray swApp, swModel, vBodyArr
        End If
    Next i
```

```
End Sub
```
