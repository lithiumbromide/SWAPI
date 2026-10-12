---
title: "IGetSheetMetalObjectsByPersistReference Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetSheetMetalObjectsByPersistReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSheetMetalObjectsByPersistReference.html"
---

# IGetSheetMetalObjectsByPersistReference Method (IModelDocExtension)

Gets the object, or objects, in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSheetMetalObjectsByPersistReference( _
   ByVal Count As System.Integer, _
   ByRef PersistId As System.Byte, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Count As System.Integer
Dim PersistId As System.Byte
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.IGetSheetMetalObjectsByPersistReference(Count, PersistId, ErrorCode)
```

### C#

```csharp
System.object IGetSheetMetalObjectsByPersistReference(
   System.int Count,
   ref System.byte PersistId,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ IGetSheetMetalObjectsByPersistReference(
   System.int Count,
   System.byte% PersistId,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of persistent reference IDs
- `PersistId`: Persistent reference IDs returned by [IModelDocExtension::GetFlattenSheetMetalPersistReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetFlattenSheetMetalPersistReference.html) or [IModelDocExtension::IGetFlattenSheetMetalPersistReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetFlattenSheetMetalPersistReference.html)
- `ErrorCode`: Error as defined by [swPersistReferencedObjectStates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPersistReferencedObjectStates_e.html)

### Return Value

- in-process, unmanaged C++: Pointer to an array of objects in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [ModelDocExtension::IGetSheetMetalObjectsByPersistReference](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IGetSheetMetalObjectsByPersistReference.html).

## Remarks

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetSheetMetalObjectsByPersistReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSheetMetalObjectsByPersistReference.html)
[IModelDocExtension::GetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.html)
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.html)
[IModelDocExtension::GetPersistReferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.html)
[IModelDocExtension::IGetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.html)
[IModelDocExtension::IGetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
