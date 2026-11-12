---
title: "ICreateOLEObject Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ICreateOLEObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ICreateOLEObject.html"
---

# ICreateOLEObject Method (IModelDocExtension)

Creates an OLE object on the active document.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateOLEObject( _
   ByVal Aspect As System.Integer, _
   ByRef Position As System.Double, _
   ByVal ByteCount As System.Integer, _
   ByRef Buffer As System.Byte, _
   ByRef ErrorCode As System.Integer _
) As SwOLEObject
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Aspect As System.Integer
Dim Position As System.Double
Dim ByteCount As System.Integer
Dim Buffer As System.Byte
Dim ErrorCode As System.Integer
Dim value As SwOLEObject

value = instance.ICreateOLEObject(Aspect, Position, ByteCount, Buffer, ErrorCode)
```

### C#

```csharp
SwOLEObject ICreateOLEObject(
   System.int Aspect,
   ref System.double Position,
   System.int ByteCount,
   ref System.byte Buffer,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
SwOLEObject^ ICreateOLEObject(
   System.int Aspect,
   System.double% Position,
   System.int ByteCount,
   System.byte% Buffer,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Aspect`: Viewing aspect of the OLE object as defined in the DVASPECT enumeration (see **Remarks**)
- `Position`: Top-left and bottom-right positions (see Remarks)
- `ByteCount`: Number of bytes
- `Buffer`: Data for the OLE object (see Remarks)
- `ErrorCode`: 0 if True or 1 if false

### Return Value

[OLE object](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISwOLEObject.html)

## VBA Syntax

See [ModelDocExtension::ICreateOLEObject](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ICreateOLEObject.html).

## Remarks

| Argument | Information |
| --- | --- |
| Aspect | Uses the DVASPECT enumeration, which has the following values: DVASPECT_CONTENT = 1 DVASPECT_THUMBNAIL = 2 DVASPECT_ICON = 4 DVASPECT_DOCPRINT = 8 See the MSDN documentation for details about the DVASPECT enumeration. |
| Position | Specify: Sheet coordinates for drawings. Screen pixel coordinates for parts and assemblies. |
| Buffer | See ISwOLEObject::Buffer or specify ISwOLEObject::IGetBuffer - or - Get the data from your own OLE object. The data is in the format obtained from the Microsoft MFC object COleClientItem using the GetHGlobalFromILockBytes. |

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateOLEObject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateOLEObject.html)
[IModelDocExtension::GetOLEObjectCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjectCount.html)
[IModelDocExtension::GetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects.html)
[IModelDocExtension::IGetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects.html)
[IModelDocExtension::InsertObjectFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertObjectFromFile.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
