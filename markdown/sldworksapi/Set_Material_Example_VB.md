---
title: "Set Material Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Material_Example_VB.htm"
---

# Set Material Example (VBA)

This example shows how to get the names of the material schema, material databases, and bodies in a part document. This example also shows how to apply a SOLIDWORKS Design Material to all of the bodies in a part document.

```
'----------------------------------------------------
' Preconditions:
' 1. Verify that the specified document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Applies the material ABS PC (polycarbonate plastic)
'    from the Material database to all
'    bodies in the part.
' 3. To verify, examine:
'    * DisplayManager tab
'    * graphics area
'    * Immediate window
'
' NOTE: Because the part document is used elsewhere,
' do not save changes.
'----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swBody As SldWorks.Body2
    Dim errors As Long
    Dim warnings As Long
    Dim vMatDBarr As Variant
    Dim vMatDB As Variant
    Dim Bodies As Variant
    Dim BodyMaterialError As Long
    Dim sMatName As String
    Dim sMatDB As String
    Dim itr As Long
    Dim boolstat As Boolean
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open the document
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt", swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set swPart = swModel
```

```
    ' Get the material schema and names
    ' of available materials databases
    vMatDBarr = swApp.GetMaterialDatabases
    Debug.Print "Material schema pathname = " & swApp.GetMaterialSchemaPathName
    For Each vMatDB In vMatDBarr
        Debug.Print "  Material database: " & vMatDB
    Next
```

```
    Debug.Print ""
```

```
    Bodies = swPart.GetBodies2(swAllBodies, False)
    For itr = 0 To UBound(Bodies)
        Set swBody = Bodies(itr)
        ' Get the name of the body
        Debug.Print swBody.Name
        boolstat = swBody.Select2(False, Nothing)
        ' Set the SOLIDWORKS Design material for that body
        BodyMaterialError = swBody.SetMaterialProperty("Default", "solidworks materials.sldmat", "ABS PC")
```

```
        ' Comment out previous statement and uncomment following statement to use custom material
        'BodyMaterialError = swBody.SetMaterialProperty("Default", "custom materials.sldmat", "Custom Plastic")
```

```
        ' Get the names of the body's material and the
        ' database to which it belongs
        sMatName = swBody.GetMaterialPropertyName("", sMatDB)
        If sMatName = "" Then
            Debug.Print ("Body " & itr & "'s material name: No material applied")
        Else
            Debug.Print ("Body " & itr & "'s material name: " & sMatName)
            Debug.Print ("Body " & itr & "'s material database: " & sMatDB)
            Debug.Print (" ")
        End If
```

```
    Next itr
```

```
End Sub
```
