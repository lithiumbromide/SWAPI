---
title: "IsSamePersistentID Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IsSamePersistentID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsSamePersistentID.html"
---

# IsSamePersistentID Method (IModelDocExtension)

Gets whether the two specified objects have the same persistent reference IDs.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSamePersistentID( _
   ByVal PersistentID1 As System.Object, _
   ByVal PersistentID2 As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PersistentID1 As System.Object
Dim PersistentID2 As System.Object
Dim value As System.Integer

value = instance.IsSamePersistentID(PersistentID1, PersistentID2)
```

### C#

```csharp
System.int IsSamePersistentID(
   System.object PersistentID1,
   System.object PersistentID2
)
```

### C++/CLI

```cpp
System.int IsSamePersistentID(
   System.Object^ PersistentID1,
   System.Object^ PersistentID2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PersistentID1`: Object
- `PersistentID2`: Object

### Return Value

Object equality as defined by [swObjectEquality](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swObjectEquality.html)

## VBA Syntax

See [ModelDocExtension::IsSamePersistentID](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IsSamePersistentID.html).

## Examples

[Compare Selected Objects and Their Persistent Reference IDs (VB.NET)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_VBNET.htm)
[Compare Selected Objects and Their Persistent Reference IDs (VBA)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_VB.htm)
[Compare Selected Objects and Their Persistent Reference IDs (C#)](Compare_Selected_Objects_and_Their_Persistent_Reference_IDs_Example_CSharp.htm)

## Remarks

Use this method when your application is passed two entities that your application did not select, and your application needs to know if they are the same entity.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectByPersistReference3.html)
[IModelDocExtension::GetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReference3.html)
[IModelDocExtension::GetPersistReferenceCount3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.html)
[IModelDocExtension::IGetPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetPersistReference3.html)
[IModelDocExtension::IGetObjectByPersistReference3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.html)
[ISldWorks::IsSame Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsSame.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
