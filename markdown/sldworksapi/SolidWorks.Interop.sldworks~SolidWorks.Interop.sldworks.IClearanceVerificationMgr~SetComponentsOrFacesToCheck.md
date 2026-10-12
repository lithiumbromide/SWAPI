---
title: "SetComponentsOrFacesToCheck Method (IClearanceVerificationMgr)"
project: "SOLIDWORKS API Help"
interface: "IClearanceVerificationMgr"
member: "SetComponentsOrFacesToCheck"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~SetComponentsOrFacesToCheck.html"
---

# SetComponentsOrFacesToCheck Method (IClearanceVerificationMgr)

Sets the components or faces for which to check clearances.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComponentsOrFacesToCheck( _
   ByVal Components As System.Object, _
   ByVal Faces As System.Object, _
   ByRef Errors As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IClearanceVerificationMgr
Dim Components As System.Object
Dim Faces As System.Object
Dim Errors As System.Integer
Dim value As System.Boolean

value = instance.SetComponentsOrFacesToCheck(Components, Faces, Errors)
```

### C#

```csharp
System.bool SetComponentsOrFacesToCheck(
   System.object Components,
   System.object Faces,
   out System.int Errors
)
```

### C++/CLI

```cpp
System.bool SetComponentsOrFacesToCheck(
   System.Object^ Components,
   System.Object^ Faces,
   [Out] System.int Errors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Components`: Array of [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)s
- `Faces`: Array of [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s
- `Errors`: Error code as defined by [swClearanceVerificationSetEntityErrors_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swClearanceVerificationSetEntityErrors_e.html)

### Return Value

True if components and/or faces successfully set, false if not

## VBA Syntax

See [ClearanceVerificationMgr::SetComponentsOrFacesToCheck](ms-its:sldworksapivb6.chm::/sldworks~ClearanceVerificationMgr~SetComponentsOrFacesToCheck.html).

## Examples

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html) examples.

## See Also

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html)
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
