---
title: "Group and Ungroup Components Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Group_Components_Example_VBNET.htm"
---

# Group and Ungroup Components Example (VB.NET)

This example shows how to:

- group the same components in the same configuration in an assembly into a folder in the FeatureManager design tree.
- ungroup the grouped components.

```
'---------------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\advdrawings\98food processor.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Groups the rubber feet components into rubber feet(Default)(5).
' 2. Examine the Immediate window and FeatureManager design tree.
' 3. Press F5.
' 4. Ungroups rubber feet(Default)(5).
' 5. Examine the Immediate window and FeatureManager design tree.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'---------------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swFeatureManager As FeatureManager
 	Dim swModelDocExt As ModelDocExtension
	Dim swAssemblyDoc As AssemblyDoc
	Dim status As Boolean

        swModel = swApp.ActiveDoc

    	'Group rubber feet components into rubber feet(Default)(5)
        swFeatureManager = swModel.FeatureManager
        swFeatureManager.GroupComponentInstances = True
        Debug.Print("Component instances grouped? " & swFeatureManager.GroupComponentInstances)
```

```
	Stop
	'Press F5

	'Ungroup rubber feet(Default)(5)
	swModelDocExt = swModel.Extension
	status = swModelDocExt.SelectByID2("rubber feet(Default)(5)", "FTRFOLDER", 0, 0, 0, False, 0, Nothing, 0)
	swAssemblyDoc = swModel
	status = swAssemblyDoc.UngroupComponents
	Debug.Print("Grouped components ungrouped? " & status)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
