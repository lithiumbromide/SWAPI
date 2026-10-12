---
title: "Find Attribute Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Find_Attribute_Example_VB.htm"
---

# Find Attribute Example (VBA)

This example shows how to find an attribute on the selected entity.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects Cut-Extrude3.
' 3. Adds attribute att 1 to the selected feature.
' 4. Rebuilds the part.
' 5. Finds attribute att 1.
' 6. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------
Option Explicit
```

```
Dim traverseLevel As Integer
Dim expandThis As Boolean
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
    Dim swFeat As SldWorks.Feature
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
    'Set attribute att 1
    Set swAttDef = swApp.DefineAttribute(AttDefName)
    bRet = swAttDef.AddParameter(AttLenDimName, swParamTypeString, 0#, 0)
    bRet = swAttDef.AddParameter(AttLenValueName, swParamTypeDouble, 0#, 0)
    bRet = swAttDef.Register
    While swAtt Is Nothing
        ' Get a unique attribute name
        i = i + 1
        AttName = AttRootName + Str(i)
        Set swAtt = swAttDef.CreateInstance5(swModel, swEnt, AttName, CreateVisible, swThisConfiguration)
    Wend
    Set swParamName = swAtt.GetParameter(AttLenDimName)
    Set swParamValue = swAtt.GetParameter(AttLenValueName)
    bRet = swParamName.SetStringValue2(AttName & " - " & AttLenDimName, swAllConfiguration, "")
    bRet = swParamValue.SetDoubleValue2(i * 10, swAllConfiguration, "")
    If Not swAtt Is Nothing Then
        Debug.Print "Attribute " & AttName & " created."
    Else
        Debug.Print "Attribute " & AttName & " not created."
    End If
```

```
    swModel.ForceRebuild3 True
```

```
    'Find attribute att 1
    bRet = swModelDocExt.SelectByID2("att 1", "ATTRIBUTE", 0, 0, 0, False, 0, Nothing, 0)
    Set swEnt = swSelMgr.GetSelectedObject6(1, -1)
```

```
    'Limit search in case attribute does not exist
    While swAtt Is Nothing And i < 300
        Set swAtt = swEnt.FindAttribute(swAttDef, i)
        i = i + 1
    Wend
```

```
    If Not swAtt Is Nothing Then
        If False = swAtt.GetEntityState(swIsEntityInvalid) And False = swAtt.GetEntityState(swIsEntitySuppressed) And False = swAtt.GetEntityState(swIsEntityAmbiguous) And False = swAtt.GetEntityState(swIsEntityDeleted) Then
            Set swParamName = swAtt.GetParameter(AttLenDimName)
            Set swParamValue = swAtt.GetParameter(AttLenValueName)
            Debug.Print "Attribute " & swParamName.GetStringValue & " found."
            Debug.Print "    Value = " & swParamValue.GetDoubleValue
        Else
            Debug.Print "  Attribute found, but problems exist."
        End If
    Else
        Debug.Print "  Attribute not found."
    End If
```

```
End Sub
```
