---
title: "ClearanceValue Property (IClearanceResult)"
project: "SOLIDWORKS API Help"
interface: "IClearanceResult"
member: "ClearanceValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ClearanceValue.html"
---

# ClearanceValue Property (IClearanceResult)

Gets the clearance value.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ClearanceValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IClearanceResult
Dim value As System.Double

value = instance.ClearanceValue
```

### C#

```csharp
System.double ClearanceValue {get;}
```

### C++/CLI

```cpp
property System.double ClearanceValue {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Clearance value

## VBA Syntax

See [ClearanceResult::ClearanceValue](ms-its:sldworksapivb6.chm::/sldworks~ClearanceResult~ClearanceValue.html).

## Examples

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html) examples.

## Remarks

This property is valid only if [IClearanceResult::ClearanceType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ClearanceType.html) is [swClearanceType_e](ms-its:swconst.chm::/::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swClearanceType_e.html).swClearanceType_Distance.

## See Also

[IClearanceResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult.html)
[IClearanceResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
