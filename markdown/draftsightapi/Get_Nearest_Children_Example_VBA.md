---
title: "Get Nearest Children Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Nearest_Children_Example_VBA.htm"
---

# Get Nearest Children Example (VBA)

This example shows how get the nearest child external references in an unopened drawing.

```vb
  '--------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VBA macro in a software product in which VBA is
 '    embedded.
 ' 2. Copy and paste this example into the Visual Basic IDE.
 ' 3. Add a reference to the DraftSight type library,
 '    install_dir\bin\dsAutomation.dll.
 ' 4. Replace the first parameter of GetImmediateChildReferences
'    with your local drawing that contains an external reference.
 ' 5. Start DraftSight with an empty drawing.
 ' 6. Run the macro.
 '
 ' Postconditions: See the DraftSight Command Window for output
 ' messages and all of the specified drawing's nearest child references.
  '--------------------------------------------------------------
 Option Explicit

 Sub main()

     Dim dsApp As DraftSight.Application
     Dim dsRefMgr As DraftSight.ReferenceManager
     Dim dsImageDefinition As DraftSight.ImageDefinition
    Dim dsPdfDefinition As DraftSight.PdfDefinition
    Dim dsDgnDefinition As DraftSight.DgnDefinition
     Dim extDefTypeArray As Variant
     Dim extDefArray As Variant
     Dim commandline As DraftSight.CommandMessage

     'Connect to DraftSight
     Set dsApp = GetObject(, "DraftSight.Application")

     'Abort any command currently running in DraftSight
     'to avoid nested commands
     dsApp.AbortRunningCommand

     Set commandline = dsApp.GetCommandMessage()

     Set dsRefMgr = dsApp.GetReferenceManager()

     'Get all nearest child references of the specified document
     dsRefMgr.GetImmediateChildReferences "C:\temp\dwgWithRef.dwg", extDefTypeArray, extDefArray

     Dim objecttype As dsObjectType_e
     Dim objectdefinition As Object
     Dim i As Long

     For i = 0 To UBound(extDefTypeArray)

         objecttype = extDefTypeArray(i)
         Set objectdefinition = extDefArray(i)

         If (objecttype = dsObjectType_e.dsImageDefinitionType) Then
             Set dsImageDefinition = objectdefinition
             commandline.PrintLine "Path: " & dsImageDefinition.GetPath()
             commandline.PrintLine "Found In Path: " & dsImageDefinition.GetFoundInPath()
         ElseIf (objecttype = dsObjectType_e.dsPdfDefinitionType) Then
             Set dsPdfDefinition = objectdefinition
             commandline.PrintLine "Path: " & dsPdfDefinition.GetPath()
             commandline.PrintLine "Found In Path: " & dsPdfDefinition.GetFoundInPath()
         ElseIf (objecttype = dsObjectType_e.dsDgnDefinitionType) Then
             Set dsDgnDefinition = objectdefinition
             commandline.PrintLine "Path: " & dsDgnDefinition.GetPath()
             commandline.PrintLine "Found In Path: " & dsDgnDefinition.GetFoundInPath()
         End If
     Next

 End Sub
```
