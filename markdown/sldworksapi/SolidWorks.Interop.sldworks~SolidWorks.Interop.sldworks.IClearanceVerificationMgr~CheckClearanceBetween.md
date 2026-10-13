---
title: "CheckClearanceBetween Property (IClearanceVerificationMgr)"
project: "SOLIDWORKS API Help"
interface: "IClearanceVerificationMgr"
member: "CheckClearanceBetween"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~CheckClearanceBetween.html"
---

# CheckClearanceBetween Property (IClearanceVerificationMgr)

Gets or sets the type of clearance check: between selected items or between selected items and the rest of the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckClearanceBetween As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IClearanceVerificationMgr
Dim value As System.Integer

instance.CheckClearanceBetween = value

value = instance.CheckClearanceBetween
```

### C#

```csharp
System.int CheckClearanceBetween {get; set;}
```

### C++/CLI

```cpp
property System.int CheckClearanceBetween {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of clearance check as defined by [swCheckClearanceBetween_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCheckClearanceBetween_e.html)

## VBA Syntax

See [ClearanceVerificationMgr::CheckClearanceBetween](ms-its:sldworksapivb6.chm::/sldworks~ClearanceVerificationMgr~CheckClearanceBetween.html).

## Examples

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html) examples.

## See Also

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html)
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
