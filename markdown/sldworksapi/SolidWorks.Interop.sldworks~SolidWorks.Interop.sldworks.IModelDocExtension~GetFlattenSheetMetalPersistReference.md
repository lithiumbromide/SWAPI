---
title: "GetFlattenSheetMetalPersistReference Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetFlattenSheetMetalPersistReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetFlattenSheetMetalPersistReference.html"
---

# GetFlattenSheetMetalPersistReference Method (IModelDocExtension)

Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFlattenSheetMetalPersistReference( _
   ByVal DispObj As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DispObj As System.Object
Dim value As System.Object

value = instance.GetFlattenSheetMetalPersistReference(DispObj)
```

### C#

```csharp
System.object GetFlattenSheetMetalPersistReference(
   System.object DispObj
)
```

### C++/CLI

```cpp
System.Object^ GetFlattenSheetMetalPersistReference(
   System.Object^ DispObj
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DispObj`: Entity (a face, edge, or vertex) in the flattened sheet metal part whose persistent reference IDs you want

### Return Value

Byte array of persistent reference IDs

## VBA Syntax

See [ModelDocExtension::GetFlattenSheetMetalPersistReference](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetFlattenSheetMetalPersistReference.html).

## Examples

[Set and Get Sheet Metal Part's Persistent Reference IDs (C#)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_CSharp.htm)
[Set and Get Sheet Metal Part's Persistent Reference IDs (VB.NET)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VBNET.htm)
[Set and Get Sheet Metal Part's Persistent Reference IDs (VBA)](Set_and_Get_Sheet_Metal_Part's_Persistent_Reference_IDs_Example_VB.htm)

## Remarks

The sheet metal part must be in the flattened state when this method is called. You can then pass the byte array of persistent reference IDs to [IModelDocExtension::GetSheetMetalObjectsByPersistReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetSheetMetalObjectsByPersistReference.html) or [IModelDocExtension::IGetSheetMetalObjectsByPersistReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetSheetMetalObjectsByPersistReference.html), which gets the objects that correspond to the persistent reference IDs in the folded configuration of the sheet metal part.

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.html)
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.html)
[IModelDocExtension::GetPersistReferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.html)
[IModelDocExtension::IGetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.html)
[IModelDocExtension::IGetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
