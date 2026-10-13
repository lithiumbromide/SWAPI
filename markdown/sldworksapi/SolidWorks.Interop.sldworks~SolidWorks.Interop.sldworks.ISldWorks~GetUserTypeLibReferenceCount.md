---
title: "GetUserTypeLibReferenceCount Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetUserTypeLibReferenceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserTypeLibReferenceCount.html"
---

# GetUserTypeLibReferenceCount Method (ISldWorks)

Gets the number of user-specified type library references.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserTypeLibReferenceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

value = instance.GetUserTypeLibReferenceCount()
```

### C#

```csharp
System.int GetUserTypeLibReferenceCount()
```

### C++/CLI

```cpp
System.int GetUserTypeLibReferenceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of user-specified type library references

## VBA Syntax

See [SldWorks::GetUserTypeLibReferenceCount](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetUserTypeLibReferenceCount.html).

## Remarks

Call this method before calling [ISldWorks::IGetUserTypeLibReferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetUserTypeLibReferences.html) to get the size of the array for that method.

See [Type Libraries](sldworksAPIProgGuide.chm::/OVERVIEW/Type_Libraries.htm) for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::UserTypeLibReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences.html)
[ISldWorks::ISetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences.html)
[ISldWorks::RemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences.html)
[ISldWorks::IRemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IRemoveUserTypeLibReferences.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number
