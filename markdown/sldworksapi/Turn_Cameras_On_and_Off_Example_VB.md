---
title: "Turn Cameras On and Off Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Turn_Cameras_On_and_Off_Example_VB.htm"
---

# Turn Cameras On and Off Example (VBA)

This example shows how to turn cameras on and off.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a SOLIDWORKS Design model that contains at least one camera.
 '
 ' Postconditions: The cameras are turned on and off.
 '----------------------------------------------------------------------------
Option Explicit
' Utility struct to combine the name and ID of a camera
 Type Camera_t
     Name As String
     Id   As Long
 End Type
Dim swApp As SldWorks.SldWorks
Sub main()
    Dim swModel                 As SldWorks.ModelDoc2
     Dim swModelView             As SldWorks.ModelView
     Dim swCamera                As SldWorks.Camera
     Dim lNumCameras             As Long
     Dim lCameraId               As Long
     Dim swFeature               As SldWorks.Feature
     Dim aCameras()              As Camera_t
     Dim bValue                  As Boolean
     Dim sFeatureName            As String
     Dim lTypeOfCamera           As Long
     Dim lTypeOfCameraPosition   As Long
    ' Connect to SOLIDWORKS
     Set swApp = Application.SldWorks

    ' Get active document
     Set swModel = swApp.ActiveDoc

    ' Get the active model view for the active document
     Set swModelView = swModel.ActiveView

    ' Check if a camera view is active
     Set swCamera = swModelView.Camera
    Debug.Print
    If (swCamera Is Nothing) Then
         Debug.Print "No active camera."
     Else
         Debug.Print "Camera is active."
         Debug.Print "  Name = " & swCamera.Id
     End If
    ' Turn off camera view
     swModelView.Camera = Nothing
    ' Get the number of cameras
     lNumCameras = swModel.Extension.GetCameraCount
    Debug.Print
     Debug.Print "Number of cameras = " & lNumCameras
    ReDim aCameras(lNumCameras - 1)
    For lCameraId = 0 To (lNumCameras - 1)
        ' Valid ID:
         '  0 <= ID <= (ModelDocExtension::GetCameraCount - 1)
         ' IDs are reassigned if a camera is deleted
         aCameras(lCameraId).Id = lCameraId
        ' Get the camera
         Set swCamera = swModel.Extension.GetCameraById(lCameraId)
        ' A camera is a feature
         Set swFeature = swCamera
       ' Get the names of the feature and camera
         sFeatureName = swFeature.Name
        aCameras(lCameraId).Name = sFeatureName
        Debug.Print
         Debug.Print "Type of feature = "; swFeature.GetTypeName
         Debug.Print "Camera name = " & sFeatureName
        ' Get the type of camera
        lTypeOfCamera = swCamera.Type
        If (lTypeOfCamera = 1) Then
             Debug.Print "Type of camera = Aimed at target"
         Else
             Debug.Print "Type of camera = Floating"
         End If
        ' Get the type of camera position
         lTypeOfCameraPosition = swCamera.PositionType
        If (lTypeOfCameraPosition = 1) Then
             Debug.Print "Type of camera position = Cartesian"
         Else
             Debug.Print "Type of camera position = Spherical"
         End If
    Next lCameraId
    ' Now switch the view to each camera
     For lCameraId = 0 To (lNumCameras - 1)
        bValue = swModelView.SetCameraByName(aCameras(lCameraId).Name)
        If (bValue = False) Then
             Debug.Print "Failed to set model view to use camera " & aCameras(lCameraId).Name
         Else
             Debug.Print "Model view set to use camera " & aCameras(lCameraId).Name
         End If
        swModelView.Camera = Nothing
    Next lCameraId
End Sub
```
