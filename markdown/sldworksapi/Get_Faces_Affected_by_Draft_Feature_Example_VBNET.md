---
title: "Get Faces Affected by Draft Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Faces_Affected_by_Draft_Feature_Example_VBNET.htm"
---

# Get Faces Affected by Draft Feature Example (VB.NET)

This example shows how to get the faces affected by a draft feature.

**NOTE:** In SOLIDWORKS Design, a feature is comprised of faces. The faces created by a feature can be retrieved using IFeature::GetFaces. However, certain types of features only affect existing faces and do not create any new faces. Examples of these types of features are draft and scale features. For these features, IFeature::GetFaces returns an empty array (no faces). This sample code shows how to use IDraftFeatureData2::GetDraftedEntities to get the faces affected by a draft feature.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part or assembly with a draft feature.
 ' 2. If you opened an assembly, then fully resolve the assembly if necessary.
 ' 3. Select a draft feature.
 '
 ' Postconditions:
 ' 1. Deselects the draft feature.
 ' 2. Selects the faces affected by the draft feature.
 ' 3. Gets the type of draft feature as defined in swDraftFeature_e.
 ' 4. Examine the Immediate window and graphics area.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swSelData As SelectData
         Dim swFeat As Feature
         Dim swDraftFeat As DraftFeatureData2
         Dim vEnt As Object
         Dim vEntArr As Object
         Dim swEnt As Entity
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swSelData = swSelMgr.CreateSelectData
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swDraftFeat = swFeat.GetDefinition

         ' Type as defined in swDraftType_e
         Debug.Print(swDraftFeat.Type)

         swModel.ClearSelection2(True)

         ' No need to roll back to get affected faces
         vEntArr = swDraftFeat.GetDraftedEntities
         For Each vEnt In vEntArr
             swEnt = vEnt
             bRet = swEnt.Select4(True, swSelData)
         Next
     End Sub

     Public swApp As SldWorks

 End  Class
```
