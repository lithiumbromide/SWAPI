---
title: "IgnoreClearanceEqualToSpecifiedValue Property (IClearanceVerificationMgr)"
project: "SOLIDWORKS API Help"
interface: "IClearanceVerificationMgr"
member: "IgnoreClearanceEqualToSpecifiedValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~IgnoreClearanceEqualToSpecifiedValue.html"
---

# IgnoreClearanceEqualToSpecifiedValue Property (IClearanceVerificationMgr)

Gets or sets whether to ignore clearances equal to or greater than [IClearanceVerificationMgr::GetMinimumAcceptableClearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~GetMinimumAcceptableClearance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreClearanceEqualToSpecifiedValue As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IClearanceVerificationMgr
Dim value As System.Boolean

instance.IgnoreClearanceEqualToSpecifiedValue = value

value = instance.IgnoreClearanceEqualToSpecifiedValue
```

### C#

```csharp
System.bool IgnoreClearanceEqualToSpecifiedValue {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnoreClearanceEqualToSpecifiedValue {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to ignore clearances equal to or greater than the specified value, false to not

## VBA Syntax

See [ClearanceVerificationMgr::IgnoreClearanceEqualToSpecifiedValue](ms-its:sldworksapivb6.chm::/sldworks~ClearanceVerificationMgr~IgnoreClearanceEqualToSpecifiedValue.html).

## Examples

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html) examples.

## Remarks

If this property is true, use [IClearanceVerificationMgr::SetMinimumAcceptableClearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~SetMinimumAcceptableClearance.html) to specify the minimum clearance value, at or above which clearances are ignored.

## See Also

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html)
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
