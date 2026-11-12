---
title: "IReferenceImage Interface"
project: ""
interface: "IReferenceImage"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html"
---

# IReferenceImage Interface

Allows access to a raster Referenced image.

## Syntax

### Visual Basic

```vb
Public Interface IReferenceImage
```

### C#

```csharp
public interface IReferenceImage
```

### JScript

```
public interface IReferenceImage
```

### Managed Extensions for C++

```
public __gc __interface IReferenceImage
```

### C++/CLI

```cpp
public interface class IReferenceImage
```

## Examples

This code snippet shows how to get the Referenced image, if the selected object is an IReferenceImage object.

##### COM native C++

long selCount = dsSelManager->GetSelectedObjectCount( dsSelectionSetType_Current );

if( selCount > 0 )
{
for( long i = 0; i < selCount; ++i )
{
//Get selected object type
dsObjectType_e retObjType;
IDispatchPtr selObj = dsSelManager->GetSelectedObject( dsSelectionSetType_Current, i, &retObjType );

//If selected object is an image
if( dsReferenceImageType == retObjType )
{

IReferenceImagePtr dsImage( selObj );

. . .

This code snippet shows how to insert a Referenced image.

##### COM native C++

bstr_t imageFileName ( L"<`path_and_file_name_of_image`>" );

double insertX = 0, insertY = 0, insertZ = 0, scale = 1, rotation = 0;

ReferenceImagePtr imageEntity = sketchMgr->InsertPicture( imageFileName, insertX, insertY, insertZ, scale, rotation );

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)
[Insert Picture (C#)](Insert_Picture_Example_CSharp.htm)
[Insert Picture (VB.NET)](Insert_Picture_Example_VBNET.htm)
[Insert Picture (VBA)](Insert_Picture_Example_VBA.htm)

## Accessors

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

[ISketchManager::InsertPicture](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPicture.html)

## Access Diagram

DSObjectModel.pdf#ReferenceImage

[ReferenceImage](DSObjectModel.pdf#ReferenceImage)

## See Also

[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[ISketchManager::DetachReferenceImage Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~DetachReferenceImage.html)
