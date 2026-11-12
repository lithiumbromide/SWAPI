---
title: "Get Nearest Children Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Nearest_Children_Example_VBNET.htm"
---

# Get Nearest Children Example (VB.NET)

This example shows how get the nearest child external references in an unopened drawing.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Replace the first parameter of GetImmediateChildReferences
'    with your local drawing that contains an external reference.
' 5. Start DraftSight with an empty drawing.
' 6. Start debugging the project.
'
' Postconditions: See the DraftSight Command Window for output
' messages and all of the specified drawing's nearest child references.
'----------------------------------------------------------------
```

```vb
 Imports DraftSight.Interop.dsAutomation
 Module   Module1

       Sub Main()
            Dim dsApp  As Application
        Dim dsRefMgr  As ReferenceManager
          Dim dsImageDefinition  As ImageDefinition
         Dim dsPdfDefinition  As PdfDefinition
         Dim dsDgnDefinition  As DgnDefinition
            Dim extDefTypeArray(0)  As   Integer
            Dim extDefArray(0)  As   Object
            Dim commandline  As CommandMessage

            'Connect to DraftSight
           dsApp = GetObject(,   "DraftSight.Application")

            'Abort any command currently running in DraftSight
            'to avoid nested commands
           dsApp.AbortRunningCommand

           commandline = dsApp.GetCommandMessage()
        dsRefMgr = dsApp.GetReferenceManager()
```

```vb
          'Get all nearest child references of the specified document
           dsRefMgr.GetImmediateChildReferences("C:\temp\dwgWithRef.dwg",extDefTypeArray, extDefArray)

            Dim objecttype  As dsObjectType_e
            Dim objectdefinition  As   Object
            Dim i  As   Integer

            For i = 0  To UBound(extDefTypeArray)

              objecttype = extDefTypeArray(i)
              objectdefinition = extDefArray(i)

               If (objecttype = dsObjectType_e.dsImageDefinitionType)  Then
                  dsImageDefinition = objectdefinition
                  commandline.PrintLine("Path: " & dsImageDefinition.GetPath())
                  commandline.PrintLine("Found In Path: " & dsImageDefinition.GetFoundInPath())
               ElseIf (objecttype = dsObjectType_e.dsPdfDefinitionType)  Then
                  dsPdfDefinition = objectdefinition
                  commandline.PrintLine("Path: " & dsPdfDefinition.GetPath())
                  commandline.PrintLine("Found In Path: " & dsPdfDefinition.GetFoundInPath())
               ElseIf (objecttype = dsObjectType_e.dsDgnDefinitionType)  Then
                  dsDgnDefinition = objectdefinition
                  commandline.PrintLine("Path: " & dsDgnDefinition.GetPath())
                  commandline.PrintLine("Found In Path: " & dsDgnDefinition.GetFoundInPath())
               End  If
            Next
       End  Sub

 End  Module
```
