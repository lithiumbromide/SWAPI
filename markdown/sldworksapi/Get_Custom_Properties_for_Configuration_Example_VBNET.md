---
title: "Get Custom Properties for Configuration Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Custom_Properties_for_Configuration_Example_VBNET.htm"
---

# Get Custom Properties for Configuration Example (VB.NET)

This example shows how to get the names, types, values, and evaluated values of the active configuration's custom properties. It also shows how to add a custom property to the configuration.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
  ' 1. Adds a date custom property to the part's configuration.
  ' 2. Tests whether the custom property is editable, and if so,
 '    edits it.
  ' 3. Gets all custom properties in the configuration.
 ' 4. Deletes a custom property.
 ' 5. Examine the Immediate window.
  '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim config As Configuration
     Dim cusPropMgr As CustomPropertyManager
     Dim lRetVal As Integer
     Dim vPropNames As Object
     Dim vPropTypes As Object
     Dim vPropValues As Object
     Dim ValOut As String
     Dim ResolvedValOut As String
     Dim wasResolved As Boolean
     Dim linkToProp As Boolean
     Dim resolved As Object
     Dim linkProp As Object
     Dim nNbrProps As Integer
     Dim j As Integer
     Dim custPropType As Integer
     Dim bRet As Boolean

     Sub main()

         swModel = swApp.ActiveDoc
         config = swModel.GetActiveConfiguration

         cusPropMgr = config.CustomPropertyManager

         lRetVal = cusPropMgr.Add3("ADATE", swCustomInfoType_e.swCustomInfoDate, "4-13-59", swCustomPropertyAddOption_e.swCustomPropertyDeleteAndAdd)
         lRetVal = cusPropMgr.Get6("ADATE", False, ValOut, ResolvedValOut, wasResolved, linkToProp)
         bRet = cusPropMgr.IsCustomPropertyEditable("ADATE", config.Name)
         If bRet = True Then
             Debug.Print("ADATE is editable. Change the date.")
             lRetVal = cusPropMgr.Set2("ADATE", "4-13-89")
         Else
             Debug.Print("ADATE is not editable.")
         End If

         lRetVal = cusPropMgr.Get6("ADATE", False, ValOut, ResolvedValOut, wasResolved, linkToProp)

         ' Get the number of custom properties for this configuration
         nNbrProps = cusPropMgr.Count
         Debug.Print("Number of custom properties for this configuration:            " & nNbrProps)

         ' Get the custom properties
         lRetVal = cusPropMgr.GetAll3(vPropNames, vPropTypes, vPropValues, resolved, linkProp)

         ' For each custom property, print its name, type, and evaluated value
         For j = 0 To nNbrProps - 1
             custPropType = cusPropMgr.GetType2(vPropNames(j))
             Debug.Print("Name, swCustomInfoType_e value, and resolved value:  " & vPropNames(j) & ", " & custPropType & ", " & vPropValues(j))
         Next j

         lRetVal = cusPropMgr.Delete2("ADATE")

         ' Get the number of custom properties for this configuration
         nNbrProps = cusPropMgr.Count
         Debug.Print("Number of custom properties for this configuration:            " & nNbrProps)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
