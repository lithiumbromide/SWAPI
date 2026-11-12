---
title: "TreatSubAssembliesAsComponents Property (IClearanceVerificationMgr)"
project: "SOLIDWORKS API Help"
interface: "IClearanceVerificationMgr"
member: "TreatSubAssembliesAsComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr~TreatSubAssembliesAsComponents.html"
---

# TreatSubAssembliesAsComponents Property (IClearanceVerificationMgr)

Gets or sets whether to treat subassemblies as single components for clearance verification.

## Syntax

### Visual Basic (Declaration)

```vb
Property TreatSubAssembliesAsComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IClearanceVerificationMgr
Dim value As System.Boolean

instance.TreatSubAssembliesAsComponents = value

value = instance.TreatSubAssembliesAsComponents
```

### C#

```csharp
System.bool TreatSubAssembliesAsComponents {get; set;}
```

### C++/CLI

```cpp
property System.bool TreatSubAssembliesAsComponents {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to not check clearances between components within subassemblies, false to check them

## VBA Syntax

See [ClearanceVerificationMgr::TreatSubAssembliesAsComponents](ms-its:sldworksapivb6.chm::/sldworks~ClearanceVerificationMgr~TreatSubAssembliesAsComponents.html).

## Examples

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html) examples.

## See Also

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html)
[IClearanceVerificationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
