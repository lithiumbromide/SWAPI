---
title: "Select Connector Using Highlight Search Tool Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Select_Connector_Using_Highlight_Search_Tool_Example_VBNET.htm"
---

# Select Connector Using Highlight Search Tool Example (VB.NET)

This example shows how to select a connector using the SOLIDWORKS Routing Highlight Search tool.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Open an assembly document containing an electrical route and
 '    connector (3pin) female-1.
 ' 2. In SOLIDWORKS, select Tools > Add-Ins > SOLIDWORKS Routing.
  ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
  '    click Launch Routing Library Manager and set the locations of your
 '    SOLIDWORKS Routing files.
 ' 4. In the IDE, right-click the project,
 '    click Add Reference, browse install_dir\api\redist, select
 '    SolidWorks.Interop.SwRoutingLib.dll, and click OK.
 ' 5. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Finds the specified component.
  ' 2. Prints the number of instances of the specified component.
 ' 3. Selects the component in the FeatureManager design tree.
  ' 4. Prints the number of components attached to the selected component.
  ' 5. Colors the selected component gray in the graphics area.
 ' 6. Inspect the Immediate window, the FeatureManager design tree,
 '    and the graphics area.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.SWRoutingLib
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swAssemblyDoc As AssemblyDoc
     Dim rtRouteMgr As RouteManager
     Dim rtAdvancedRouteSelector As AdvancedRouteSelector
     Dim nbrConnectors As Long
     Dim selName As Object
     Dim attachNames As Object

     Sub main()

         swModel = swApp.ActiveDoc
         swAssemblyDoc = swModel

         ' Get SOLIDWORKS RouteManager
         rtRouteMgr = swAssemblyDoc.GetRouteManager()

         ' Access the Highlight Search tool
         rtAdvancedRouteSelector = rtRouteMgr.GetAdvancedRouteSelector

         ' Find the specified component and add it to the selection list
         nbrConnectors = rtAdvancedRouteSelector.Find("connector (3pin) female-1", swRoutingSearchType_e.swRoutingComponentSearch, True, False)
         Debug.Print("Number of instances of the specified component in this assembly: " & nbrConnectors)

         ' Get the number of components attached to the selected component
         Debug.Print("Number of components attached to the specified connector: " & rtAdvancedRouteSelector.getAttachedComponentsCount(0))

         ' Color the selection gray
         rtAdvancedRouteSelector.SetSelectionColor(True, 0)

         ' Select the component and return an array of its attached components
         attachNames = rtAdvancedRouteSelector.Select(0, False, Nothing, swAdvancedRouteSelectionOutput_e.swBoth, selName)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
