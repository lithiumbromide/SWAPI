---
title: "SetUseSoftSpring2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetUseSoftSpring2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetUseSoftSpring2.html"
---

# SetUseSoftSpring2 Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::SetUseSoftSpring3](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetUseSoftSpring3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUseSoftSpring2( _
   ByVal BUseSoftSpring As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BUseSoftSpring As System.Integer
Dim value As System.Integer

value = instance.SetUseSoftSpring2(BUseSoftSpring)
```

### C#

```csharp
System.int SetUseSoftSpring2(
   System.int BUseSoftSpring
)
```

### C++/CLI

```cpp
System.int SetUseSoftSpring2(
   System.int BUseSoftSpring
)
```

### Parameters

- `BUseSoftSpring`: - 1 = Use soft spring to stabilize model
  - 0 = Do not use soft spring

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetUseSoftSpring2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetUseSoftSpring2.html).

## Remarks

Use [ICWDynamicStudyOptions::GetUseSoftSpring2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetUseSoftSpring2.html) to check the stability of the model.

To stabilize the model for final runs:

- set BUseSoftSpring = 0.
- use proper restraints.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
