---
title: "Get Custom Properties of Referenced Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Custom_Properties_of_Referenced_Part_Example_VBNET.htm"
---

# Get Custom Properties of Referenced Part Example (VB.NET)

This example shows how to get the custom property data of a referenced part.

```vb
 '----------------------------------------------------
 ' Preconditions:
 ' 1. Open a part that contains a referenced part
 '    with a custom property and a value.
 ' 2. Open the referenced part.
 ' 3. Switch back to the part opened in step 1.
 ' 4. In the macro, replace Property_Name with the name of
 '    the referenced part's custom property.
 ' 5. Open the Immediate window.
 '
 ' Postconditions: Prints the custom property data
 ' to the Immediate window.
 '---------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swCustProp As CustomPropertyManager
         Dim val As String = ""
         Dim valout As String = ""
         Dim bool As Boolean

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension

         ' Get the custom property data
         swCustProp = swModelDocExt.CustomPropertyManager("")
         bool = swCustProp.Get4("Property_Name", False, val, valout)

         Debug.Print("Value:                    " & val)
         Debug.Print("Evaluated value:          " & valout)
         Debug.Print("Up-to-date data:          " & bool)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End  Class
```
