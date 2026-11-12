---
title: "InsertPicture Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertPicture"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPicture.html"
---

# InsertPicture Method (ISketchManager)

Inserts a raster Referenced image.

## Syntax

### Visual Basic

```vb
Function InsertPicture( _
   ByVal PathName As System.String, _
   ByVal InsertX As System.Double, _
   ByVal InsertY As System.Double, _
   ByVal InsertZ As System.Double, _
   ByVal Scale As System.Double, _
   ByVal Rotation As System.Double _
) As ReferenceImage
```

### C#

```csharp
ReferenceImage InsertPicture(
   System.string PathName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### JScript

```
function InsertPicture(
   PathName : System.String,
   InsertX : System.double,
   InsertY : System.double,
   InsertZ : System.double,
   Scale : System.double,
   Rotation : System.double
) : ReferenceImage;
```

### Managed Extensions for C++

```
ReferenceImage* InsertPicture(
   System.string* PathName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### C++/CLI

```cpp
ReferenceImage^ InsertPicture(
   System.String^ PathName,
   System.double InsertX,
   System.double InsertY,
   System.double InsertZ,
   System.double Scale,
   System.double Rotation
)
```

### Parameters

- `PathName`: Path and file name of the Referenced image to insert
- `InsertX`: x coordinate where to insert the Referenced image
- `InsertY`: y coordinate where to insert the Referenced image
- `InsertZ`: z coordinate where to insert the Referenced image
- `Scale`: Scale factor for each axis
- `Rotation`: Angle by which to rotate the Referenced image (see **Remarks**)

### Return Value

[Referenced image](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)

## Examples

This code snippet shows how to insert a Referenced image.

##### COM native C++

bstr_t imageFileName ( L"<`path_and file_name_of_image`>" );

double insertX = 0, insertY = 0, insertZ = 0, scale = 1, rotation = 0;

ReferenceImagePtr imageEntity = sketchMgr->InsertPicture( imageFileName, insertX, insertY, insertZ, scale, rotation );

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)
[Insert Picture (C#)](Insert_Picture_Example_CSharp.htm)
[Insert Picture (VB.NET)](Insert_Picture_Example_VBNET.htm)
[Insert Picture (VBA)](Insert_Picture_Example_VBA.htm)

## Remarks

Use a positive value for Rotation to rotate the Referenced image counterclockwise and a negative value to rotate the Referenced image clockwise.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::DetachReferenceImage Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~DetachReferenceImage.html)
[IReferenceImage::Reload Method ()](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~Reload.html)
[IReferenceImage::Unload Method ()](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~Unload.html)

## Availability

DraftSight V1R1
