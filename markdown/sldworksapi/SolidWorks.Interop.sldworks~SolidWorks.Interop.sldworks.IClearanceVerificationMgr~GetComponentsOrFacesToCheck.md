---
title: "GetComponentsOrFacesToCheck Method (IClearanceVerificationMgr)"
project: "SOLIDWORKS API Help"
interface: "IClearanceVerificationMgr"
member: "GetComponentsOrFacesToCheck"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~GetComponentsOrFacesToCheck.html"
---

# GetComponentsOrFacesToCheck Method (IClearanceVerificationMgr)

Gets the components and/or faces for which to check clearance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentsOrFacesToCheck() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IClearanceVerificationMgr
Dim value As System.Object

value = instance.GetComponentsOrFacesToCheck()
```

### C#

```csharp
System.object GetComponentsOrFacesToCheck()
```

### C++/CLI

```cpp
System.Object^ GetComponentsOrFacesToCheck();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)s and/or [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s

## VBA Syntax

See [ClearanceVerificationMgr::GetComponentsOrFacesToCheck](ms-its:sldworksapivb6.chm::/sldworks~ClearanceVerificationMgr~GetComponentsOrFacesToCheck.html).

## Examples

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html) examples.

## See Also

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html)
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
