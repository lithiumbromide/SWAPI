---
title: "IGetPersistReference3 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetPersistReference3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.html"
---

# IGetPersistReference3 Method (IModelDocExtension)

Gets the persistent reference ID for the specified object in this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPersistReference3( _
   ByVal DipsObj As System.Object, _
   ByVal Count As System.Integer _
) As System.Byte
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DipsObj As System.Object
Dim Count As System.Integer
Dim value As System.Byte

value = instance.IGetPersistReference3(DipsObj, Count)
```

### C#

```csharp
System.byte IGetPersistReference3(
   System.object DipsObj,
   System.int Count
)
```

### C++/CLI

```cpp
System.byte IGetPersistReference3(
   System.Object^ DipsObj,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DipsObj`: Object
- `Count`: Size of returned array assigned to that object (see [Remarks](#Remarks))

### Return Value

Array containing the persistent reference ID assigned to that object

## VBA Syntax

See [ModelDocExtension::IGetPersistReference3](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IGetPersistReference3.html).

## Examples

[Get Object's Persistent Reference ID (C++)](Get_Object_s_Persistent_Reference_ID_Example_CPlusPlus_COM.htm)

## Remarks

Persistent reference ID values obtained using the now obsolete IModelDocExtension::GetPersistReference and its related obsolete methods, IModelDocExtension::GetPersistReferenceCount and IModelDocExtension::GetObjectByPersistReference2, are not compatible with persistent reference IDs obtained using this method and its related methods, [IModelDocExtension::GetPersistReferenceCount3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.html) and [IModelDocExtension::GetObjectByPersistReference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.html) or [IModelDocExtension::IGetObjectByPersistReference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.html).

**IMPORTANT:** SOLIDWORKS recommends not using IModelDocExtension::IGetPersistReference3 with ModelDocExtension::GetPersistReferenceCount3 because when ModelDocExtension::GetPersistReferenceCount3 is used with ModelDocExtension::IGetPersistReference3, you will experience a significant decrease in performance. Instead, use [IModelDocExtension::GetPersistReference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetPersistReference3.html).

A persistent reference ID is related to a model. It is portable and can be saved within the model or in other places. Some persistent reference IDs are general to all models and can be instantiated from all models. Your application must handle persistent reference IDs and their relationships among models.

The internal representations of the return value array may change, possibly from rebuild to rebuild, or more likely, from one release of SOLIDWORKS to the next, but their usage in finding the correct entity will be consistent across rebuilds and SOLIDWORKS releases.

To compare the referenced entities, you could use the Visual Basic Is operator to find out if the entities are the same.

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IsSamePersistentID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsSamePersistentID.html)

## Availability

SOLIDWORKS 2007 SP3, Revision Number 15.3
