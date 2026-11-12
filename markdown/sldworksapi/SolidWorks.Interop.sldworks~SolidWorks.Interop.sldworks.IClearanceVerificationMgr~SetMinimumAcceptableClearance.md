---
title: "SetMinimumAcceptableClearance Method (IClearanceVerificationMgr)"
project: "SOLIDWORKS API Help"
interface: "IClearanceVerificationMgr"
member: "SetMinimumAcceptableClearance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~SetMinimumAcceptableClearance.html"
---

# SetMinimumAcceptableClearance Method (IClearanceVerificationMgr)

Sets the minimum acceptable clearance value.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMinimumAcceptableClearance( _
   ByVal Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IClearanceVerificationMgr
Dim Value As System.Double
Dim value As System.Boolean

value = instance.SetMinimumAcceptableClearance(Value)
```

### C#

```csharp
System.bool SetMinimumAcceptableClearance(
   System.double Value
)
```

### C++/CLI

```cpp
System.bool SetMinimumAcceptableClearance(
   System.double Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: Minimum acceptable clearance value

### Return Value

True if minimum acceptable clearance value successfuly set, false if not

## VBA Syntax

See [ClearanceVerificationMgr::SetMinimumAcceptableClearance](ms-its:sldworksapivb6.chm::/sldworks~ClearanceVerificationMgr~SetMinimumAcceptableClearance.html).

## Examples

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html) examples.

## See Also

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html)
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.html)
[IClearanceVerificationMgr::IgnoreClearanceEqualToSpecifiedValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~IgnoreClearanceEqualToSpecifiedValue.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
