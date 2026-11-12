---
title: "SetSectionParams Method (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "SetSectionParams"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~SetSectionParams.html"
---

# SetSectionParams Method (ICWLinkageRod)

Sets the specified cross-section parameter values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSectionParams( _
   ByVal NSectionType As System.Integer, _
   ByVal ArrayParamValues As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLinkageRod
Dim NSectionType As System.Integer
Dim ArrayParamValues As System.Object

instance.SetSectionParams(NSectionType, ArrayParamValues)
```

### C#

```csharp
void SetSectionParams(
   System.int NSectionType,
   System.object ArrayParamValues
)
```

### C++/CLI

```cpp
void SetSectionParams(
   System.int NSectionType,
   System.Object^ ArrayParamValues
)
```

### Parameters

- `NSectionType`: Cross-section parameter type as defined by [swsCRSectionType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCRSectionType_e.html)
- `ArrayParamValues`: Array of parameter values (see **Remarks**)

## VBA Syntax

See [CWLinkageRod::SetSectionParams](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~SetSectionParams.html).

## Examples

See the [ICWLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html) examples

## Remarks

If NSectionType is swsCRSectionType_e.:

- swsSolidCircular, then specify ArrayParamValues with an array containing outer radius.
- swsSolidRectangular, then specify ArrayParamValues with an array containing width and height.
- swsHollowCircular, then specify ArrayParamValues with an array containing outer radius and wall thickness.
- swsHollowRectangular, then specify ArrayParamValues with an array containing width, height, and wall thickness.

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
