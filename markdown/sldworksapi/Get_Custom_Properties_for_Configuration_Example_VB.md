---
title: "Get Custom Properties for Configuration Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Custom_Properties_for_Configuration_Example_VB.htm"
---

# Get Custom Properties for Configuration Example (VBA)

This example shows how to get the names, types, and evaluated values of the custom properties in the active configuration. It also shows how to add a custom property to the configuration.

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

Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim config As SldWorks.Configuration
 Dim cusPropMgr As SldWorks.CustomPropertyManager
 Dim lRetVal As Long
 Dim vPropNames As Variant
 Dim vPropTypes As Variant
 Dim vPropValues As Variant
 Dim ValOut As String
 Dim ResolvedValOut As String
 Dim wasResolved As Boolean
 Dim linkToProp As Boolean
 Dim resolved As Variant
 Dim linkProp As Variant
 Dim nNbrProps As Long
 Dim j As Long
 Dim custPropType As Long
 Dim bRet As Boolean
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set config = swModel.GetActiveConfiguration

    Set cusPropMgr = config.CustomPropertyManager

    lRetVal = cusPropMgr.Add3("ADATE", swCustomInfoType_e.swCustomInfoDate, "4-13-59", swCustomPropertyAddOption_e.swCustomPropertyDeleteAndAdd)
     lRetVal = cusPropMgr.Get6("ADATE", False, ValOut, ResolvedValOut, wasResolved, linkToProp)

    bRet = cusPropMgr.IsCustomPropertyEditable("ADATE", config.Name)
     If bRet = True Then
         Debug.Print "    ADATE is editable."
         lRetVal = cusPropMgr.Set2("ADATE", "4-13-89")
     Else
         Debug.Print "    ADATE is not editable."
     End If

     lRetVal = cusPropMgr.Get6("ADATE", False, ValOut, ResolvedValOut, wasResolved, linkToProp)

    ' Get the number of custom properties for this configuration
     nNbrProps = cusPropMgr.Count
     Debug.Print "Number of properties for this configuration:            " & nNbrProps

    ' Gets the custom properties
     lRetVal = cusPropMgr.GetAll3(vPropNames, vPropTypes, vPropValues, resolved, linkProp)

     ' For each custom property, print its name, type, and evaluated value
     For j = 0 To nNbrProps - 1
         custPropType = cusPropMgr.GetType2(vPropNames(j))
         Debug.Print "    Name, swCustomInfoType_e value, and resolved value:  " & vPropNames(j) & ", "; custPropType & ", " & vPropValues(j)
     Next j

     lRetVal = cusPropMgr.Delete2("ADATE")

     ' Get the number of custom properties for this configuration
     nNbrProps = cusPropMgr.Count
     Debug.Print "Number of properties for this configuration:            " & nNbrProps
End Sub
```
