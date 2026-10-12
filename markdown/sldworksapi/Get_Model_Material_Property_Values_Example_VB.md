---
title: "Get Model Material Property Values Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Model_Material_Property_Values_Example_VB.htm"
---

# Get Model Material Property Values Example (VBA)

This example shows how to get the material property values of components in lightweight mode.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\TopAssembly1.SLDASM in lightweight
'    mode.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the material property values of the lightweight components in the
'    model.
' 2. Inspect the Immediate window.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swDoc As SldWorks.ModelDoc2
 Dim swADoc As SldWorks.AssemblyDoc
 Dim varComp As Variant
 Dim varMatProp As Variant
Option Explicit
 Sub main()
Set swApp = Application.SldWorks
 Set swDoc = swApp.ActiveDoc
 Set swADoc = swDoc
 varComp = swADoc.GetComponents(True)
 Dim I As Long
 For I = LBound(varComp) To UBound(varComp)
     Dim swComp As SldWorks.Component2
     Set swComp = varComp(I)

    varMatProp = swComp.GetModelMaterialPropertyValues(swComp.ReferencedConfiguration)
     If Not (IsEmpty(varMatProp)) Then
         Debug.Print (swComp.Name2 & "(" & I & ")" & "ConfigName : " & swComp.ReferencedConfiguration & "MatProp : ")
         Debug.Print "Red: " & (varMatProp(0)) * 255#
         Debug.Print "Green: " & (varMatProp(1)) * 255#
         Debug.Print "Blue: " & (varMatProp(2)) * 255#
         Debug.Print "Ambient: " & (varMatProp(3)) * 100# & "%"
         Debug.Print "Diffuse: " & (varMatProp(4)) * 100# & "%"
         Debug.Print "Specularity: " & (varMatProp(5)) * 100# & "%"
         Debug.Print "Shininess: " & (varMatProp(6)) * 100# & "%"
         Debug.Print "Transparency: " & (varMatProp(7)) * 100# & "%"
         Debug.Print "Emission: " & (varMatProp(8)) * 100# & "%"
     End If

    Debug.Print ""
 Next I
 varComp = Empty
 End Sub
```
