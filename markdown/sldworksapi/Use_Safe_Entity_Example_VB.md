---
title: "Use Safe Entity Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Use_Safe_Entity_Example_VB.htm"
---

# Use Safe Entity Example (VBA)

This example shows how to use the safe entity functionality.

**NOTE:** In general, an entity is something that can be selected through the SOLIDWORKS Design user interface. Examples of safe entities include vertices, edges, faces, and features. An entity is useful because you can add an attribute to it to store arbitrary user information. Entities are also useful because they support direct selection through IEntity::Select4. Under normal conditions, an entity is transient and is not valid when the model is rebuilt. Thus, if a rebuild occurs, then the entity must be reacquired. This can be time consuming and prone to errors. Furthermore, it increases the programming complexity. Safe entities are valid across rebuilds of the model. However, this type of entity is not valid across sessions of SOLIDWORKS Design.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a part, fully resolved assembly, or drawing.
' 2. Select one of these entities in the graphics area:
'    * vertex
'    * edge
'    * face
'    * feature
'
' Postconditions:
' 1. Rebuilds the model.
' 2. Reselects the entity.
'
' NOTE: This code does not work for a feature selected
' in the FeatureManager design tree in a drawing.
'------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim swEnt As SldWorks.Entity
    Dim swSafeEnt  As SldWorks.Entity
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
```

```
    ' Select safe entity
    Set swSelMgr = swModel.SelectionManager
    Set swEnt = swSelMgr.GetSelectedObject6(1, -1)
    Set swSafeEnt = swEnt.GetSafeEntity
```

```
    ' Clear any selections
    bRet = swModel.ForceRebuild3(False)
```

```
   ' Selection still works because entity is safe
    Set swSelData = swSelMgr.CreateSelectData
    bRet = swSafeEnt.Select4(True, swSelData)
```

```
    Debug.Print "Number of safe entities selected = " & swSelMgr.GetSelectedObjectCount
```

```
End Sub
```
