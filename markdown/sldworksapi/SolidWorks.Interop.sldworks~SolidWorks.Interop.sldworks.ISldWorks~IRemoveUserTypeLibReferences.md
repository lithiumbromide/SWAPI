---
title: "IRemoveUserTypeLibReferences Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IRemoveUserTypeLibReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IRemoveUserTypeLibReferences.html"
---

# IRemoveUserTypeLibReferences Method (ISldWorks)

Removes the user-specified type library references.

## Syntax

### Visual Basic (Declaration)

```vb
Function IRemoveUserTypeLibReferences( _
   ByVal NCount As System.Integer, _
   ByRef BstrTlbRef As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim NCount As System.Integer
Dim BstrTlbRef As System.String
Dim value As System.Boolean

value = instance.IRemoveUserTypeLibReferences(NCount, BstrTlbRef)
```

### C#

```csharp
System.bool IRemoveUserTypeLibReferences(
   System.int NCount,
   ref System.string BstrTlbRef
)
```

### C++/CLI

```cpp
System.bool IRemoveUserTypeLibReferences(
   System.int NCount,
   System.String^% BstrTlbRef
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCount`: Number of user-specified type library references
- `BstrTlbRef`: Array of strings of the user-specified type library references

### Return Value

True if the user-specified type library references are removed, false if not

## VBA Syntax

See [SldWorks::IRemoveUserTypeLibReferences](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IRemoveUserTypeLibReferences.html).

## Remarks

Before calling this method, call [ISldWorks::GetUserTypeLibReferenceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserTypeLibReferenceCount.html) to get the value for NCount.

Any macro recorded after this method is called will not have references to the removed user-specified type libraries.

An add-in can use this method to remove its type library references when the add-in is unloaded.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IGetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserTypeLibReferences.html)
[ISldWorks::ISetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences.html)
[ISldWorks::RemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences.html)
[ISldWorks::UserTypeLibReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
