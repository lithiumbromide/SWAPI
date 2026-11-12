---
title: "ClearanceType Property (IClearanceResult)"
project: "SOLIDWORKS API Help"
interface: "IClearanceResult"
member: "ClearanceType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ClearanceType.html"
---

# ClearanceType Property (IClearanceResult)

Gets the clearance type.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ClearanceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IClearanceResult
Dim value As System.Integer

value = instance.ClearanceType
```

### C#

```csharp
System.int ClearanceType {get;}
```

### C++/CLI

```cpp
property System.int ClearanceType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Clearance type as defined by [swClearanceType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swClearanceType_e.html)

## VBA Syntax

See [ClearanceResult::ClearanceType](ms-its:sldworksapivb6.chm::/sldworks~ClearanceResult~ClearanceType.html).

## Examples

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html) examples.

## See Also

[IClearanceResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult.html)
[IClearanceResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
