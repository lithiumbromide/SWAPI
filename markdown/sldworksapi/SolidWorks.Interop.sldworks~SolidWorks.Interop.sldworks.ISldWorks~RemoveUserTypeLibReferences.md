---
title: "RemoveUserTypeLibReferences Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveUserTypeLibReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences.html"
---

# RemoveUserTypeLibReferences Method (ISldWorks)

Removes the user-specified type library references.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveUserTypeLibReferences( _
   ByVal VTlbRef As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim VTlbRef As System.Object
Dim value As System.Boolean

value = instance.RemoveUserTypeLibReferences(VTlbRef)
```

### C#

```csharp
System.bool RemoveUserTypeLibReferences(
   System.object VTlbRef
)
```

### C++/CLI

```cpp
System.bool RemoveUserTypeLibReferences(
   System.Object^ VTlbRef
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VTlbRef`: Array of strings of the user-specified type library references

### Return Value

True if the user-specified type library references are removed, false if not

## VBA Syntax

See [SldWorks::RemoveUserTypeLibReferences](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveUserTypeLibReferences.html).

## Remarks

Any macro recorded after this method is called will not have references to the removed user-specified type libraries.

An add-in can use this method to remove its type library references when the add-in is unloaded.

See [Type Libraries](sldworksAPIProgGuide.chm::/OVERVIEW/Type_Libraries.htm) for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetUserTypeLibReferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserTypeLibReferenceCount.html)
[ISldWorks::IGetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserTypeLibReferences.html)
[ISldWorks::IRemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IRemoveUserTypeLibReferences.html)
[ISldWorks::ISetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences.html)
[ISldWorks::UserTypeLibReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
