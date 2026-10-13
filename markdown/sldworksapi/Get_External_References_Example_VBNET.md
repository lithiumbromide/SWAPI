---
title: "Get External References (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_External_References_Example_VBNET.htm"
---

# Get External References (VB.NET)

This example shows how to get a list of the external references for a selected component, selected feature, or document.

```vb
 '----------------------------------------------------------
 '  Preconditions:
 '  1. Open an assembly or part document.
 '  2. Select:
 '     * a component in an assembly document.
 '       - or -
 '     * a feature in an assembly or part document.
 '       - or -
 '     * Nothing in either type of document.
 '
 ' Postconditions: Examine the Immediate window
 ' to see the name of the part or assembly document
 ' and the external references for the  selected
 ' component, selected feature, or document.
 '----------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swModDocExt As ModelDocExtension
         Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim swComp As Component2
         Dim vModelPathName As Object = Nothing
         Dim vComponentPathName As Object = Nothing
         Dim vFeature As Object = Nothing
         Dim vDataType As Object = Nothing
         Dim vStatus As Object = Nothing
         Dim vRefEntity As Object = Nothing
         Dim vFeatComp As Object = Nothing
        Dim vConfigOpt As Object = Nothing
         Dim vConfigName As Object = Nothing
         Dim nConfigOpt As Integer
         Dim sConfigName As String
         Dim nRefCount As Integer
         Dim nSelType As Integer
         Dim i As  Integer

         swApp = CreateObject("SldWorks.Application")
         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager

         swModDocExt = swModel.Extension
         nSelType = swSelMgr.GetSelectedObjectType3(1, -1)

         Select Case nSelType

             ' Selected component in an assembly
             Case swSelectType_e.swSelCOMPONENTS
                 swComp = swSelMgr.GetSelectedObjectsComponent3(1, -1)
                 nRefCount = swComp.ListExternalFileReferencesCount
                 swComp.ListExternalFileReferences2(vModelPathName, vComponentPathName, vFeature, vDataType, vStatus, vRefEntity, vFeatComp, nConfigOpt, sConfigName)

                 swModel = swComp.GetModelDoc2
        Debug.Print("Model name = " + swModel.GetPathName)
         Debug.Print("    Reference count        = " + Str(nRefCount))
         Debug.Print("")
         For i = 0 To nRefCount - 1
             Debug.Print("    Model path + name      = " + vModelPathName(i))
             Debug.Print("    Component path + name  = " + vComponentPathName(i))
             Debug.Print("    Feature                = " + vFeature(i))
             Debug.Print("    Data type              = " + vDataType(i))
             Debug.Print("    Status                 = " + Str(vStatus(i)))
             Debug.Print("    Reference entity       = " + vRefEntity(i))
             Debug.Print("    Feature component      = " + vFeatComp(i))
         Next i

         Debug.Print("    Configuration option   = " & nConfigOpt)
         Debug.Print("    Configuration name     = " & sConfigName)
         Debug.Print("")

                 ' Selected feature in a part or assembly
             Case swSelectType_e.swSelBODYFEATURES, swSelectType_e.swSelSKETCHES
                 swFeat = swSelMgr.GetSelectedObject6(1, -1)
                 nRefCount = swFeat.ListExternalFileReferencesCount
                 swFeat.ListExternalFileReferences2(vModelPathName, vComponentPathName, vFeature, vDataType, vStatus, vRefEntity, vFeatComp, nConfigOpt, sConfigName)

         Debug.Print("Model name = " + swModel.GetPathName)
         Debug.Print("    Reference count        = " + Str(nRefCount))
         Debug.Print("")
         For i = 0 To nRefCount - 1
             Debug.Print("    Model path + name      = " + vModelPathName(i))
             Debug.Print("    Component path + name  = " + vComponentPathName(i))
             Debug.Print("    Feature                = " + vFeature(i))
             Debug.Print("    Data type              = " + vDataType(i))
             Debug.Print("    Status                 = " + Str(vStatus(i)))
             Debug.Print("    Reference entity       = " + vRefEntity(i))
             Debug.Print("    Feature component      = " + vFeatComp(i))
         Next i

         Debug.Print("    Configuration option   = " & nConfigOpt)
         Debug.Print("    Configuration name     = " & sConfigName)
         Debug.Print("")
                 ' Part or assembly
             Case Else
                 nRefCount = swModDocExt.ListExternalFileReferencesCount
                 swModDocExt.ListExternalFileReferences2(vModelPathName, vComponentPathName, vFeature, vDataType, vStatus, vRefEntity, vFeatComp, vConfigOpt, vConfigName)
 Debug.Print("Model name = " + swModel.GetPathName)
         Debug.Print("    Reference count        = " + Str(nRefCount))
         Debug.Print("")
         For i = 0 To nRefCount - 1
             Debug.Print("    Model path + name      = " + vModelPathName(i))
             Debug.Print("    Component path + name  = " + vComponentPathName(i))
             Debug.Print("    Feature                = " + vFeature(i))
             Debug.Print("    Data type              = " + vDataType(i))
             Debug.Print("    Status                 = " + Str(vStatus(i)))
             Debug.Print("    Reference entity       = " + vRefEntity(i))
             Debug.Print("    Feature component      = " + vFeatComp(i))
             Debug.Print("    Configuration option   = " & vConfigOpt(i))
             Debug.Print("    Configuration name     = " & vConfigName(i))
             Debug.Print("")
 Next i
         End Select

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End  Class
```
