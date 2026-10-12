---
title: "CalculateClearances Method (IClearanceVerificationMgr)"
project: "SOLIDWORKS API Help"
interface: "IClearanceVerificationMgr"
member: "CalculateClearances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~CalculateClearances.html"
---

# CalculateClearances Method (IClearanceVerificationMgr)

Runs a clearance check of selected assembly components and/or faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function CalculateClearances() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IClearanceVerificationMgr
Dim value As System.Object

value = instance.CalculateClearances()
```

### C#

```csharp
System.object CalculateClearances()
```

### C++/CLI

```cpp
System.Object^ CalculateClearances();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IClearanceResult](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult.html)s

## VBA Syntax

See [ClearanceVerificationMgr::CalculateClearances](ms-its:sldworksapivb6.chm::/sldworks~ClearanceVerificationMgr~CalculateClearances.html).

## Examples

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html) examples.

## See Also

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html)
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
