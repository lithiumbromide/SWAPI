---
title: "Get Model Material Property Values Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Model_Material_Property_Values_Example_VBNET.htm"
---

# Get Model Material Property Values Example (VB.NET)

This example shows how to get the material property values of components in lightweight mode.

```vb
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swDoc As ModelDoc2
     Dim swADoc As AssemblyDoc
     Dim varComp As Object
     Dim varMatProp As Object

     Sub main()

         swDoc = swApp.ActiveDoc
         swADoc = swDoc
         varComp = swADoc.GetComponents(True)
         Dim I As  Long
         For I = LBound(varComp) To UBound(varComp)
             Dim swComp As Component2
             swComp = varComp(I)

             varMatProp = swComp.GetModelMaterialPropertyValues(swComp.ReferencedConfiguration)
             If Not (IsNothing(varMatProp)) Then
                 Debug.Print(swComp.Name2 & "(" & I & ")" & "ConfigName : " & swComp.ReferencedConfiguration & "MatProp : ")
                 Debug.Print("Red: " & (varMatProp(0)) * 255.0#)
                 Debug.Print("Green: " & (varMatProp(1)) * 255.0#)
                 Debug.Print("Blue: " & (varMatProp(2)) * 255.0#)
                 Debug.Print("Ambient: " & (varMatProp(3)) * 100.0# & "%")
                 Debug.Print("Diffuse: " & (varMatProp(4)) * 100.0# & "%")
                 Debug.Print("Specularity: " & (varMatProp(5)) * 100.0#   "%")
                 Debug.Print("Shininess: " & (varMatProp(6)) * 100.0# & "%")
                 Debug.Print("Transparency: " & (varMatProp(7)) * 100.0#   "%")
                 Debug.Print("Emission: " & (varMatProp(8)) * 100.0# & "%")
             End If

             Debug.Print("")
         Next I
         varComp = Nothing
     End Sub

     Public swApp As SldWorks

 End  Class
```
