---
title: "InsertObjectFromFile Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertObjectFromFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertObjectFromFile.html"
---

# InsertObjectFromFile Method (IModelDocExtension)

Inserts an OLE object from a file.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertObjectFromFile( _
   ByVal FilePath As System.String, _
   ByVal CreateLink As System.Boolean, _
   ByVal Aspect As System.Integer, _
   ByVal XPos As System.Double, _
   ByVal YPos As System.Double, _
   ByVal ZPos As System.Double _
) As SwOLEObject
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim FilePath As System.String
Dim CreateLink As System.Boolean
Dim Aspect As System.Integer
Dim XPos As System.Double
Dim YPos As System.Double
Dim ZPos As System.Double
Dim value As SwOLEObject

value = instance.InsertObjectFromFile(FilePath, CreateLink, Aspect, XPos, YPos, ZPos)
```

### C#

```csharp
SwOLEObject InsertObjectFromFile(
   System.string FilePath,
   System.bool CreateLink,
   System.int Aspect,
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

### C++/CLI

```cpp
SwOLEObject^ InsertObjectFromFile(
   System.String^ FilePath,
   System.bool CreateLink,
   System.int Aspect,
   System.double XPos,
   System.double YPos,
   System.double ZPos
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePath`: Path and filename for the OLE object file
- `CreateLink`: True to create an external link to the OLE object file, false to embed the OLE object on the document
- `Aspect`: Viewing aspect of the object as defined in the DVASPECT enumeration (see **Remarks**)
- `XPos`: x coordinate for the OLE object
- `YPos`: y coordinate for the OLE object
- `ZPos`: z coordinate for the OLE object

### Return Value

Newly inserted [object](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject.html)

## VBA Syntax

See [ModelDocExtension::InsertObjectFromFile](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertObjectFromFile.html).

## Remarks

Currently, only the drawing documents use the x,y,z coordinate position. Part and assembly documents place the inserted object at the upper-right corner of the model view.

The aspect argument uses the DVASPECT enumeration, which has the following values:

- DVASPECT_CONTENT = 1
- DVASPECT_THUMBNAIL = 2
- DVASPECT_ICON = 4
- DVASPECT_DOCPRINT = 8

See the MSDN documentation for additional details about the DVASPECT enumeration.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject.html)
[IModelDocExtension::GetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects.html)
[IModelDocExtension::GetOLEObjectCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjectCount.html)
[IModelDocExtension::ICreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject.html)
[IModelDocExtension::IGetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
