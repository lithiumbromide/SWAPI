---
title: "IGetFlattenSheetMetalPersistReference Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetFlattenSheetMetalPersistReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetFlattenSheetMetalPersistReference.html"
---

# IGetFlattenSheetMetalPersistReference Method (IModelDocExtension)

Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFlattenSheetMetalPersistReference( _
   ByVal DispObj As System.Object, _
   ByVal Count As System.Integer _
) As System.Byte
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DispObj As System.Object
Dim Count As System.Integer
Dim value As System.Byte

value = instance.IGetFlattenSheetMetalPersistReference(DispObj, Count)
```

### C#

```csharp
System.byte IGetFlattenSheetMetalPersistReference(
   System.object DispObj,
   System.int Count
)
```

### C++/CLI

```cpp
System.byte IGetFlattenSheetMetalPersistReference(
   System.Object^ DispObj,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DispObj`: Entity (a face, edge, or vertex) in the flattened sheet metal part whose persistent reference IDs you want
- `Count`: Number of persistent reference IDs

### Return Value

- in-process, unmanaged C++: Pointer to a byte array of persistent reference IDs

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [ModelDocExtension::IGetFlattenSheetMetalPersistReference](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IGetFlattenSheetMetalPersistReference.html).

## Remarks

The sheet metal part must be in the flattened state when this method is called. You can pass the byte array of persistent reference IDs to [IModelDocExtension::GetSheetMetalObjectsByPersistReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetSheetMetalObjectsByPersistReference.html) or [IModelDocExtension::IGetSheetMetalObjectsByPersistReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetSheetMetalObjectsByPersistReference.html), which gets the objects that correspond to the persistent reference IDs in the folded configuration of the sheet metal part.

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetFlattenSheetMetalPersistReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetFlattenSheetMetalPersistReference.html)
[IModelDocExtension::GetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.html)
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.html)
[IModelDocExtension::GetPersistReferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount.html)
[IModelDocExtension::IGetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.html)
[IModelDocExtension::IGetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
