---
title: "GetPersistReferenceCount3 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetPersistReferenceCount3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPersistReferenceCount3.html"
---

# GetPersistReferenceCount3 Method (IModelDocExtension)

Gets the size of the persistent reference ID assigned to the selected object in this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPersistReferenceCount3( _
   ByVal DispObj As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DispObj As System.Object
Dim value As System.Integer

value = instance.GetPersistReferenceCount3(DispObj)
```

### C#

```csharp
System.int GetPersistReferenceCount3(
   System.object DispObj
)
```

### C++/CLI

```cpp
System.int GetPersistReferenceCount3(
   System.Object^ DispObj
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DispObj`: Selected object

### Return Value

Size of that object's persistent reference ID

## VBA Syntax

See [ModelDocExtension::GetPersistReferenceCount3](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetPersistReferenceCount3.html).

## Examples

[Get Object's Persistent Reference ID (C++)](Get_Object_s_Persistent_Reference_ID_Example_CPlusPlus_COM.htm)

## Remarks

Persistent reference ID values obtained using the now obsolete IModelDocExtension::GetPersistReference and its related obsolete methods, IModelDocExtension::GetPersistReferenceCount and IModelDocExtension::GetObjectByPersistReference2, are not compatible with persistent reference IDs obtained using [IModelDocExtension::GetPersistReference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetPersistReference3.html) or [IModelDocExtension::IGetPersistReference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetPersistReference3.html) and its related methods, [IModelDocExtension::GetObjectByPersistReference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.html) or [IModelDocExtension::IGetObjectByPersistReference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetObjectByPersistReference3.html) and this method.

**IMPORTANT:** SOLIDWORKS recommends not using this method with IModelDocExtension::IGetPersistReference3 because when these methods are used together, you will experience a significant decrease in performance.

See [Persistent Reference IDs](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm) for more information.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2007 SP3, Revision Number 15.3
