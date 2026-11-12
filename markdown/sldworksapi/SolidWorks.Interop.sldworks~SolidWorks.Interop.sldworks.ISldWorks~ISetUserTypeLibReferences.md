---
title: "ISetUserTypeLibReferences Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ISetUserTypeLibReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences.html"
---

# ISetUserTypeLibReferences Method (ISldWorks)

Sets the user-specified type library references.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetUserTypeLibReferences( _
   ByVal NCount As System.Integer, _
   ByRef BstrTlbRef As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim NCount As System.Integer
Dim BstrTlbRef As System.String

instance.ISetUserTypeLibReferences(NCount, BstrTlbRef)
```

### C#

```csharp
void ISetUserTypeLibReferences(
   System.int NCount,
   ref System.string BstrTlbRef
)
```

### C++/CLI

```cpp
void ISetUserTypeLibReferences(
   System.int NCount,
   System.String^% BstrTlbRef
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCount`: Number of user-specified type library references
- `BstrTlbRef`: - in-process, unmanaged C++: Pointer to an array of strings of the user-specified type library references

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

- An add-in can use this method to add its type library references after the add-in is loaded.
- A user-specified type library first appears on the list of available references only after adding it and only after recording a macro.
- User-specified type library references are not persistent across SOLIDWORKS Design sessions.
- Only macros created after adding a user-specified type library reference can reference that type library.

See [Type Libraries](sldworksAPIProgGuide.chm::/OVERVIEW/Type_Libraries.htm) for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetUserTypeLibReferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserTypeLibReferenceCount.html)
[ISldWorks::IGetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserTypeLibReferences.html)
[ISldWorks::IRemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IRemoveUserTypeLibReferences.html)
[ISldWorks::RemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences.html)
[ISldWorks::UserTypeLibReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
