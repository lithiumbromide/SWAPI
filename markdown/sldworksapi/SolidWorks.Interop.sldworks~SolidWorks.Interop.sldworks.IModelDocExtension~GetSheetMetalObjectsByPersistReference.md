---
title: "GetSheetMetalObjectsByPersistReference Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetSheetMetalObjectsByPersistReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSheetMetalObjectsByPersistReference.html"
---

# GetSheetMetalObjectsByPersistReference Method (IModelDocExtension)

Gets the objects in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetMetalObjectsByPersistReference( _
   ByVal PersistId As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PersistId As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetSheetMetalObjectsByPersistReference(PersistId, ErrorCode)
```

### C#

```csharp
System.object GetSheetMetalObjectsByPersistReference(
   System.object PersistId,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetSheetMetalObjectsByPersistReference(
   System.Object^ PersistId,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PersistId`: Persistent reference IDs returned by [IModelDocExtension::GetFlattenSheetMetalPersistReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetFlattenSheetMetalPersistReference.html) or [IModelDocExtension::IGetFlattenSheetMetalPersistReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetFlattenSheetMetalPersistReference.html)
- `ErrorCode`: Error as defined by [swPersistReferencedObjectStates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPersistReferencedObjectStates_e.html)

### Return Value

Objects in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part

## VBA Syntax

See [ModelDocExtension::GetSheetMetalObjectsByPersistReference](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetSheetMetalObjectsByPersistReference.html).

## Examples

[Set and Get Sheet Metal Part's Persistent Reference IDs (C#)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_CSharp.htm)
[Set and Get Sheet Metal Part's Persistent Reference IDS (VB.NET)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VBNET.htm)
[Set and Get Sheet Metal Part's Persistent Reference IDs (VBA)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VB.htm)

## Remarks

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IGetSheetMetalObjectsByPersistReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetSheetMetalObjectsByPersistReference.html)
[IModelDocExtension::GetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.html)
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.html)
[IModelDocExtension::GetPersistReferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.html)
[IModelDocExtension::IGetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.html)
[IModelDocExtension::IGetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
