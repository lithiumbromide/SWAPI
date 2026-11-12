---
title: "Get Transform of Coordinate System Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Transform_of_Coordinate_System_Example_VB.NET.htm"
---

# Get Transform of Coordinate System Example (VB.NET)

This example shows how to get the transform of a coordinate system.

NOTE: Because VB.NET does not directly support VARIANTs, you must cast the returned objects to the appropriate data types.

```vb
'-------------------------------------
Private Sub API_Test2()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.feature
    Dim vXformArr() As Double
    Dim vXform As Object
    Dim sAxisName As String
    Dim bRet As Boolean

    swApp = CType(CreateObject("SldWorks.Application"), SldWorks.SldWorks)
    swModel = swApp.IActiveDoc2
    swSelMgr = swModel.ISelectionManager
    swFeat = CType(swSelMgr.GetSelectedObject6(1, 0), SldWorks.feature)
    System.Diagnostics.Debug.WriteLine("File = " & swModel.GetPathName)
    System.Diagnostics.Debug.WriteLine("  Current coordinate system = " & swModel.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swFileSaveAsCoordinateSystem))
    System.Diagnostics.Debug.WriteLine("")
    sAxisName = swFeat.Name
    vXformArr = CType(swModel.GetCoordinateSystemXformByName(sAxisName), Double())
    System.Diagnostics.Debug.WriteLine("  " & sAxisName)
    For Each vXform In vXformArr
    Next
    System.Diagnostics.Debug.WriteLine("    Origin = (" + _
                        Str(-1.0# * vXformArr(9) * 1000.0#) + "," + _
                        Str(-1.0# * vXformArr(10) * 1000.0#) + "," + _
                        Str(-1.0# * vXformArr(11) * 1000.0#) + _
                        ") mm")
End Sub
'-------------------------------------
```
