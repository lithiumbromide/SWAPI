---
title: "Create Attribute Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Attribute_Example_VB.htm"
---

# Create Attribute Example (VBA)

This example shows how to create an instance of attribute and display that attribute in the FeatureManager design tree.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects Cut-Extrude3.
' 3. Adds an attribute to the selected feature.
' 4. Rebuilds the part.
' 5. Expand Cut-Extrude3 in the FeatureManager design tree
'    to verify that the att 1 attribute added to that feature.
' 6. Examine the Immediate window.
'
' NOTES:
' * Attribute definition is as follows:
'   Name = "XML_string"
'   Parameter:
'     Name = "att_name"
'     Type = swParamTypeString
'   Parameter:
'     Name = "att_value"
'     Type = swParamTypeDouble
' * Attribute is not shown in FeatureManager design tree
'   until you rebuild, because attributes
'   are normally created hidden and refreshing the
'   FeatureManager design tree is an expensive operation.
' * Attributes are allocated by name, and the names must be
'   unique across the model.
' * The selected object must present the IEntity interface.
' * Because this part document is used elsewhere, do not save changes.
'----------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    '1 = invisible
    '0 = visible
    Const CreateVisible As Long = 0
    Const AttDefName As String = "XML_string"
    Const AttLenDimName As String = "att_name"
    Const AttLenValueName As String = "att_value"
    Const AttRootName As String = "att"
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As Object
    Dim swEnt As SldWorks.Entity
    Dim swAttDef As SldWorks.AttributeDef
    Dim swAtt As SldWorks.Attribute
    Dim swParamName As SldWorks.Parameter
    Dim swParamValue As SldWorks.Parameter
    Dim AttName As String
    Dim i As Long
    Dim bRet As Boolean
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    'Open part document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\smartcomponents\bearing.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Select feature
    Set swModelDocExt = swModel.Extension
    bRet = swModelDocExt.SelectByID2("Cut-Extrude3", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swEnt = swFeat
```

```
    'Set attribute
    Set swAttDef = swApp.DefineAttribute(AttDefName)
    bRet = swAttDef.AddParameter(AttLenDimName, swParamTypeString, 0#, 0)
    bRet = swAttDef.AddParameter(AttLenValueName, swParamTypeDouble, 0#, 0)
```

```
    bRet = swAttDef.Register
```

```
    While swAtt Is Nothing
        ' Get a unique attribute name
        i = i + 1
        AttName = AttRootName + Str(i)
        Set swAtt = swAttDef.CreateInstance5(swModel, swEnt, AttName, CreateVisible, swThisConfiguration)
    Wend
```

```
    Set swParamName = swAtt.GetParameter(AttLenDimName)
    Set swParamValue = swAtt.GetParameter(AttLenValueName)
```

```
    bRet = swParamName.SetStringValue2(AttName & " - " & AttLenDimName, swAllConfiguration, "")
    bRet = swParamValue.SetDoubleValue2(i * 10, swAllConfiguration, "")
```

```
    Debug.Print "File = " & swModel.GetPathName
    If Not swAtt Is Nothing Then
        Debug.Print "  " & AttDefName & "(" & i - 1 & ") = " & AttName
    Else
        Debug.Print "  Attribute not created."
    End If
```

```
    swModel.ForceRebuild3 True
```

```
End Sub
```
