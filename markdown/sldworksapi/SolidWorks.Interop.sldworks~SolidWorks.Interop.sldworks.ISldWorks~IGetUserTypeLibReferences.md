---
title: "IGetUserTypeLibReferences Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetUserTypeLibReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserTypeLibReferences.html"
---

# IGetUserTypeLibReferences Method (ISldWorks)

Gets the specified user-specified type library references.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetUserTypeLibReferences( _
   ByVal NCount As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim NCount As System.Integer
Dim value As System.String

value = instance.IGetUserTypeLibReferences(NCount)
```

### C#

```csharp
System.string IGetUserTypeLibReferences(
   System.int NCount
)
```

### C++/CLI

```cpp
System.String^ IGetUserTypeLibReferences(
   System.int NCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCount`: Number of user-specified type libraries

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings for the user-specified type library references.

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISldWorks::GetUserTypeLibReferenceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserTypeLibReferenceCount.html) to get the value for NCount.

See [Type Libraries](sldworksAPIProgGuide.chm::/OVERVIEW/Type_Libraries.htm) for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::ISetUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetUserTypeLibReferences.html)
[ISldWorks::RemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveUserTypeLibReferences.html)
[ISldWorks::UserTypeLibReferences Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserTypeLibReferences.html)
[ISldWorks::IRemoveUserTypeLibReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IRemoveUserTypeLibReferences.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
