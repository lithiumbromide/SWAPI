---
title: "UserTypeLibReferences Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "UserTypeLibReferences"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences.html"
---

# UserTypeLibReferences Property (ISldWorks)

Gets and sets the user-specified type library references.

## Syntax

### Visual Basic (Declaration)

```vb
Property UserTypeLibReferences As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Object

instance.UserTypeLibReferences = value

value = instance.UserTypeLibReferences
```

### C#

```csharp
System.object UserTypeLibReferences {get; set;}
```

### C++/CLI

```cpp
property System.Object^ UserTypeLibReferences {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of the user-specified type library references

## VBA Syntax

See [SldWorks::UserTypeLibReferences](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~UserTypeLibReferences.html).

## Examples

[Add User-specified Type Library Reference (VBA)](Add_User-specified_Type_Library_Reference_Example_VB.htm)

## Remarks

An add-in can use this property to add its type library references after the add-in is loaded.

A user-specified type library first appears on the list of available references only after adding it and only after recording a macro.

User-specified type library references are not persistent across SOLIDWORKS Design sessions.

Only macros created after adding a user-specified type library reference can reference that type library.

See [Type Libraries](sldworksAPIProgGuide.chm::/OVERVIEW/Type_Libraries.htm) for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetUserTypeLibReferenceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserTypeLibReferenceCount.html)
[ISldWorks::IGetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserTypeLibReferences.html)
[ISldWorks::ISetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences.html)
[ISldWorks::RemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
