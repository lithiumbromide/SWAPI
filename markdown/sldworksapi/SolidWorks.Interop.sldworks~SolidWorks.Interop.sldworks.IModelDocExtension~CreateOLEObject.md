---
title: "CreateOLEObject Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CreateOLEObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject.html"
---

# CreateOLEObject Method (IModelDocExtension)

Creates an OLE object on the active document.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateOLEObject( _
   ByVal Aspect As System.Integer, _
   ByVal Position As System.Object, _
   ByVal Buffer As System.Object, _
   ByRef ErrorCode As System.Integer _
) As SwOLEObject
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Aspect As System.Integer
Dim Position As System.Object
Dim Buffer As System.Object
Dim ErrorCode As System.Integer
Dim value As SwOLEObject

value = instance.CreateOLEObject(Aspect, Position, Buffer, ErrorCode)
```

### C#

```csharp
SwOLEObject CreateOLEObject(
   System.int Aspect,
   System.object Position,
   System.object Buffer,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
SwOLEObject^ CreateOLEObject(
   System.int Aspect,
   System.Object^ Position,
   System.Object^ Buffer,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Aspect`: Viewing aspect of the OLE object as defined in the DVASPECT enumeration (see **Remarks**)
- `Position`: Top-left and bottom-right positions (see Remarks)
- `Buffer`: Data for the OLE object (see Remarks)
- `ErrorCode`: 0 if True or 1 if false

### Return Value

[OLE object](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject.html)

## VBA Syntax

See [ModelDocExtension::CreateOLEObject](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CreateOLEObject.html).

## Remarks

| Argument | Information |
| --- | --- |
| Aspect | Uses the DVASPECT enumeration, which has the following values: DVASPECT_CONTENT = 1 DVASPECT_THUMBNAIL = 2 DVASPECT_ICON = 4 DVASPECT_DOCPRINT = 8 See the MSDN documentation for details about the DVASPECT enumeration. |
| Position | Specify: Sheet coordinates for drawings. Screen pixel coordinates for parts and assemblies. |
| Buffer | See ISwOLEObject::Buffer or specify ISwOLEObject::IGetBuffer - or - Get the data from your own OLE object. The data is in the format obtained from the Microsoft MFC object COleClientItem using the GetHGlobalFromILockBytes. |

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetOLEObjectCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjectCount.html)
[IModelDocExtension::GetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects.html)
[IModelDocExtension::InsertObjectFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertObjectFromFile.html)
[IModelDocExtension::ICreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject.html)
[IModelDocExtension::IGetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
